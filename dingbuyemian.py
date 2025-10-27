import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title="多页面顶部",page_icon="📝", layout="wide")

st.image("D:\streamlit_env\顶部.png")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["数字档案", "南宁美食数据", "相册","音乐播放器","视频网站","个人简历"])


with tab1:
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
    

with tab2:
    st.title("南宁美食🍛")
    st.header("南宁美食地图🍰",help='详细内容')

    map_data={
    'latitude':[23.096832,22.798278,22.817690,22.847565,23.156355],
    'longitude':[108.301585,108.337854,108.321063,108.268926,108.237124],
    }
    st.map(pd.DataFrame(map_data))

    data = {
    '永盛粉店🍜':[200, 150, 180,120,145,125,133,178,165,188,179,135],
    '舒记粉店(桃源店)🥢':[120, 160, 123,165,189,124,125,145,123,156,158,158],
    '味芙恬蛋糕店🍨':[110, 100, 160,120,130,164,157,159,211,230,146,145],
    '水果天空(七星店)🍇':[200, 210, 215,195,189,178,189,186,185,145,165,145],
    '麦当劳(南宁北站店)🥞':[300, 256, 250,145,155,233,146,146,198,168,250,146]
}

    df = pd.DataFrame(data)
# 定义数据框所用的新索引
    index = pd.Series(['01月','02月', '03月','04月','05月','06月','07月','08月','09月','10月','11月','12月'], name='月份')
# 将新索引应用到数据框上
    df.index = index

    st.header("门店数据")
#展示数据
    st.table(df)
#柱形图
    st.line_chart(df)
#柱形图
    st.bar_chart(df)
#面积图
    st.area_chart(df)
   

with tab3:
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

with tab4:
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
