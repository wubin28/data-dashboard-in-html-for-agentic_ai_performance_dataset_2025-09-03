import pandas as pd
import json
import sys

# 设置UTF-8编码
sys.stdout.reconfigure(encoding='utf-8')

# 读取Excel文件，使用第一行作为列名
df = pd.read_excel('first-80-rows-agentic_ai_performance_dataset_20250622.xlsx', skiprows=1)

print(f"实际处理的数据行数: {len(df)}")

# 1. 分析支持多模态处理的智能体类型占比排名
def analyze_multimodal_agent_types():
    # 筛选出支持多模态的智能体
    multimodal_agents = df[df['multimodal_capability'] == True]

    # 计算每种智能体类型的占比
    agent_type_counts = df['agent_type'].value_counts()
    multimodal_agent_type_counts = multimodal_agents['agent_type'].value_counts()

    # 计算占比
    agent_type_ratios = {}
    for agent_type in agent_type_counts.index:
        if agent_type in multimodal_agent_type_counts.index:
            ratio = multimodal_agent_type_counts[agent_type] / agent_type_counts[agent_type]
            agent_type_ratios[agent_type] = ratio
        else:
            agent_type_ratios[agent_type] = 0

    # 排序并取前三
    top_3_agent_types = sorted(agent_type_ratios.items(), key=lambda x: x[1], reverse=True)[:3]

    print("\n=== 多模态智能体类型占比排名前三 ===")
    for i, (agent_type, ratio) in enumerate(top_3_agent_types, 1):
        print(f"{i}. {agent_type}: {ratio:.2%}")

    return top_3_agent_types

# 2. 分析支持多模态处理的大模型架构占比排名
def analyze_multimodal_architectures():
    # 筛选出支持多模态的智能体
    multimodal_agents = df[df['multimodal_capability'] == True]

    # 计算每种架构的占比
    architecture_counts = df['model_architecture'].value_counts()
    multimodal_architecture_counts = multimodal_agents['model_architecture'].value_counts()

    # 计算占比
    architecture_ratios = {}
    for architecture in architecture_counts.index:
        if architecture in multimodal_architecture_counts.index:
            ratio = multimodal_architecture_counts[architecture] / architecture_counts[architecture]
            architecture_ratios[architecture] = ratio
        else:
            architecture_ratios[architecture] = 0

    # 排序并取前三
    top_3_architectures = sorted(architecture_ratios.items(), key=lambda x: x[1], reverse=True)[:3]

    print("\n=== 多模态大模型架构占比排名前三 ===")
    for i, (architecture, ratio) in enumerate(top_3_architectures, 1):
        print(f"{i}. {architecture}: {ratio:.2%}")

    return top_3_architectures

# 3. 分析各种任务类别的公正性中位数排名
def analyze_task_category_fairness():
    # 按任务类别分组，计算公正性中位数
    task_fairness = df.groupby('task_category')['bias_detection_score'].median().sort_values(ascending=False)

    print("\n=== 任务类别公正性中位数排名前三 ===")
    for i, (task_category, median_score) in enumerate(task_fairness.head(3).items(), 1):
        print(f"{i}. {task_category}: {median_score:.2f}")

    return task_fairness.head(3).to_dict()

# 执行分析
top_agent_types = analyze_multimodal_agent_types()
top_architectures = analyze_multimodal_architectures()
top_task_fairness = analyze_task_category_fairness()

# 生成HTML看板数据
dashboard_data = {
    "total_records": len(df),
    "multimodal_agent_types": top_agent_types,
    "multimodal_architectures": top_architectures,
    "task_fairness": top_task_fairness
}

# 保存数据为JSON
with open('dashboard_data.json', 'w', encoding='utf-8') as f:
    json.dump(dashboard_data, f, ensure_ascii=False, indent=2)

print(f"\n分析完成！数据已保存到 dashboard_data.json")