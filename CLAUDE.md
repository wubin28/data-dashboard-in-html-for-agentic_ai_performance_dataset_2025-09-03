# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a data analysis project for the "Agentic AI Performance Dataset 2025". The project creates a static HTML dashboard that analyzes AI agent performance data from Excel files and presents insights through interactive charts.

## Commands

```bash
# Run data analysis and generate dashboard
python analyze_data.py

# View dashboard (open in browser)
# Open data-dashboard.html in your preferred browser
```

## Architecture

**Data Pipeline**: Excel Dataset → Python Analysis → JSON Output → HTML Dashboard

**Core Components**:
- `analyze_data.py`: Python script that reads Excel data, performs 3 types of analysis (multimodal agent types, model architectures, task fairness), and generates JSON output
- `data-dashboard.html`: Self-contained HTML dashboard with inline CSS/JS using Chart.js for visualizations
- `dashboard_data.json`: Generated data consumed by the HTML dashboard
- `analysis_results.json`: Complete analysis results for debugging/validation

**Technology Stack**:
- Backend: Python + pandas + openpyxl + numpy
- Frontend: HTML5 + CSS3 + Chart.js + Bootstrap (all inlined for portability)
- No build system required - direct Python execution

## Key Design Patterns

1. **Self-Contained Output**: The HTML dashboard includes all CSS and JavaScript inline to eliminate external dependencies
2. **Responsive Design**: Mobile-first approach with Bootstrap grid system
3. **Modern Light Theme**: White background with light blue accent cards
4. **JSON Data Flow**: Analysis results are serialized to JSON for both debugging and dashboard consumption

## Development Notes

- No package manager or virtual environment required - uses standard Python libraries
- Excel files are the single source of truth for data
- The project generates static output suitable for sharing without server requirements
- Multiple AI model integration scripts are provided in `Configuration Scripts/` for different development environments