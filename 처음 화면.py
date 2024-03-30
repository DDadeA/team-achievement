import streamlit as st

def go_to_survey():
    st.write("설문 페이지로 이동합니다.")

st.title("안녕하세요!")

next_button = st.button("설문 시작")

def go_to_성별설문():
    st.switch_page("pages/성별 설문.py")
if next_button:
    go_to_성별설문()
