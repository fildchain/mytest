import streamlit as st

st.set_page_config(page_title='动物园', page_icon='🐒')

#展示多张图片
images=[
    {
        'url':'https://cdn.pixabay.com/photo/2013/05/17/15/54/cat-111793_1280.jpg',
        'parm':'猫'
    },
    {
        'url': 'https://wallup.net/wp-content/uploads/2018/10/06/520307-pomeranian-dog-dogs.jpg',
        'parm':'狗'

    },
    {
        'url':  'https://birdwatchinghq.com/wp-content/uploads/2021/10/bluebird-featured-image-scaled.jpg',
        'parm':'鸟'

    }
]
#将ind的值存储到streamlit的内存中，如果内存中没有ind,才要设置成0，否则不需要设置
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

    
#define:定义
def nextImg():
    st.session_state['ind'] =(st.session_state['ind'] + 1) % len(images)
def prevImg():
    st.session_state['ind'] =(st.session_state['ind'] - 1) % len(images)

#st.image()总共两个参数，url图片地址 caption:图片备注
st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])


#将1行分成2列
c1,c2 =st.columns(2)

with c1:
#st.button()按钮，test:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('上一张',on_click=prevImg, use_container_width=True)
with c2:
#st.button()按钮，test:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('下一张',on_click=nextImg,use_container_width=True)   



 
