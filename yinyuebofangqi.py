import streamlit as st

st.title("🎼简易音乐播放器")
images=[
    {
        'url':"https://p2.music.126.net/SdToLdLtb5IEWUA0GCkKaw==/109951163336686938.jpg?param=180y180", caption='像小时候一样'
        'name':'像小时候一样'
        'author':'唐恬'
        'singer':'郁可唯'
        'audio':'https://music.163.com/song/media/outer/url?id=571894775.mp3'
    }
        ]

    

audio_file = 'https://music.163.com/song/media/outer/url?id=571894775.mp3'

st.audio(audio_file)

#将ind的值存储到streamlit的内存中，如果内存中没有ind,才要设置成0，否则不需要设置
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0
    
st.audio(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['name']['photo']['author']['singer'])

#define:定义
def nextImg():
    st.session_state['ind'] =(st.session_state['ind'] + 1) % len(images)
def prevImg():
    st.session_state['ind'] =(st.session_state['ind'] - 1) % len(images)

#st.image()总共两个参数，url图片地址 caption:图片备注
st.audio(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])


#将1行分成2列
c1,c2 =st.columns(2)

with c1:
#st.button()按钮，test:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('上一首',on_click=prevIsong, use_container_width=True)
with c2:
#st.button()按钮，test:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('下一首',on_click=nextsong,use_container_width=True)   

