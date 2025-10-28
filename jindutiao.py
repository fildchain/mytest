import streamlit as st
import time

st.header("进度条示例")
# 设置初始状态
progress_text_1 = "程序正在处理中，请稍等"
my_bar = st.progress(0, text=progress_text_1)
time.sleep(0.5)

# 第一个过程，时间间隔为0.1秒，进度较慢
for percent in range(80):
    time.sleep(0.1)
    my_bar.progress(percent + 1, text=f'{progress_text_1}，当前进度{percent}%:hourglass:')

# 第二个过程，时间间隔为0.05秒，进度较快
for percent in range(80,100):
    time.sleep(0.05)
    my_bar.progress(percent + 1, text=f'程序马上就要完成了，当前进度{percent}%:laughing:')



st.title("旋转等待组件")
with st.spinner('请耐心等待:hourglass:'):
    time.sleep(5)
st.write("感谢你的耐心等待，任务已完成！")



st.title("错误信息框")
# 不可以使用表情符号短代码
st.error('程序运行出错了', icon="🚨")
st.error('程序运行又出错了')

# 捕捉零作为除数的异常
try:
    div = 1/0
except ZeroDivisionError as e:
   st.error(e)

# 捕捉自定义抛出的异常
try:
    raise Exception("程序错了，这是一个自定义的异常")
except Exception as e:
   st.error(e)

st.title("警告信息框")
# 不可以使用表情符号短代码
st.warning('程序出现问题，可能导致程序错误，请注意', icon="⚠")
st.warning('程序又出现问题，可能导致程序错误，请注意')

st.title("提示信息框")
# 不可以使用表情符号短代码
st.info('这是一个带有图标提示信息框', icon="🤖")
st.info('这也是一个提示信息框')

st.title("成功信息框")
# 不可以使用表情符号短代码
st.success('这是一个带有图标的成功信息框', icon="✅")
st.success('这也是一个成功信息框')

st.header("错误信息框")
# 捕捉零作为除数的异常
try:
    div = 1/0
except ZeroDivisionError as e:
   st.error(e)

st.header("异常信息框")

# 捕捉零作为除数的异常
try:
    div = 1/0
except ZeroDivisionError as e:
   st.exception(e)
