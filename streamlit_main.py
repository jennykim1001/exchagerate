import streamlit as st
from PIL import Image
import exchange

# 사이드바 화면
st.sidebar.header("로그인")
user_id = st.sidebar.text_input('아이디(ID) 입력', value="streamlit", max_chars=15)
user_password = st.sidebar.text_input('패스워드(Password) 입력', value="", type="password")

if user_password == '1234':

    st.sidebar.header("그림 목록")
    selectbox_options = ['환율조회', '데이터분석'] # 셀렉트 박스의 선택 항목
    your_option = st.sidebar.selectbox('메뉴선택', selectbox_options, index=0) # 셀렉트박스의 항목 선택 결과
    st.sidebar.write(your_option)

    # 메인(Main) 화면
    st.subheader('heeya workspace', divider='rainbow')

    if your_option=='환율조회':
        # pass
        exchange.exchange_main()
    else:
        pass
    