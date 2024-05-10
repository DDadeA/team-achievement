import streamlit as st
from PIL import Image 

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
    st.markdown("# :violet[오늘의 보상:]") 
    if 'exercise' in st.session_state:
        selected_exercise = st.session_state['exercise']
    st.markdown(f"# :violet[오늘 {selected_exercise}를 했습니다. 오늘의 보상은 2000원어치의 음류수 쿠폰입니다.]")

쿠폰 = Image.open('pages/스타벅스 쿠폰.jpg')
st.image(쿠폰)

