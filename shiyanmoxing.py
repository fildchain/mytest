import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

class GradePredictionModel:
    def __init__(self):
        self.models = {}
        self.model_performance = {}
        self.best_model = None
        self.feature_names = []
        
    def load_and_preprocess_data(self, file_path):
        """加载和预处理数据"""
        try:
            # 读取数据
            df = pd.read_csv(file_path)
            print(f"数据加载成功，共 {len(df)} 条记录")
            
            # 显示数据基本信息
            print("\n数据基本信息:")
            print(f"列名: {df.columns.tolist()}")
            print(f"数据类型:\n{df.dtypes}")
            print(f"\n数据前5行:\n{df.head()}")
            
            # 数据清洗
            df_clean = df.copy()
            
            # 重命名列以统一格式
            column_mapping = {
                '每周学习时': 'weekly_study_hours',
                '期中考试分': 'midterm_score', 
                '上课出勤率': 'attendance_rate',
                '作业完成率': 'homework_completion_rate',
                '期末考试分数': 'final_score'
            }
            
            for old_col, new_col in column_mapping.items():
                if old_col in df_clean.columns:
                    df_clean = df_clean.rename(columns={old_col: new_col})
            
            # 处理缺失值
            numeric_columns = ['weekly_study_hours', 'attendance_rate', 'midterm_score', 
                             'homework_completion_rate', 'final_score']
            
            for col in numeric_columns:
                if col in df_clean.columns:
                    # 填充缺失值
                    if df_clean[col].isnull().sum() > 0:
                        df_clean[col] = df_clean[col].fillna(df_clean[col].mean())
                        print(f"填充 {col} 的 {df_clean[col].isnull().sum()} 个缺失值")
            
            # 特征工程
            df_processed = self.feature_engineering(df_clean)
            
            return df_processed
            
        except Exception as e:
            print(f"数据加载失败: {e}")
            return None
    
    def feature_engineering(self, df):
        """特征工程"""
        df_encoded = df.copy()
        
        # 1. 编码分类变量
        if '性别' in df_encoded.columns:
            df_encoded['性别'] = df_encoded['性别'].map({'男': 0, '女': 1})
        
        # 2. 专业one-hot编码
        if '专业' in df_encoded.columns:
            df_encoded = pd.get_dummies(df_encoded, columns=['专业'], prefix='专业')
        
        # 3. 创建交互特征
        if all(col in df_encoded.columns for col in ['weekly_study_hours', 'attendance_rate']):
            df_encoded['学习效率'] = df_encoded['weekly_study_hours'] * df_encoded['attendance_rate']
        
        if all(col in df_encoded.columns for col in ['midterm_score', 'homework_completion_rate']):
            df_encoded['平时表现'] = df_encoded['midterm_score'] * 0.6 + df_encoded['homework_completion_rate'] * 100 * 0.4
        
        # 4. 创建成绩等级特征
        if 'midterm_score' in df_encoded.columns:
            df_encoded['期中等级'] = pd.cut(df_encoded['midterm_score'], 
                                        bins=[0, 60, 70, 80, 90, 100],
                                        labels=[0, 1, 2, 3, 4])
        
        print(f"特征工程完成，最终特征数量: {len(df_encoded.columns)}")
        print(f"特征列表: {df_encoded.columns.tolist()}")
        
        return df_encoded
    
    def prepare_features(self, df):
        """准备特征和目标变量"""
        # 目标变量
        target = 'final_score'
        
        # 基础特征
        base_features = ['性别', 'weekly_study_hours', 'attendance_rate', 'midterm_score', 'homework_completion_rate']
        
        # 选择存在的特征
        existing_features = [f for f in base_features if f in df.columns]
        
        # 添加专业特征
        major_features = [col for col in df.columns if col.startswith('专业_')]
        
        # 添加工程特征
        engineered_features = [col for col in df.columns if col in ['学习效率', '平时表现', '期中等级']]
        
        # 最终特征列表
        all_features = existing_features + major_features + engineered_features
        
        X = df[all_features]
        y = df[target]
        
        self.feature_names = all_features
        
        print(f"特征准备完成:")
        print(f"- 基础特征: {existing_features}")
        print(f"- 专业特征: {len(major_features)} 个")
        print(f"- 工程特征: {engineered_features}")
        print(f"- 总特征数: {len(all_features)}")
        print(f"- 目标变量: {target}")
        
        return X, y
    
    def train_models(self, X, y):
        """训练多个模型并比较性能"""
        # 分割数据
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        print(f"\n数据分割:")
        print(f"- 训练集: {X_train.shape[0]} 样本")
        print(f"- 测试集: {X_test.shape[0]} 样本")
        
        # 定义模型
        models = {
            'RandomForest': RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10),
            'LinearRegression': LinearRegression(),
            'SVR': SVR(kernel='rbf', C=1.0)
        }
        
        # 训练并评估每个模型
        best_score = -np.inf
        self.best_model = None
        
        for name, model in models.items():
            print(f"\n训练 {name}...")
            
            try:
                # 训练模型
                model.fit(X_train, y_train)
                
                # 预测
                y_pred = model.predict(X_test)
                
                # 评估指标
                mae = mean_absolute_error(y_test, y_pred)
                mse = mean_squared_error(y_test, y_pred)
                rmse = np.sqrt(mse)
                r2 = r2_score(y_test, y_pred)
                
                # 存储模型和性能
                self.models[name] = model
                self.model_performance[name] = {
                    'MAE': mae,
                    'MSE': mse,
                    'RMSE': rmse,
                    'R2': r2
                }
                
                print(f"{name} 性能:")
                print(f"- MAE: {mae:.2f}")
                print(f"- RMSE: {rmse:.2f}")
                print(f"- R2: {r2:.4f}")
                
                # 更新最佳模型
                if r2 > best_score:
                    best_score = r2
                    self.best_model = name
                    
            except Exception as e:
                print(f"训练 {name} 时出错: {e}")
        
        if self.best_model:
            print(f"\n最佳模型: {self.best_model} (R2: {best_score:.4f})")
        else:
            print("\n所有模型训练失败")
    
    def evaluate_models(self):
        """模型评估和可视化"""
        if not self.model_performance:
            print("没有训练好的模型可供评估")
            return
        
        # 创建性能比较表格
        performance_df = pd.DataFrame(self.model_performance).T
        print("\n模型性能比较:")
        print(performance_df.round(4))
        
        # 可视化比较
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # MAE比较
        performance_df['MAE'].plot(kind='bar', ax=axes[0,0], color='skyblue')
        axes[0,0].set_title('平均绝对误差 (MAE)')
        axes[0,0].set_ylabel('MAE')
        
        # RMSE比较
        performance_df['RMSE'].plot(kind='bar', ax=axes[0,1], color='lightcoral')
        axes[0,1].set_title('均方根误差 (RMSE)')
        axes[0,1].set_ylabel('RMSE')
        
        # R2比较
        performance_df['R2'].plot(kind='bar', ax=axes[1,0], color='lightgreen')
        axes[1,0].set_title('决定系数 (R²)')
        axes[1,0].set_ylabel('R²')
        axes[1,0].set_ylim(0, 1)
        
        # 特征重要性（仅随机森林）
        if 'RandomForest' in self.models:
            rf_model = self.models['RandomForest']
            feature_importance = pd.DataFrame({
                'feature': self.feature_names,
                'importance': rf_model.feature_importances_
            }).sort_values('importance', ascending=False)
            
            feature_importance.head(10).plot(kind='barh', x='feature', y='importance', 
                                           ax=axes[1,1], color='orange')
            axes[1,1].set_title('随机森林特征重要性 (Top 10)')
        
        plt.tight_layout()
        plt.savefig('model_performance.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def save_model(self, file_path='grade_prediction_model.pkl'):
        """保存最佳模型"""
        if self.best_model and self.best_model in self.models:
            model_to_save = {
                'model': self.models[self.best_model],
                'feature_names': self.feature_names,
                'performance': self.model_performance[self.best_model],
                'model_name': self.best_model
            }
            
            joblib.dump(model_to_save, file_path)
            print(f"\n模型已保存到: {file_path}")
            print(f"保存的模型: {self.best_model}")
            print(f"模型性能: R2 = {self.model_performance[self.best_model]['R2']:.4f}")
            
            # 保存特征列表
            feature_info = {
                'feature_names': self.feature_names,
                'required_features': ['性别', 'weekly_study_hours', 'attendance_rate', 'midterm_score', 'homework_completion_rate']
            }
            joblib.dump(feature_info, 'feature_info.pkl')
            print("特征信息已保存到: feature_info.pkl")
            
        else:
            print("没有可保存的模型")
    
    def predict_single(self, input_data):
        """单个样本预测"""
        if not self.best_model or self.best_model not in self.models:
            print("请先训练模型")
            return None
        
        model = self.models[self.best_model]
        
        # 确保输入数据格式正确
        if isinstance(input_data, dict):
            # 创建DataFrame
            input_df = pd.DataFrame([input_data])
            
            # 确保所有特征都存在
            for feature in self.feature_names:
                if feature not in input_df.columns:
                    input_df[feature] = 0  # 默认值
            
            # 重新排序列以匹配训练时的顺序
            input_df = input_df[self.feature_names]
        else:
            input_df = input_data
        
        # 预测
        prediction = model.predict(input_df)[0]
        
        return prediction
    
    def create_prediction_template(self):
        """创建预测模板"""
        template = {
            '性别': 0,  # 0:男, 1:女
            'weekly_study_hours': 20.0,
            'attendance_rate': 0.85,
            'midterm_score': 75.0,
            'homework_completion_rate': 0.8
        }
        
        # 添加专业特征
        major_features = [col for col in self.feature_names if col.startswith('专业_')]
        for major_feature in major_features:
            template[major_feature] = 0
        
        return template

def main():
    """主函数"""
    print("=" * 50)
    print("学生期末成绩预测模型训练")
    print("=" * 50)
    
    # 初始化模型
    predictor = GradePredictionModel()
    
    # 加载数据
    file_path = 'student_data_adjusted_rounded.csv'
    df = predictor.load_and_preprocess_data(file_path)
    
    if df is None:
        print("数据加载失败，程序退出")
        return
    
    # 准备特征
    X, y = predictor.prepare_features(df)
    
    # 训练模型
    predictor.train_models(X, y)
    
    # 评估模型
    predictor.evaluate_models()
    
    # 保存模型
    predictor.save_model()

   
if __name__ == "__main__":
    main()
