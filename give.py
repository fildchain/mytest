import streamlit as st
import pandas as pd
st.title("学生 小白-数字档案")
st.header('**🥥基础信息**')
st.markdown('**🥥信息**')
st.markdown(':red[学生ID：NEO33550336]')
st.text('''
注册时间：2025.7.12 12:00 精神状态：✅正常
当前教室：实训楼204 安全等级：高
''')


st.header("🥥技能矩阵")
st.metric(label="当日收入", value="4500", delta="100")
st.subheader('技能')
c1, c2, c3 = st.columns(3)
c1.metric(label="Python", value="87%", delta="30%")
c2.metric(label="C语音", value="76%", delta="6%")
c3.metric(label="Java", value="92%", delta="10%")

st.header("🏷️任务日志",help='详细任务内容')

data = {
    '日期':["2023-10-01", "2023-10-05"," 2023-10-12"],
    '任务':["学生数字档案", "课程管理系统", "数字图表展示"],
    '状态':["✅完成","⏲进行中","❌未完成"],
    '难度':["⭐⭐","⭐","⭐⭐⭐"],
}

# 定义数据框所用的索引
index = pd.Series(['0', '1', '2'], name='  ')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)

st.subheader('任务表')
st.table(df)





