import streamlit as st

def set_background(color):
  style = f"""
    <style>
      div.stApp {{
        background-color: {color};
      }}
    </style>
  """
  st.markdown(style, unsafe_allow_html=True)

set_background("#228B22")  

with st.container():    
    st.markdown("# :violet[오늘의 추천]")
    st.markdown("# :violet[당신은 13세이이남자이며 오늘은 근력운동을 하였습니다.]")
    st.markdown("# :violet[오늘의 운동 브리핑]")
    st.markdown("# :violet[오늘의 운동 추천]")
    
data = [['근력 운동', '윗몸 말아올리기'], ['유산소 운동', '조깅'], ['기타', '축구']]
st.table(data) 

prize_button = st.button("보상")

def go_to_보상():
    st.switch_page("pages/보상.py")
if prize_button:
    go_to_보상()