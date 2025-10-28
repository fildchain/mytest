import streamlit as st

st.title("停止执行示例")
# 将单行文本的值赋值给name变量
name = st.text_input('你的姓名：')
# 判断name变量是否为空
if not name:
    # 如果用户未输入姓名，name变量为空字符串，not name的值将为True
    # 警告用户需要输入姓名
    st.warning('请输入姓名！')
    # 停止执行
    st.stop()
# name不是空字符串，用成功信息框提示用户
st.success('非常感谢！你按要求输入了姓名')

st.title("提交表单示例")
with st.form("my_form"):
   st.write("这是在表单内")
   slider_val = st.slider("表单内的数值滑块组件")
   checkbox_val = st.checkbox("表单内的勾选按钮")

   # 注意：每个表单内都需要有一个表单提交按钮
   submitted = st.form_submit_button("提交")
   if submitted:
       st.write("数值滑块组件的值", slider_val, "勾选按钮的值", checkbox_val)

st.write("这个不在表单内")
