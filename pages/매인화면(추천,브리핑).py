import streamlit as st

st.tittle("오늘의 추천")
st.header("오늘의 운동 브리핑")
st.header("오늘의 운동 추천")
st.button("보상")

def go_to_보상():
    st.write("보상으로 이동합니다.")
if st.button("보상"):
    go_to_보상()