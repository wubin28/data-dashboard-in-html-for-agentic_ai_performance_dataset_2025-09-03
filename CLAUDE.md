# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a complete data analysis and dashboard project for the "Agentic AI Performance Dataset 2025". The project has been implemented with Python data analysis backend and HTML/CSS/JavaScript frontend.

## Current Implementation

The repository contains:
- **Datasets**:
  - `first-80-rows-agentic_ai_performance_dataset_20250622.xlsx` (original dataset)
  - `correct-answers-for-80-rows.xlsx` (validation data)
- **Analysis Engine**: `analyze_data.py` (Python script with pandas for data processing)
- **Dashboard**: `data-dashboard.html` (complete HTML dashboard with Chart.js visualizations)
- **Generated Data**:
  - `analysis_results.json` (raw analysis output)
  - `dashboard_data.json` (formatted data for dashboard)
- **Configuration Scripts**: PowerShell and shell scripts for LLM API integration

## Architecture

**Data Flow:**
1. `analyze_data.py` reads Excel files using pandas
2. Processes data for multimodal agent analysis and fairness metrics
3. Outputs structured JSON data
4. `data-dashboard.html` consumes JSON for interactive visualizations

**Tech Stack:**
- **Backend**: Python + pandas + openpyxl
- **Frontend**: HTML5 + CSS3 + Chart.js + vanilla JavaScript
- **Output**: Self-contained HTML with inline resources and external CDN dependencies

**Key Analysis Functions:**
- `analyze_multimodal_agent_types()`: Agent type distribution analysis
- `analyze_multimodal_architectures()`: Model architecture ratio analysis
- `analyze_task_fairness()`: Task category fairness median calculations

## Common Commands

```bash
# Run complete data analysis and generate dashboard data
python analyze_data.py

# View dashboard (requires HTTP server for CORS)
# Option 1: Python built-in server
python -m http.server 8000
# Then open http://localhost:8000/data-dashboard.html

# Option 2: Direct file access (may have CORS issues)
# Open data-dashboard.html directly in browser
```

## Development Notes

- Dashboard uses Chart.js for all visualizations (pie charts, bar charts, line charts)
- Data processing handles UTF-8 encoding for Chinese text
- HTML dashboard is responsive with gradient backgrounds and card-based layout
- All external dependencies loaded via CDN (Chart.js)
- JSON data files are generated automatically by the Python analysis script