import streamlit as st
import pickle
import pandas as pd


pipe = pickle.load(open('pipe.pkl','rb'))

st.title('T-20 Score Predictor')

teams = [
    'Chennai Super Kings',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Rajasthan Royals',
    'Sunrisers Hyderabad',
    'Punjab Kings',
    'Delhi Capitals',
    'Lucknow Super Giants',
    'Gujarat Titans'
]

teams = sorted(teams)


cities = [
    'Mumbai',
    'Chennai',
    'Bangalore',
    'Hyderabad',
    'Kolkata',
    'Delhi',
    'Ahmedabad',
    'Lucknow',
    'Jaipur',
    'Mohali'
]

cities = sorted(cities)


col1,col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select Batting Team ' , teams)
with col2:
  
    bowling_team = st.selectbox('Select Bowling Team ',teams)
    
city = st.selectbox('Select City',cities)
col3,col4,col5 = st.columns(3)

with col3:
    current_score =st.number_input('Current Score',min_value=0)
with col4:
    overs_done = st.number_input('Overs Done (Must Be Greater Than 5 )',min_value=5,max_value=20,step=1)
with col5:
    wickets = st.number_input('Wickets Taken',max_value=9)
    
runs_in_5 = st.number_input('Runs In Last 5 Overs')

if st.button('Predict Score'):
    balls_left = 120 - overs_done*6 
    wickets_left = 10-wickets
    crr = current_score / overs_done
    df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[city],'current_score':[current_score],'balls_left':[balls_left],'wickets_left':[wickets_left],'crr':[crr],'last_five_runs':[runs_in_5]})
    pred =pipe.predict(df)
    st.header(f'{batting_team} Will Score {round(pred[0])} Runs')
    
