import streamlit as st
st.set_page_config(page_title='视频', page_icon='📹')

st.title('视频播放')
#视频地址
video_url=[{
            'url':'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
            'title':'动画',
            'episode':'1'


    },
    {
            'url':'https://www.w3schools.com/html/movie.mp4',
            'title':'动物世界',
            'episode':'2'
           
    },
    {
        
            'url':'https://media.w3.org/2010/05/sintel/trailer.mp4',
            'title':'动漫',
            'episode':'3'
           
    }
]

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

    
st.title(video_url[st.session_state['ind']]['title'] + '-第' + video_url[st.session_state['ind']]['episode'] + '集')
st.video(video_url[st.session_state['ind']]['url'])

def play(arg):
    #点击哪个按钮就播放第几集
    #将传递过来的值赋值给内存中的ind
    st.session_state['ind'] = int(arg)

for i in range(len(video_url)):
    st.button('第'+str(i+1) +'集',on_click=play,use_container_width=True,args=([i]))



    
