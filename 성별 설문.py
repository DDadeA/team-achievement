import streamlit as st

st.title("당신의 성별은?")

st.button("남자")
st.button("여자")
st.button("다음 페이지")

def go_to_나이설문():
    st.write("이제 나이에 대한 설문으로 이동합니다")
if st.button("다음 페이지"):
    go_to_나이설문()