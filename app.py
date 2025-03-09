import streamlit as st

st.title('리딩지저스')

# read 'url_list.csv'
import pandas as pd
url_list = pd.read_csv('url_list.csv')

# get today date (yyyy-mm-dd)
import datetime
today = datetime.datetime.now() + datetime.timedelta(days=1)
today = today.strftime('%Y-%m-%d')

# get today data from url_list
today_data = url_list[url_list['date'] == today].to_dict('records')[0]
# st.write(today_data)

# display today data (title, )
st.subheader(today_data['title'])
st.caption(f'{today_data["volume"]}권 {today_data["chapter"]}강 {today_data["day"]}일차')

# display today data (youtube)
st.video(today_data['url'])

# sidebar
st.sidebar.title('진행표')
# st.sidebar.table(st.dataframe())