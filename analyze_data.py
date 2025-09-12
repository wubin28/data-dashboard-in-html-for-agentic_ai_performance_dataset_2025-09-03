import pandas as pd
import numpy as np
import json

# Read the Excel file - skip the first row and use second row as header
df = pd.read_excel('first-80-rows-agentic_ai_performance_dataset_20250622.xlsx', skiprows=1)

print("Dataset shape:", df.shape)
print(f"Total records processed: {len(df)}")

# Check the key columns we need
key_columns = ['agent_type', 'multimodal_capability', 'model_architecture', 'task_category', 'bias_detection_score']
print(f"\nKey columns present: {[col for col in key_columns if col in df.columns]}")

# Display unique values for key columns
print(f"\nUnique agent types: {sorted(df['agent_type'].unique())}")
print(f"\nUnique model architectures: {sorted(df['model_architecture'].unique())}")
print(f"\nUnique task categories: {sorted(df['task_category'].unique())}")

# Check data types and sample values for key columns
print(f"\nMultimodal capability sample values: {df['multimodal_capability'].unique()}")
print(f"Bias detection score sample values: {df['bias_detection_score'].unique()}")

# Calculate statistics for the three questions
print("\n" + "="*60)
print("ANALYSIS RESULTS")
print("="*60)

# Question 1: Top 3 agent types by multimodal capability ratio
print("\n1. Top 3 agent types by multimodal capability ratio:")
# Convert multimodal_capability to binary (assuming 1/0 or True/False)
df['multimodal_binary'] = df['multimodal_capability'].astype(int)
multimodal_by_agent = df.groupby('agent_type')['multimodal_binary'].agg(['sum', 'count'])
multimodal_by_agent['ratio'] = multimodal_by_agent['sum'] / multimodal_by_agent['count']
multimodal_by_agent = multimodal_by_agent.sort_values('ratio', ascending=False)
print("All agent types ranked by multimodal ratio:")
print(multimodal_by_agent)
top_3_agents = multimodal_by_agent.head(3)
print(f"\nTop 3 agent types:")
for i, (agent, row) in enumerate(top_3_agents.iterrows(), 1):
    print(f"{i}. {agent}: {row['ratio']:.3f} ({row['sum']}/{row['count']} agents)")

# Question 2: Top 3 model architectures by multimodal capability ratio  
print("\n2. Top 3 model architectures by multimodal capability ratio:")
multimodal_by_arch = df.groupby('model_architecture')['multimodal_binary'].agg(['sum', 'count'])
multimodal_by_arch['ratio'] = multimodal_by_arch['sum'] / multimodal_by_arch['count']
multimodal_by_arch = multimodal_by_arch.sort_values('ratio', ascending=False)
print("All model architectures ranked by multimodal ratio:")
print(multimodal_by_arch)
top_3_archs = multimodal_by_arch.head(3)
print(f"\nTop 3 model architectures:")
for i, (arch, row) in enumerate(top_3_archs.iterrows(), 1):
    print(f"{i}. {arch}: {row['ratio']:.3f} ({row['sum']}/{row['count']} models)")

# Question 3: Top 3 task categories by bias detection median (higher is better)
print("\n3. Top 3 task categories by bias detection median (higher = more fair):")
bias_by_task = df.groupby('task_category')['bias_detection_score'].agg(['median', 'mean', 'count'])
bias_by_task = bias_by_task.sort_values('median', ascending=False)
print("All task categories ranked by bias detection median:")
print(bias_by_task)
top_3_tasks = bias_by_task.head(3)
print(f"\nTop 3 task categories by bias detection median:")
for i, (task, row) in enumerate(top_3_tasks.iterrows(), 1):
    print(f"{i}. {task}: {row['median']:.3f} median score")

# Save results for HTML generation
results = {
    'total_records': len(df),
    'top_agents': {agent: float(row['ratio']) for agent, row in top_3_agents.iterrows()},
    'top_architectures': {arch: float(row['ratio']) for arch, row in top_3_archs.iterrows()},
    'top_tasks': {task: float(row['median']) for task, row in top_3_tasks.iterrows()}
}

with open('analysis_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nResults saved to analysis_results.json")
print(f"\nSummary:")
print(f"- Total records processed: {len(df)}")
print(f"- Top agent type: {list(results['top_agents'].keys())[0]} ({list(results['top_agents'].values())[0]:.3f})")
print(f"- Top architecture: {list(results['top_architectures'].keys())[0]} ({list(results['top_architectures'].values())[0]:.3f})")
print(f"- Top task category: {list(results['top_tasks'].keys())[0]} ({list(results['top_tasks'].values())[0]:.3f})")