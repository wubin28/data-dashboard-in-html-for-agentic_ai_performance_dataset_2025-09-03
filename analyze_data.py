import pandas as pd
import json

def analyze_data():
    # Read Excel file with proper headers
    df = pd.read_excel('first-80-rows-agentic_ai_performance_dataset_20250622.xlsx', header=0)
    new_header = df.iloc[0] 
    df = df[1:]  
    df.columns = new_header
    
    # Convert relevant columns to proper data types
    df['multimodal_capability'] = df['multimodal_capability'].astype(bool)
    df['bias_detection_score'] = pd.to_numeric(df['bias_detection_score'], errors='coerce')
    
    print(f"Successfully processed {len(df)} records")
    
    # Question 1: Top 3 agent types by multimodal capability percentage
    agent_stats = df.groupby('agent_type').agg({
        'multimodal_capability': ['count', 'sum']
    })
    agent_stats.columns = ['total_count', 'multimodal_count']
    agent_stats['multimodal_ratio'] = (agent_stats['multimodal_count'] / agent_stats['total_count'] * 100).round(2)
    top3_agent_types = agent_stats.sort_values('multimodal_ratio', ascending=False).head(3)
    
    # Question 2: Top 3 model architectures by multimodal capability percentage  
    model_stats = df.groupby('model_architecture').agg({
        'multimodal_capability': ['count', 'sum']
    })
    model_stats.columns = ['total_count', 'multimodal_count']
    model_stats['multimodal_ratio'] = (model_stats['multimodal_count'] / model_stats['total_count'] * 100).round(2)
    top3_model_architectures = model_stats.sort_values('multimodal_ratio', ascending=False).head(3)
    
    # Question 3: Top 3 task categories by bias detection median score
    task_bias_median = df.groupby('task_category')['bias_detection_score'].median().sort_values(ascending=False).head(3)
    
    # Prepare data for HTML dashboard
    results = {
        'total_records': len(df),
        'agent_type_multimodal': {
            'labels': list(top3_agent_types.index),
            'ratios': list(top3_agent_types['multimodal_ratio']),
            'counts': list(top3_agent_types['multimodal_count']),
            'totals': list(top3_agent_types['total_count'])
        },
        'model_architecture_multimodal': {
            'labels': list(top3_model_architectures.index),
            'ratios': list(top3_model_architectures['multimodal_ratio']),
            'counts': list(top3_model_architectures['multimodal_count']),
            'totals': list(top3_model_architectures['total_count'])
        },
        'task_category_bias': {
            'labels': list(task_bias_median.index),
            'medians': list(task_bias_median.values)
        }
    }
    
    print("Analysis Results:")
    print("="*50)
    print("Question 1 - Top 3 Agent Types by Multimodal Support:")
    for i, (agent_type, row) in enumerate(top3_agent_types.iterrows(), 1):
        print(f"{i}. {agent_type}: {row['multimodal_ratio']}% ({row['multimodal_count']}/{row['total_count']})")
    
    print("\nQuestion 2 - Top 3 Model Architectures by Multimodal Support:")
    for i, (arch, row) in enumerate(top3_model_architectures.iterrows(), 1):
        print(f"{i}. {arch}: {row['multimodal_ratio']}% ({row['multimodal_count']}/{row['total_count']})")
        
    print("\nQuestion 3 - Top 3 Task Categories by Bias Detection Median:")
    for i, (task, median) in enumerate(task_bias_median.items(), 1):
        print(f"{i}. {task}: {median:.2f}")
    
    return results

if __name__ == "__main__":
    results = analyze_data()