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
    st.markdown("# 당신의 성별은?")

gender_selected = st.selectbox("성별", ["남자", "여자"])
st.session_state['gender'] = gender_selected
next_button = st.button("다음 페이지")

def go_to_나이설문():
    st.switch_page("pages/나이 설문.py")

if next_button:
    go_to_나이설문()

