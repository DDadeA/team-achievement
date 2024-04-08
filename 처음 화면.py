import streamlit as st

def go_to_survey():
    st.write("설문 페이지로 이동합니다.")

st.title("안녕하세요, TA Health Care에 오신 것을 환영합니다!")

skip_button = st.button("skip")
next_button = st.button("설문")


def go_to_성별설문():
    st.switch_page("pages/성별 설문.py")


if next_button:
    go_to_성별설문()


def go_to_매인화면():
    st.switch_page("pages/매인화면(추천, 브리핑).py")
if skip_button:
    go_to_매인화면()
    
