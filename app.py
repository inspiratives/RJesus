import streamlit as st

st.set_page_config(page_title='리딩지저스', page_icon='📖', initial_sidebar_state='collapsed')
# st.title('리딩지저스')

# read 'url_list.csv'
import pandas as pd
url_list = pd.read_csv('url_list.csv')

if 'date' not in st.session_state:
    # get today date (yyyy-mm-dd)
    import datetime
    st.session_state['date'] = datetime.datetime.now()
date = st.session_state['date'].strftime('%Y-%m-%d')

# progress
today_data = url_list[url_list['date'] == date]
if len(today_data) > 0 and all(today_data.notna()):
    st.progress(today_data.index[0] / len(url_list), f'📖 {round(today_data.index[0] / len(url_list)*100, 1)}%')

# title
st.markdown("<h1 style='text-align: center;'>&nbsp;&nbsp;&nbsp;리딩지저스</h1>", unsafe_allow_html=True) 

# date select
input = st.date_input('날짜', 'today', key='date')

# get today data from url_list
today_data = url_list[url_list['date'] == date]
if len(today_data) > 0 and all(today_data.notna()):
    data = today_data.to_dict('records')[0]
    volume = int(data["volume"])
    chapter = int(data["chapter"])
    day = int(data["day"])
    # st.write(data)
# st.divider()
# st.subheader(data['title'])

    # status
    if day != 0:
        st.caption(f'{volume}권 {chapter}강 {day}일차')
    else:
        st.caption(f'{volume}권 {chapter}강')

    # summary
    if day != 0:
        with st.expander('**본문해설**', expanded=True):
            st.image(f'Summary/{volume}권 성경읽기/{volume}권 {chapter}강/{volume}권{chapter}강_성경읽기_{day}.jpg')
    
    # youtube
    st.video(data['url'])

# sidebar
# st.sidebar.title('진행표')
# st.sidebar.table(st.dataframe())