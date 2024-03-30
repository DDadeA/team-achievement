import streamlit as st

st.title("당신의 성별은?")

st.selectbox("성별", ["남자", "여자"])

next_button = st.button("다음 페이지")

def go_to_나이설문():
    st.write("이제 나이에 대한 설문으로 이동합니다")
    st.switch_page("pages/나이 설문.py")

if next_button:
    go_to_나이설문()