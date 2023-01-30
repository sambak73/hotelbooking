import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days:', min_value=1, max_value=5,
                 help='Slide and place the pointer to select the number of days')
option = st.selectbox('Select the data to view',('Temperature','Sky'))

st.subheader(f'{option} for the next {days} days in {place}')

def get_value(days):
    dates = ['2022-12-02','2022-12-03','2022-12-04']
    temp = [10.1,12.3,11.2]
    temp_days = [days * i for i in temp]
    return dates, temp_days

d,t = get_value(days)

fig = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})

st.plotly_chart(fig)