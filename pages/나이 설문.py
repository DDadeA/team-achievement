import streamlit as st

st.title("당신의 나이는?")

st.button("만13세~만14세")
st.button("만15세~만16세")
st.button("만17세~만19세")


def go_to_운동종목설문():
    st.write("이제 운동종목에 대한 설문으로 이동합니다.")
    
if st.button("다음 페이지"):
    go_to_운동종목설문()