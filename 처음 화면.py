import streamlit as st

st.set_page_config(
    page_title="TA 헬스케어",
    page_icon="💪🏼",
    layout="centered",
    initial_sidebar_state="collapsed",
)

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
    st.markdown("# 안녕하세요!")
    st.markdown("### TA 헬스케어에 오신 것을 환영합니다.")


skip_button = st.button("skip")
next_button = st.button("설문")


def go_to_이름설문():
    st.switch_page("pages/이름 설문.py")
if next_button:
    go_to_이름설문()

def go_to_매인화면():
    st.switch_page("pages/매인 화면.py")
if skip_button:
    go_to_매인화면()