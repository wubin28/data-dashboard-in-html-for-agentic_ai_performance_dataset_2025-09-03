# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a data analysis project for the "Agentic AI Performance Dataset 2025". The project is currently in its initial state on the main branch, containing only the raw dataset and project configuration.

## Current State (main branch)

The repository contains:
- **Dataset**: `first-80-rows-agentic_ai_performance_dataset_20250622.xlsx` (19KB Excel file with 80 rows of AI performance data)
- **Configuration**: `.codebuddy/analysis-summary.json` with project specifications
- **Git setup**: `.gitignore` configured for the project

## Planned Architecture (from .codebuddy config)

According to the project configuration, this will be an "Agentic AI数据分析看板系统" with:

**Features:**
- Excel数据读取处理 (Excel data reading and processing)
- 多维度数据分析 (Multi-dimensional data analysis) 
- 静态HTML看板生成 (Static HTML dashboard generation)
- 数据可视化图表 (Data visualization charts)

**Tech Stack:**
- Backend: Python + pandas + openpyxl + numpy
- Frontend: HTML5 + CSS3 + Chart.js + Bootstrap + JavaScript
- Output: 静态HTML文件 + 内联资源 (Static HTML files with inline resources)

**Design Approach:**
- 现代简约浅色调设计 (Modern minimalist light color design)
- 白色主背景配浅蓝色卡片 (White background with light blue cards)
- 响应式布局 (Responsive layout)
- 统计卡片、排名列表和交互式图表 (Statistics cards, ranking lists, and interactive charts)

## Development Status

Based on the configuration, the planned development phases are:
1. ✅ 创建Python数据读取和预处理模块 (Create Python data reading and preprocessing module)
2. ✅ 实现多模态智能体类型占比分析功能 (Implement multimodal agent type ratio analysis)
3. ✅ 实现多模态大模型架构占比分析功能 (Implement multimodal model architecture ratio analysis) 
4. ✅ 实现任务类别智能体公正性中位数分析功能 (Implement task category agent fairness median analysis)
5. 🔄 开发HTML数据看板生成器 (Develop HTML dashboard generator)
6. ⏸️ 集成图表可视化和样式设计 (Integrate chart visualization and style design)

## Branch Structure

- `main`: Initial state with dataset only
- `by-codebuddy-ide-with-claude-sonnet-4-in-new-way-without-plan-mode`: Implementation branch
- `by-codebuddy-ide-with-claude-sonnet-4-in-new-way-in-plan-mode`: Alternative implementation branch

## Expected Commands (when implemented)

```bash
# Run data analysis
python analyze_data.py

# View dashboard
# Open generated HTML file in browser
```