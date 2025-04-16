import streamlit as st

st.set_page_config(page_title='리딩지저스', page_icon='📖', initial_sidebar_state='collapsed')
# st.title('리딩지저스')

# initialize session_state
if 'date' not in st.session_state:
    # get today date (yyyy-mm-dd)
    # tz = timezone('Asia/Seoul')
    from datetime import datetime
    from pytz import timezone
    tz = timezone('Asia/Seoul')
    st.session_state['date'] = datetime.now(tz=tz)
if 'url_list' not in st.session_state:
    import pandas as pd
    st.session_state['url_list'] = pd.read_csv('url_list.csv')
if 'url_list2' not in st.session_state:
    import pandas as pd
    st.session_state['url_list2'] = pd.read_csv('url_list2.csv')
date = st.session_state['date'].strftime('%Y-%m-%d')


# sidebar 
# st.sidebar.title('일정표')

# event = st.sidebar.dataframe(
#     st.session_state['url_list'][['title', 'date']].rename(columns={'title': '제목', 'date': '날짜'}).set_index('날짜'),
#     on_select='rerun',
#     selection_mode='single-row',
# )
# if len(event.selection['rows']) > 0:
#     selected_date = datetime.strptime(st.session_state['url_list'].iloc[event.selection['rows'][0]]['date'], '%Y-%m-%d')
#     st.session_state['date'] = selected_date

# title
st.markdown("<h1 style='text-align: center;'>&nbsp;&nbsp;&nbsp;리딩지저스</h1>", unsafe_allow_html=True) 

# if st.button('< Go to today >', type='tertiary', use_container_width=True):
#     st.session_state['date'] = datetime.now()
#     print(st.session_state['selected'])
#     st.session_state['selected'] = datetime.now().strftime('%Y-%m-%d')
#     st.rerun()
# date select
# input = st.date_input('날짜', st.session_state['date'])
# if input:
#     st.session_state['date'] = input
A = st.session_state['url_list']['date'].to_list()
B = st.session_state['url_list']['title'].to_list()
def get_date_selection(date):
    title = st.session_state['url_list'][st.session_state['url_list']['date'] == date]['title'].values[0]
    return f'{date} | {title}'
    
C = [f'{a} | {b}' for a, b in zip(A, B)]
selected_date = st.selectbox('날짜', A, key='selected', format_func=get_date_selection, index=A.index(date) if date in A else None, placeholder=date, label_visibility='collapsed')
if selected_date:
    date = selected_date.split(' | ')[0]

# progress
today_data = st.session_state['url_list'][st.session_state['url_list']['date'] == date]
if len(today_data) > 0 and all(today_data.notna()):
    st.progress(today_data.index[0] / len(st.session_state['url_list']), f'📖 {round(today_data.index[0] / len(st.session_state['url_list'])*100, 1)}%')

# get today data from st.session_state['url_list']
today_data = st.session_state['url_list'][st.session_state['url_list']['date'] == date]
if len(today_data) > 0 and all(today_data.notna()):
    data = today_data.to_dict('records')[0]
    volume = int(data["volume"])
    chapter = int(data["chapter"])
    day = int(data["day"])
    # st.write(data)
    list2 = st.session_state['url_list2']
    list2 = list2[list2['volume'] == volume]
    list2 = list2[list2['chapter'] == chapter]
    data2 = list2.to_dict('records')[0]
# st.divider()
# st.subheader(data['title'])

    # status
    if day != 0:
        st.caption(f'{volume}권 {chapter}강 {day}일차')
    else:
        st.caption(f'{volume}권 {chapter}강')

    # summary
    with st.expander('**본문해설**', expanded=True):
        st.image(f'Summary/{volume}권 성경읽기/{volume}권{chapter}강/{volume}권{chapter}강_성경읽기_{day}.jpg')
    
    # video
    with st.expander('**본문영상**', expanded=True):
        st.video(data['url'])
    
    # chapter video
    with st.expander('**챕터영상**', expanded=True):
        st.video(data2['url'])