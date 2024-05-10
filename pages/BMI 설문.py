import streamlit as st

style = """
  <style>
    div.stApp {
      background: linear-gradient(129deg, rgba(79,207,100,1) 29%, rgba(89,136,144,1) 87%, rgba(97,90,163,1) 100%);
    }

    div.stButton > button {
      &:hover {
        border: 1px solid #afa !important;
      }
    }
    div.stButton > button[kind="secondary"] {
      background-color: white !important;
      color: #555 !important;
      border-radius: 16px !important;
    }
    div.stButton > button[kind="primary"] {
      background-color: #444 !important;
      color: white !important;
      border-radius: 16px !important;
      border: 1px solid #444 !important;
    }
  </style>
"""
st.markdown(style, unsafe_allow_html=True)

with st.container():
    st.markdown("# :violet[당신의 비만도는?]")

BMI_selected = st.selectbox("비만도", ["저체중", "정상", "비만 전 단계", "1단계 비만","2단계 비만", "3단계 비만" ])
st.session_state['BMI'] = BMI_selected
next_button = st.button("다음 페이지")

def go_to_운동종목설문():
    st.switch_page("pages/운동종목 설문.py")
if next_button:
    go_to_운동종목설문()