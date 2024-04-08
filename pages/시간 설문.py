import streamlit as st

st.title("당신이 오늘 운동한 시간은?")
st.number_input("당신이 오늘 운동한 시간을 입력하세요",value=None, placeholder="시간를 입력하세요...")
next_button = st.button("설문 제출")

def go_to_매인화면():
    st.switch_page("pages/매인 화면.py")
if next_button:
    go_to_매인화면()