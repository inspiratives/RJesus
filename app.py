import streamlit as st

st.set_page_config(page_title='리딩지저스', page_icon='📖', initial_sidebar_state='collapsed')
# st.title('리딩지저스')

# read 'url_list.csv'
import pandas as pd
url_list = pd.read_csv('url_list.csv')

# get today date (yyyy-mm-dd)
import datetime
today = datetime.datetime.now() + datetime.timedelta(days=1)
today = today.strftime('%Y-%m-%d')

# get today data from url_list
today_data = url_list[url_list['date'] == today]
data = url_list[url_list['date'] == today].to_dict('records')[0]
volume = int(data["volume"])
chapter = int(data["chapter"])
day = int(data["day"])
# st.write(data)

# display today data (title, )
st.progress(today_data.index[0] / len(url_list), f'📖 {round(today_data.index[0] / len(url_list)*100, 1)}%')
st.markdown("<h1 style='text-align: center;'>&nbsp;&nbsp;&nbsp;리딩지저스</h1>", unsafe_allow_html=True)
# st.divider()
# st.subheader(data['title'])
if day != 0:
    st.caption(f'{volume}권 {chapter}강 {day}일차')
else:
    st.caption(f'{volume}권 {chapter}강')

if day != 0:
    with st.expander('**본문해설**', expanded=True):
        st.image(f'Summary/{volume}권 성경읽기/{volume}권 {chapter}강/{volume}권{chapter}강_성경읽기_{day}.jpg')
    
# display today data (youtube)
st.video(data['url'])

# sidebar
# st.sidebar.title('진행표')
# st.sidebar.table(st.dataframe())