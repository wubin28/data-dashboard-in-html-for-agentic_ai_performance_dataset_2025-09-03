import pandas as pd
import json
import numpy as np

def analyze_agentic_ai_data():
    """
    分析Agentic AI Performance Dataset 2025数据集
    """
    try:
        # 读取Excel文件
        df = pd.read_excel('first-80-rows-agentic_ai_performance_dataset_20250622.xlsx')
        
        print(f"成功读取数据，共 {len(df)} 条记录")
        print(f"数据列名: {list(df.columns)}")
        
        # 显示前几行数据以了解结构
        print("\n数据前5行:")
        print(df.head())
        
        # 检查数据类型
        print("\n数据类型:")
        print(df.dtypes)
        
        # 检查缺失值
        print("\n缺失值统计:")
        print(df.isnull().sum())
        
        # 分析问题1：支持多模态处理的智能体类型占比排名前三
        print("\n=== 问题1分析 ===")
        if 'multimodal_capability' in df.columns and 'agent_type' in df.columns:
            # 计算每种智能体类型中支持多模态的占比
            agent_multimodal_stats = df.groupby('agent_type').agg({
                'multimodal_capability': ['count', 'sum']
            }).round(4)
            
            agent_multimodal_stats.columns = ['total_count', 'multimodal_count']
            agent_multimodal_stats['multimodal_ratio'] = (
                agent_multimodal_stats['multimodal_count'] / 
                agent_multimodal_stats['total_count']
            ).round(4)
            
            top3_agent_types = agent_multimodal_stats.sort_values(
                'multimodal_ratio', ascending=False
            ).head(3)
            
            print("支持多模态处理的智能体类型占比排名前三:")
            print(top3_agent_types)
        
        # 分析问题2：支持多模态处理的大模型架构占比排名前三
        print("\n=== 问题2分析 ===")
        if 'multimodal_capability' in df.columns and 'model_architecture' in df.columns:
            # 计算每种大模型架构中支持多模态的占比
            model_multimodal_stats = df.groupby('model_architecture').agg({
                'multimodal_capability': ['count', 'sum']
            }).round(4)
            
            model_multimodal_stats.columns = ['total_count', 'multimodal_count']
            model_multimodal_stats['multimodal_ratio'] = (
                model_multimodal_stats['multimodal_count'] / 
                model_multimodal_stats['total_count']
            ).round(4)
            
            top3_model_architectures = model_multimodal_stats.sort_values(
                'multimodal_ratio', ascending=False
            ).head(3)
            
            print("支持多模态处理的大模型架构占比排名前三:")
            print(top3_model_architectures)
        
        # 分析问题3：各任务类别对应的公正性中位数排名前三
        print("\n=== 问题3分析 ===")
        if 'task_category' in df.columns and 'bias_detection' in df.columns:
            # 计算每种任务类别的公正性中位数
            task_bias_median = df.groupby('task_category')['bias_detection'].median().sort_values(ascending=False)
            top3_task_categories = task_bias_median.head(3)
            
            print("各任务类别公正性中位数排名前三:")
            print(top3_task_categories)
        
        # 准备数据用于HTML可视化
        analysis_results = {
            'total_records': len(df),
            'columns': list(df.columns),
            'agent_type_multimodal': top3_agent_types.to_dict('index') if 'multimodal_capability' in df.columns and 'agent_type' in df.columns else {},
            'model_architecture_multimodal': top3_model_architectures.to_dict('index') if 'multimodal_capability' in df.columns and 'model_architecture' in df.columns else {},
            'task_category_bias': top3_task_categories.to_dict() if 'task_category' in df.columns and 'bias_detection' in df.columns else {}
        }
        
        # 保存分析结果到JSON文件
        with open('analysis_results.json', 'w', encoding='utf-8') as f:
            json.dump(analysis_results, f, ensure_ascii=False, indent=2, default=str)
        
        print(f"\n分析完成！结果已保存到 analysis_results.json")
        return analysis_results
        
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return None

if __name__ == "__main__":
    results = analyze_agentic_ai_data()