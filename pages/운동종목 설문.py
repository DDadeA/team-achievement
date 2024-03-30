import streamlit as st

st.title("당신이 한 운동은?")

st.button("유산소 운동")
st.button("근력 운동")
st.button("기타")
st.button("설문 제출")

def go_to_매인화면():
    st.write("모든 설문이 완료되었습니다. 매인 화면으로 이동합니다.")
if button("설문 제출"):
    go_to_매인화면()