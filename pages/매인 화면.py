import streamlit as st


st.title("오늘의 추천")
st.header("오늘의 운동 브리핑")
briefing_text = st.write("당신은 13세인 남자이며 오늘은 근력 운동을 하였습니다. ")
st.write(briefing_text)

st.header("오늘의 운동 추천")
recommend_text = st.write("당신의 추천 종목은 아래와 같습니다.")
st.write(recommend_text)
data = [['근력 운동', '윗몸 말아올리기'], ['유산소 운동', '조깅'], ['기타', '축구']]
st.table(data) 

prize_button = st.button("보상")

def go_to_보상():
    st.switch_page("pages/보상.py")
if prize_button:
    go_to_보상()