import streamlit as st

st.title("당신이 한 운동은?")
st.selectbox("운동종목", ["유산소운동", "근력운동", "기타" ])
next_button = st.button("다음 페이지")

def go_to_시간설문():
    st.switch_page("pages/시간 설문.py")
if next_button:
    go_to_시간설문()