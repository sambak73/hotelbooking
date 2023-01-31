import streamlit as st
from PIL import Image
import plotly.express as px
from weather import get_value

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days:', min_value=1, max_value=5,
                 help='Slide and place the pointer to select the number of days')
option = st.selectbox('Select the data to view', ('Temperature', 'Sky'))

st.subheader(f'{option} for the next {days} days in {place}')

sky_images = {
    'Clear': 'images/clear.png',
    'Clouds': 'images/cloud.png',
    'Rain': 'images/rain.png',
    'Snow': 'images/snow.png'
}

if place:

    d, t =  get_value(place=place, days=days, choice=option)

    if option == 'Temperature':
        fig = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})
        st.plotly_chart(fig)
    if option == 'Sky':
        sky_conditions = [sky_images[condition] for condition in t]
        st.image(sky_conditions, width=100, caption=d)
