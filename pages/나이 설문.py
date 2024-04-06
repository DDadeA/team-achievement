import streamlit as st

st.title("당신의 나이는?")
st.number_input("당신의 나이를 입력하세요",value=None, placeholder="나이를 입력하세요...")
next_button = st.button("다음 페이지")

def go_to_운동종목설문():
    st.switch_page("pages/운동종목 설문.py")
if next_button:
    go_to_운동종목설문()