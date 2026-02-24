# Contracts Tab Rewrite Summary

**Date:** 2026-02-24  
**File:** `/Users/rook/workspace/the-factory/src/pages/hire-space/finance-tools/unified.astro`  
**Status:** ✅ COMPLETE

## Changes Made

### 1. CSS Added (lines 114-150 approx.)
Added comprehensive CSS for the new contracts layout to the main `<style>` block:

- `.ctr-layout` - Flexbox container with sidebar + main area
- `.ctr-sidebar` - Left sidebar (260px wide)
- `.ctr-sidebar-item` - Individual contract items in sidebar
- `.ctr-main` - Right main content area
- `.ctr-topbar` - Top bar within each contract
- `.ctr-subtabs` - Sub-navigation tabs within contracts
- `.ctr-sub-c` - Sub-tab content containers
- `.ctr-section` - Content sections
- `.upload-box` - Document upload areas
- `.contact-list` & `.contact-item` - Contact selection UI
- `.win-contract-box` - Win contract section styling
- Radio button selectors for sidebar navigation (#ctr-select-1, #ctr-select-2)
- Radio button selectors for sub-tabs (#ctr-sub-details, #ctr-sub-payments, #ctr-sub-cancel, #ctr-sub-timesold)

### 2. HTML Content Replaced (lines 208-522 approx.)
Completely replaced the Contracts tab content with new sidebar + main layout design:

#### Structure:
```
<div class="l1-c l1-c-contracts"> (KEPT - line 207)
  
  <!-- Radio inputs for contract selection -->
  <input type="radio" name="ctr-select" id="ctr-select-1" checked/>
  <input type="radio" name="ctr-select" id="ctr-select-2"/>
  
  <div class="ctr-layout">
    <!-- LEFT SIDEBAR -->
    <div class="ctr-sidebar">
      - Header: "Contracts (2)"
      - Contract 1: The Grand Ballroom (Draft, £14,850)
      - Contract 2: DJ Sounds Ltd (Signed, £3,500)
    </div>
    
    <!-- RIGHT MAIN: CONTRACT 1 -->
    <div class="ctr-main ctr-main-1">
      - Top bar with contract name, status badges, links
      - Action buttons (Signed outside Juro)
      - Sub-tabs: Contract Details, Client Payments, Cancellations, Time Sold
      
      **Contract Details sub-tab includes:**
      - Event & Client Details
      - Event Specific Terms
      - Venue / Suppliers section (with venue selector, deal type, commission %)
      - Key Contact selection
      - Documents upload area
      - Deliverables & Venue Specific Terms
      - Payments table
      - Contract Items table (5 line items totaling £14,850)
      - **WIN THIS CONTRACT section:**
        - Pre-win checklist (4 checks: 2 failing, 2 passing)
        - Commission Summary table (per-item editable percentages)
        - Manual commission confirmation input (£1,914.00)
        - Win button (disabled due to failing checks)
      
      **Other sub-tabs:**
      - Client Payments (placeholder)
      - Cancellations (placeholder)
      - Time Sold (placeholder)
    </div>
    
    <!-- RIGHT MAIN: CONTRACT 2 -->
    <div class="ctr-main ctr-main-2">
      - Simplified contract view (DJ Sounds Ltd)
      - Contract details
      - Contract items (2 line items totaling £3,500)
      - Fully signed status indicator
    </div>
  </div>
  
</div><!-- /contracts tab --> (KEPT - line 523)
```

### 3. What Was NOT Changed
- ✅ Main `<style>` block structure (only appended to)
- ✅ Everything before the Contracts tab (lines 1-206)
- ✅ Everything after the Contracts tab (lines 524+)
- ✅ Invoices tab
- ✅ Finance Operations section

## Key Features

### Sidebar Navigation
- Two contracts listed with status badges and amounts
- Click to switch between contracts using CSS-only radio button technique
- Visual indicator (blue left border) shows selected contract

### Per-Contract View
- Each contract has its own main panel
- Top bar shows contract name, template type, status, amount, and external links
- Sub-tabs for organizing contract information

### Win Contract Section (Contract 1 only)
- Pre-win checklist with pass/fail indicators
- Commission summary table with editable percentages per line item
- Guard rail: manual typing of total commission to confirm review
- Disabled win button until all checks pass
- TODO notes for future Juro API integration

### Data Shown
**Contract 1: The Grand Ballroom**
- Status: Draft
- Amount: £14,850.00 (net)
- Items: Room hire, Catering (85 pax), AV package, Tea/coffee, Breakout rooms
- Commission: £1,914.00 (~12.9% blended)
- Checks: 2 failing (signed contract, venue T&Cs not uploaded)

**Contract 2: DJ Sounds Ltd**
- Status: Signed
- Amount: £3,500.00 (net)
- Items: DJ set (4 hours), Lighting package
- Commission: £420.00 (12%)
- Fully signed and won

## Technical Implementation
- Pure CSS-only navigation (no JavaScript required)
- Radio buttons control sidebar selection and sub-tab visibility
- Responsive flex layout
- Consistent styling with existing design system

## Files Backed Up
- `unified.astro.backup` - Backup created before changes

## Testing Recommendations
1. Verify sidebar navigation switches between contracts correctly
2. Test sub-tab navigation within each contract
3. Verify all form inputs are functional (venue selector, commission inputs, etc.)
4. Check that external links (Retool, Juro) work
5. Verify styling consistency across different screen sizes
6. Test the manual commission confirmation input (no copy/paste should work)

## Future Enhancements (as noted in TODOs)
- Pull signed contract status from Juro API automatically
- Allow countersigning from this screen
- Auto-pull T&Cs from booking system
- Implement actual sub-tab content for Client Payments, Cancellations, Time Sold
- Trigger Juro countersign directly from this screen
