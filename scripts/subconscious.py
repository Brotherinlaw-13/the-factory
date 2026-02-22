#!/usr/bin/env python3
"""
Subconscious Anomaly Detector
Pure Python script (NO LLM calls) that runs every 15 minutes to detect anomalies.
Compares current state against established patterns and writes signals.
"""

import os
import json
import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
import glob

def load_world_state(workspace_path):
    """Load the world-state.json file with baseline patterns"""
    world_state_path = Path(workspace_path) / "memory" / "world-state.json"
    
    try:
        with open(world_state_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        return None

def check_diego_conversation_patterns(workspace_path, world_state):
    """Check if Diego conversation patterns are anomalous"""
    signals = []
    
    if not world_state or "baselines" not in world_state:
        return signals
    
    telegram_path = Path(workspace_path) / "memory" / "telegram"
    now = datetime.now()
    
    # Check last 3 days for messages
    quiet_days = 0
    for i in range(3):
        check_date = (now - timedelta(days=i)).strftime("%Y-%m-%d")
        dm_file = telegram_path / f"dm-diego-{check_date}.md"
        
        if dm_file.exists():
            try:
                with open(dm_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                message_count = len(re.findall(r'\[\d{2}:\d{2}\]', content))
                if message_count == 0:
                    quiet_days += 1
            except:
                quiet_days += 1
        else:
            quiet_days += 1
    
    # Flag if no messages for >48h on weekdays
    if quiet_days >= 2 and now.weekday() < 5:  # Monday = 0, Friday = 4
        signals.append({
            "type": "anomaly",
            "severity": "medium",
            "description": f"Diego: Sin mensajes en {quiet_days} días (días laborables)",
            "source": "telegram_dm",
            "detected_at": now.isoformat()
        })
    
    return signals

def check_git_activity(workspace_path, world_state):
    """Check git repositories for unusual inactivity"""
    signals = []
    
    if not world_state or "patterns" not in world_state:
        return signals
    
    git_data = world_state["patterns"].get("git_analysis", {})
    repositories = git_data.get("repositories", {})
    
    for repo_name, repo_info in repositories.items():
        repo_path = Path(repo_info.get("path", ""))
        
        if not repo_path.exists():
            continue
            
        try:
            # Check commits in last 7 days
            since_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
            result = subprocess.run(
                ['git', 'log', '--since', since_date, '--oneline'],
                cwd=repo_path, capture_output=True, text=True, timeout=10
            )
            
            recent_commits = len([c for c in result.stdout.strip().split('\n') if c])
            baseline_commits = repo_info.get("commits_14d", 0)
            expected_weekly = baseline_commits / 2  # 14d -> 7d expectation
            
            # Flag if significantly below expected activity
            if expected_weekly > 2 and recent_commits == 0:
                signals.append({
                    "type": "anomaly", 
                    "severity": "low",
                    "description": f"{repo_name}: 0 commits en 7 días (media: {expected_weekly:.1f}/semana)",
                    "source": "git_log",
                    "detected_at": datetime.now().isoformat()
                })
            
        except Exception:
            # Don't signal on git errors, just skip
            continue
    
    return signals

def check_cron_health(workspace_path, world_state):
    """Check cron job health patterns"""
    signals = []
    
    # Read cron health file
    cron_health_path = Path(workspace_path) / "memory" / "cron-health.txt"
    
    if cron_health_path.exists():
        try:
            with open(cron_health_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            
            # Parse timestamp from cron health
            if content:
                # Extract timestamp if format is recognizable
                import dateutil.parser
                try:
                    last_update = dateutil.parser.parse(content, fuzzy=True)
                    minutes_ago = (datetime.now() - last_update).total_seconds() / 60
                    
                    if minutes_ago > 45:  # Cron health should update every 30min
                        signals.append({
                            "type": "anomaly",
                            "severity": "medium", 
                            "description": f"Cron health: Sin actualizaciones en {int(minutes_ago)} minutos",
                            "source": "cron_health",
                            "detected_at": datetime.now().isoformat()
                        })
                except:
                    pass
                    
        except Exception:
            pass
    
    # Check recent daily journals for repeated cron failures
    memory_path = Path(workspace_path) / "memory"
    recent_failures = {}
    
    for i in range(3):  # Check last 3 days
        date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        journal_files = list(memory_path.glob(f"{date}*.md"))
        
        for journal_file in journal_files:
            try:
                with open(journal_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Look for failure patterns
                failures = re.findall(r'(\w+.*?)(?:Failed|Timed out|Error)', content, re.IGNORECASE)
                for failure in failures:
                    cron_name = failure.strip().split(':')[0]
                    if cron_name not in recent_failures:
                        recent_failures[cron_name] = 0
                    recent_failures[cron_name] += 1
                    
            except Exception:
                continue
    
    # Signal if any cron has >2 failures in 3 days
    for cron_name, failure_count in recent_failures.items():
        if failure_count > 2:
            signals.append({
                "type": "anomaly",
                "severity": "high",
                "description": f"{cron_name}: {failure_count} errores en 3 días",
                "source": "daily_journals", 
                "detected_at": datetime.now().isoformat()
            })
    
    return signals

def check_telegram_activity(workspace_path, world_state):
    """Check Telegram channel activity for unusual quiet periods"""
    signals = []
    
    telegram_path = Path(workspace_path) / "memory" / "telegram"
    now = datetime.now()
    
    # Check The Factory activity
    today = now.strftime("%Y-%m-%d")
    yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")
    
    factory_files = [
        telegram_path / f"the-factory-{today}.md",
        telegram_path / f"the-factory-{yesterday}.md"
    ]
    
    total_factory_activity = 0
    for factory_file in factory_files:
        if factory_file.exists():
            try:
                with open(factory_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Count messages roughly by timestamps
                activity = len(re.findall(r'\[\d{2}:\d{2}\]', content))
                total_factory_activity += activity
            except Exception:
                continue
    
    # Flag if Factory is unusually quiet (baseline would be from world_state)
    if total_factory_activity < 5 and now.weekday() < 5:  # Weekday threshold
        signals.append({
            "type": "reminder",
            "severity": "low",
            "description": f"Factory: Actividad baja ({total_factory_activity} mensajes en 2 días)",
            "source": "telegram_factory",
            "detected_at": now.isoformat()
        })
    
    return signals

def check_stale_files(workspace_path, world_state):
    """Check for stagnant progress files or important documents"""
    signals = []
    
    progress_path = Path(workspace_path) / "memory" / "progress"
    
    if progress_path.exists():
        for progress_file in progress_path.glob("*.md"):
            try:
                mod_time = datetime.fromtimestamp(progress_file.stat().st_mtime)
                days_old = (datetime.now() - mod_time).days
                
                # Read file to check if it's still IN_PROGRESS
                with open(progress_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if "Status: IN_PROGRESS" in content and days_old > 3:
                    signals.append({
                        "type": "reminder",
                        "severity": "low", 
                        "description": f"Progreso estancado: {progress_file.name} ({days_old} días)",
                        "source": "progress_files",
                        "detected_at": datetime.now().isoformat()
                    })
                    
            except Exception:
                continue
    
    return signals

def write_signals(workspace_path, signals):
    """Write signals to the signals.json file"""
    signals_path = Path(workspace_path) / "memory" / "signals.json"
    
    signal_data = {
        "generated_at": datetime.now().isoformat(),
        "signals": signals
    }
    
    with open(signals_path, 'w', encoding='utf-8') as f:
        json.dump(signal_data, f, indent=2, ensure_ascii=False)
    
    return len(signals)

def main():
    workspace_path = "/Users/rook/workspace"
    
    # Load world state (baseline patterns)
    world_state = load_world_state(workspace_path)
    
    if not world_state:
        # No world state available, generate empty signals
        write_signals(workspace_path, [])
        return 0
    
    # Collect signals from all checks
    all_signals = []
    
    try:
        all_signals.extend(check_diego_conversation_patterns(workspace_path, world_state))
        all_signals.extend(check_git_activity(workspace_path, world_state))
        all_signals.extend(check_cron_health(workspace_path, world_state))
        all_signals.extend(check_telegram_activity(workspace_path, world_state))
        all_signals.extend(check_stale_files(workspace_path, world_state))
        
        # Write signals file
        signal_count = write_signals(workspace_path, all_signals)
        
        return 0
        
    except Exception as e:
        # On any error, write empty signals file
        write_signals(workspace_path, [])
        return 1

if __name__ == "__main__":
    exit(main())