#!/usr/bin/env python3
"""
Subconscious Bootstrap Script
Analyzes the last 14 days of data to establish baseline patterns for anomaly detection.
This script CAN use LLM calls since it runs once for initial setup.
"""

import os
import json
import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
import glob
import sys

# Add workspace to Python path
sys.path.insert(0, '/Users/rook/workspace')

def get_date_range(days_back=14):
    """Get list of dates for the last N days"""
    end_date = datetime.now()
    dates = []
    for i in range(days_back):
        date = end_date - timedelta(days=i)
        dates.append(date.strftime("%Y-%m-%d"))
    return sorted(dates)

def analyze_daily_journals(workspace_path):
    """Analyze daily journal files to extract patterns"""
    memory_path = Path(workspace_path) / "memory"
    dates = get_date_range(14)
    
    journal_patterns = {
        "conversation_frequency": {},
        "cron_patterns": {},
        "activity_patterns": {},
        "project_mentions": {}
    }
    
    print("📖 Analyzing daily journals...")
    
    for date in dates:
        journal_files = list(memory_path.glob(f"{date}*.md"))
        
        for journal_file in journal_files:
            print(f"  📄 {journal_file.name}")
            try:
                with open(journal_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract conversation patterns
                if "Diego" in content or "conversation with Diego" in content:
                    journal_patterns["conversation_frequency"][date] = content.lower().count("diego")
                else:
                    journal_patterns["conversation_frequency"][date] = 0
                
                # Extract cron patterns
                cron_matches = re.findall(r'(\w+.*?(?:OK|Failed|Timed out|Error).*?(?:\d+s|\d+m))', content, re.IGNORECASE)
                for match in cron_matches:
                    cron_name = match.split(':')[0].strip()
                    status = "success" if "OK" in match else "failure"
                    
                    if cron_name not in journal_patterns["cron_patterns"]:
                        journal_patterns["cron_patterns"][cron_name] = {"success": 0, "failure": 0, "dates": []}
                    
                    journal_patterns["cron_patterns"][cron_name][status] += 1
                    journal_patterns["cron_patterns"][cron_name]["dates"].append(date)
                
                # Extract project mentions
                project_keywords = ["Darwin", "Chowdown", "Factory", "Bluesky", "Research Radar", 
                                  "Blog", "Moltbook", "WhatsApp", "Gmail", "Security Scan"]
                
                for project in project_keywords:
                    count = content.count(project)
                    if count > 0:
                        if project not in journal_patterns["project_mentions"]:
                            journal_patterns["project_mentions"][project] = {}
                        journal_patterns["project_mentions"][project][date] = count
                        
            except Exception as e:
                print(f"  ⚠️ Error reading {journal_file}: {e}")
    
    return journal_patterns

def analyze_telegram_conversations(workspace_path):
    """Analyze Telegram archives to understand conversation patterns"""
    telegram_path = Path(workspace_path) / "memory" / "telegram"
    dates = get_date_range(14)
    
    conversation_patterns = {
        "daily_message_counts": {},
        "avg_messages_per_day": 0,
        "quiet_days": [],
        "busy_days": []
    }
    
    print("📱 Analyzing Telegram conversations...")
    
    total_messages = 0
    days_with_data = 0
    
    for date in dates:
        # Look for DM files for that date
        dm_files = list(telegram_path.glob(f"dm-diego-{date}.md"))
        
        if dm_files:
            try:
                with open(dm_files[0], 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Count messages (rough approximation based on timestamps)
                message_count = len(re.findall(r'\[\d{2}:\d{2}\]', content))
                conversation_patterns["daily_message_counts"][date] = message_count
                total_messages += message_count
                days_with_data += 1
                
                # Categorize days
                if message_count == 0:
                    conversation_patterns["quiet_days"].append(date)
                elif message_count > 50:  # Arbitrary threshold for "busy"
                    conversation_patterns["busy_days"].append(date)
                    
            except Exception as e:
                print(f"  ⚠️ Error reading telegram file for {date}: {e}")
        else:
            conversation_patterns["daily_message_counts"][date] = 0
            conversation_patterns["quiet_days"].append(date)
    
    if days_with_data > 0:
        conversation_patterns["avg_messages_per_day"] = total_messages / days_with_data
    
    return conversation_patterns

def analyze_git_repositories(workspace_path):
    """Analyze git repositories for commit patterns"""
    workspace = Path(workspace_path)
    dates = get_date_range(14)
    
    git_patterns = {
        "repositories": {},
        "total_commits_14d": 0,
        "active_repos": [],
        "stale_repos": []
    }
    
    print("🔧 Analyzing git repositories...")
    
    # Find all .git directories
    git_dirs = []
    try:
        result = subprocess.run(
            ['find', str(workspace), '-name', '.git', '-type', 'd'],
            capture_output=True, text=True, timeout=30
        )
        git_dirs = result.stdout.strip().split('\n') if result.stdout.strip() else []
    except Exception as e:
        print(f"  ⚠️ Error finding git repos: {e}")
    
    for git_dir in git_dirs:
        if not git_dir:
            continue
            
        repo_path = Path(git_dir).parent
        repo_name = repo_path.name
        
        print(f"  📁 {repo_name}")
        
        try:
            # Get commits from last 14 days
            since_date = (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d")
            result = subprocess.run(
                ['git', 'log', '--since', since_date, '--oneline'],
                cwd=repo_path, capture_output=True, text=True, timeout=10
            )
            
            commits = result.stdout.strip().split('\n') if result.stdout.strip() else []
            commit_count = len([c for c in commits if c])
            
            git_patterns["repositories"][repo_name] = {
                "commits_14d": commit_count,
                "last_commit_date": None,
                "path": str(repo_path)
            }
            
            # Get last commit date
            if commit_count > 0:
                last_commit_result = subprocess.run(
                    ['git', 'log', '-1', '--format=%ci'],
                    cwd=repo_path, capture_output=True, text=True, timeout=5
                )
                if last_commit_result.stdout.strip():
                    git_patterns["repositories"][repo_name]["last_commit_date"] = last_commit_result.stdout.strip()
            
            git_patterns["total_commits_14d"] += commit_count
            
            # Categorize repos
            if commit_count > 0:
                git_patterns["active_repos"].append(repo_name)
            else:
                git_patterns["stale_repos"].append(repo_name)
                
        except Exception as e:
            print(f"    ⚠️ Error analyzing {repo_name}: {e}")
            git_patterns["repositories"][repo_name] = {
                "commits_14d": 0,
                "last_commit_date": None,
                "path": str(repo_path),
                "error": str(e)
            }
    
    return git_patterns

def analyze_memory_files(workspace_path):
    """Analyze memory file modification patterns"""
    memory_path = Path(workspace_path) / "memory"
    
    file_patterns = {
        "recent_files": [],
        "stale_files": [],
        "modification_frequency": {}
    }
    
    print("📁 Analyzing memory file patterns...")
    
    try:
        # Get all files in memory directory
        memory_files = list(memory_path.glob("**/*.md"))
        memory_files.extend(list(memory_path.glob("**/*.txt")))
        memory_files.extend(list(memory_path.glob("**/*.json")))
        
        now = datetime.now()
        
        for file_path in memory_files:
            if file_path.is_file():
                # Get modification time
                mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
                days_old = (now - mod_time).days
                
                file_info = {
                    "path": str(file_path.relative_to(Path(workspace_path))),
                    "days_old": days_old,
                    "size_bytes": file_path.stat().st_size
                }
                
                if days_old <= 2:
                    file_patterns["recent_files"].append(file_info)
                elif days_old > 7:
                    file_patterns["stale_files"].append(file_info)
    
    except Exception as e:
        print(f"  ⚠️ Error analyzing memory files: {e}")
    
    return file_patterns

def generate_world_state(workspace_path):
    """Generate the world-state.json file with all patterns"""
    print("\n🧠 Generating world-state.json...")
    
    world_state = {
        "generated_at": datetime.now().isoformat(),
        "analysis_period": {
            "days_analyzed": 14,
            "start_date": (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d"),
            "end_date": datetime.now().strftime("%Y-%m-%d")
        },
        "patterns": {}
    }
    
    # Analyze all data sources
    world_state["patterns"]["journal_analysis"] = analyze_daily_journals(workspace_path)
    world_state["patterns"]["conversation_analysis"] = analyze_telegram_conversations(workspace_path)  
    world_state["patterns"]["git_analysis"] = analyze_git_repositories(workspace_path)
    world_state["patterns"]["file_analysis"] = analyze_memory_files(workspace_path)
    
    # Calculate derived metrics
    journal_data = world_state["patterns"]["journal_analysis"]
    conversation_data = world_state["patterns"]["conversation_analysis"]
    
    # Diego conversation frequency baseline
    msg_counts = list(conversation_data["daily_message_counts"].values())
    avg_messages = sum(msg_counts) / len(msg_counts) if msg_counts else 0
    
    world_state["baselines"] = {
        "diego_avg_messages_per_day": avg_messages,
        "diego_quiet_threshold": 2,  # Days without messages before flagging
        "total_repos_tracked": len(world_state["patterns"]["git_analysis"]["repositories"]),
        "avg_commits_per_week": world_state["patterns"]["git_analysis"]["total_commits_14d"] / 2,
        "cron_failure_threshold": 2  # Consecutive failures before flagging
    }
    
    # Expectations for common patterns
    world_state["expectations"] = {
        "diego_messages": {
            "min_per_week": max(1, int(avg_messages * 5)),  # Weekday average
            "max_quiet_days": 2
        },
        "git_activity": {
            "active_repos": world_state["patterns"]["git_analysis"]["active_repos"],
            "expected_weekly_commits": world_state["patterns"]["git_analysis"]["total_commits_14d"] / 2
        },
        "cron_health": {
            "critical_crons": ["Morning Briefing", "Research Radar", "Bluesky Engagement", 
                             "Daily Calendar Briefing", "Security Scan"],
            "max_consecutive_failures": 2
        }
    }
    
    # Save world state
    output_path = Path(workspace_path) / "memory" / "world-state.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(world_state, f, indent=2, ensure_ascii=False)
    
    print(f"✅ World state saved to {output_path}")
    print(f"📊 Analysis summary:")
    print(f"  • {len(world_state['patterns']['git_analysis']['repositories'])} git repositories tracked")
    print(f"  • Average {avg_messages:.1f} messages/day with Diego")
    print(f"  • {len(world_state['patterns']['git_analysis']['active_repos'])} active repos in 14d")
    print(f"  • {len(world_state['patterns']['journal_analysis']['cron_patterns'])} cron jobs identified")
    
    return world_state

def main():
    workspace_path = "/Users/rook/workspace"
    
    print("🚀 Starting subconscious bootstrap analysis...")
    print(f"📁 Workspace: {workspace_path}")
    
    try:
        world_state = generate_world_state(workspace_path)
        print("\n✅ Bootstrap complete! World state patterns established.")
        return 0
    except Exception as e:
        print(f"\n❌ Bootstrap failed: {e}")
        return 1

if __name__ == "__main__":
    exit(main())