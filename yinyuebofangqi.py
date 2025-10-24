import streamlit as st
st.set_page_config(page_title='音乐播放器', page_icon='🎹',)
st.title("🎼简易音乐播放器")
music=[
    {
        'url':'https://music.163.com/song/media/outer/url?id=571894775.mp3',
        'name':'像小时候一样',
        'author':'唐恬',
        'singer':'郁可唯',
        'photo':"https://p2.music.126.net/SdToLdLtb5IEWUA0GCkKaw==/109951163336686938.jpg?param=250y250"
    },
    {
        'url':'https://music.163.com/song/media/outer/url?id=1844441197.mp3',
        'name':'五四特别版错位时空',
        'author':'许诺',
        'singer':'共青团中央',
        'photo':'https://p2.music.126.net/pyfusPWvrFQbrhf2nP80Bg==/109951165972833054.jpg?param=250y250'
    },
    {
        'url':'https://music.163.com/song/media/outer/url?id=518725853.mp3',
        'name':'篝火旁',
        'author':'吕大叶/鳄鱼/马子林',
        'singer':'吕大叶/马子林',
        'photo':'https://p2.music.126.net/sN5dTpmeJO1DhxIj1ogMLg==/109951163416453597.jpg?param=250y250'
    }
]

#将ind的值存储到streamlit的内存中，如果内存中没有ind,才要设置成0，否则不需要设置
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0
    


#define:定义
def nextImg():
    st.session_state['ind'] =(st.session_state['ind'] + 1) % len(music)
def lastImg():
    st.session_state['ind'] =(st.session_state['ind'] - 1) % len(music)

#st.image()总共两个参数，url图片地址 caption:图片备注
a1, a2 = st.columns([1,2])
with a1:
    st.image(music[st.session_state['ind']]['photo'])
with a2:
    st.title(music[st.session_state['ind']]['name'])
    st.title(music[st.session_state['ind']]['author'])
    st.title(music[st.session_state['ind']]['singer'])
    st.audio(music[st.session_state['ind']]['url'],autoplay=True)
#将1行分成2列
c1,c2 =st.columns(2)

with c1:
#st.button()按钮，test:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('上一首',on_click=lastImg, use_container_width=True)
with c2:
#st.button()按钮，test:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('下一首',on_click=nextImg,use_container_width=True)   



