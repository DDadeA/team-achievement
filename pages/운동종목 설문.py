import streamlit as st

st.title("당신이 한 운동은?")
st.selectbox("운동종목", ["유산소운동", "근력운동", "기타" ])

next_button = st.button("설문 제출")

def go_to_매인화면():
    st.switch_page("pages/매인화면(추천,브리핑).py")
if next_button:
    go_to_매인화면()