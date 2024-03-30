import streamlit as st

st.title("당신의 나이는?")

st.selectbox("나이",["만13세~만14세", "만14세~만15세", "만15세~만16세", "만17세~만18세", "만18세~만 19세"])

next_button = st.button("다음 페이지")

def go_to_운동종목설문():
    st.switch_page("pages/운동종목 설문.py")
if next_button:
    go_to_운동종목설문()