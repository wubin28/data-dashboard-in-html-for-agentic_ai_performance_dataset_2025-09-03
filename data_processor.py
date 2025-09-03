import pandas as pd
import numpy as np
import json
from typing import Dict, List, Tuple, Any

class AgenticAIDataProcessor:
    """Agentic AI Performance Dataset 数据处理器"""
    
    def __init__(self, excel_file_path: str):
        """
        初始化数据处理器
        
        Args:
            excel_file_path: Excel文件路径
        """
        self.excel_file_path = excel_file_path
        self.df = None
        self.processed_rows = 0
        
    def load_data(self) -> bool:
        """
        加载Excel数据
        
        Returns:
            bool: 加载是否成功
        """
        try:
            self.df = pd.read_excel(self.excel_file_path)
            self.processed_rows = len(self.df)
            print(f"成功加载数据，共 {self.processed_rows} 行")
            return True
        except Exception as e:
            print(f"数据加载失败: {e}")
            return False
    
    def get_data_overview(self) -> Dict[str, Any]:
        """
        获取数据概览信息
        
        Returns:
            Dict: 数据概览信息
        """
        if self.df is None:
            return {}
            
        return {
            "total_rows": self.processed_rows,
            "columns": list(self.df.columns),
            "multimodal_count": len(self.df[self.df['multimodal_capability'] == True]) if 'multimodal_capability' in self.df.columns else 0,
            "agent_types": self.df['agent_type'].nunique() if 'agent_type' in self.df.columns else 0,
            "model_architectures": self.df['model_architecture'].nunique() if 'model_architecture' in self.df.columns else 0,
            "task_categories": self.df['task_category'].nunique() if 'task_category' in self.df.columns else 0
        }
    
    def analyze_multimodal_agent_types(self) -> List[Tuple[str, float]]:
        """
        分析支持多模态处理的智能体类型占比排名前三
        
        Returns:
            List[Tuple[str, float]]: [(智能体类型, 占比), ...]
        """
        if self.df is None or 'multimodal_capability' not in self.df.columns or 'agent_type' not in self.df.columns:
            return []
        
        # 按智能体类型分组，计算每种类型中支持多模态的占比
        agent_type_stats = []
        
        for agent_type in self.df['agent_type'].unique():
            type_data = self.df[self.df['agent_type'] == agent_type]
            total_count = len(type_data)
            multimodal_count = len(type_data[type_data['multimodal_capability'] == True])
            
            if total_count > 0:
                ratio = multimodal_count / total_count
                agent_type_stats.append((agent_type, ratio))
        
        # 按占比降序排序，取前三
        agent_type_stats.sort(key=lambda x: x[1], reverse=True)
        return agent_type_stats[:3]
    
    def analyze_multimodal_model_architectures(self) -> List[Tuple[str, float]]:
        """
        分析支持多模态处理的大模型架构占比排名前三
        
        Returns:
            List[Tuple[str, float]]: [(大模型架构, 占比), ...]
        """
        if self.df is None or 'multimodal_capability' not in self.df.columns or 'model_architecture' not in self.df.columns:
            return []
        
        # 按大模型架构分组，计算每种架构中支持多模态的占比
        arch_stats = []
        
        for arch in self.df['model_architecture'].unique():
            arch_data = self.df[self.df['model_architecture'] == arch]
            total_count = len(arch_data)
            multimodal_count = len(arch_data[arch_data['multimodal_capability'] == True])
            
            if total_count > 0:
                ratio = multimodal_count / total_count
                arch_stats.append((arch, ratio))
        
        # 按占比降序排序，取前三
        arch_stats.sort(key=lambda x: x[1], reverse=True)
        return arch_stats[:3]
    
    def analyze_task_category_bias_median(self) -> List[Tuple[str, float]]:
        """
        分析各任务类别智能体公正性中位数排名前三
        
        Returns:
            List[Tuple[str, float]]: [(任务类别, 公正性中位数), ...]
        """
        if self.df is None or 'task_category' not in self.df.columns or 'bias_detection' not in self.df.columns:
            return []
        
        # 按任务类别分组，计算每种类别的公正性中位数
        category_bias_stats = []
        
        for category in self.df['task_category'].unique():
            category_data = self.df[self.df['task_category'] == category]
            bias_scores = category_data['bias_detection'].dropna()
            
            if len(bias_scores) > 0:
                median_bias = bias_scores.median()
                category_bias_stats.append((category, median_bias))
        
        # 按中位数降序排序，取前三
        category_bias_stats.sort(key=lambda x: x[1], reverse=True)
        return category_bias_stats[:3]
    
    def generate_analysis_results(self) -> Dict[str, Any]:
        """
        生成完整的分析结果
        
        Returns:
            Dict: 包含所有分析结果的字典
        """
        if not self.load_data():
            return {}
        
        results = {
            "data_overview": self.get_data_overview(),
            "multimodal_agent_types": self.analyze_multimodal_agent_types(),
            "multimodal_model_architectures": self.analyze_multimodal_model_architectures(),
            "task_category_bias_median": self.analyze_task_category_bias_median(),
            "processed_timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        return results
    
    def save_results_to_json(self, output_file: str = "analysis_results.json") -> bool:
        """
        保存分析结果到JSON文件
        
        Args:
            output_file: 输出文件名
            
        Returns:
            bool: 保存是否成功
        """
        try:
            results = self.generate_analysis_results()
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"分析结果已保存到 {output_file}")
            return True
        except Exception as e:
            print(f"保存结果失败: {e}")
            return False

def main():
    """主函数：执行数据分析"""
    # 初始化数据处理器
    processor = AgenticAIDataProcessor("first-80-rows-agentic_ai_performance_dataset_20250622.xlsx")
    
    # 生成分析结果
    results = processor.generate_analysis_results()
    
    if results:
        print("\n=== 数据分析结果 ===")
        print(f"处理数据行数: {results['data_overview']['total_rows']}")
        
        print("\n1. 支持多模态处理的智能体类型占比排名前三:")
        for i, (agent_type, ratio) in enumerate(results['multimodal_agent_types'], 1):
            print(f"   {i}. {agent_type}: {ratio:.2%}")
        
        print("\n2. 支持多模态处理的大模型架构占比排名前三:")
        for i, (arch, ratio) in enumerate(results['multimodal_model_architectures'], 1):
            print(f"   {i}. {arch}: {ratio:.2%}")
        
        print("\n3. 各任务类别智能体公正性中位数排名前三:")
        for i, (category, median) in enumerate(results['task_category_bias_median'], 1):
            print(f"   {i}. {category}: {median:.3f}")
        
        # 保存结果到JSON文件
        processor.save_results_to_json()
    else:
        print("数据分析失败，请检查Excel文件是否存在且格式正确")

if __name__ == "__main__":
    main()