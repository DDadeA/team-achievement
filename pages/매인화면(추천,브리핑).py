import streamlit as st

st.title("오늘의 추천")
st.header("오늘의 운동 브리핑")
st.header("오늘의 운동 추천")
prize_button = st.button("보상")

def go_to_보상():
    st.switch_page("pages/보상.py")
if prize_button:
    go_to_보상()