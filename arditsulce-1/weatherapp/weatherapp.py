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
    try:
        filtered_data =  get_value(place=place, days=days)

        if option == 'Temperature':
            d = [item['dt_txt'] for item in filtered_data]
            t = [item['main']['temp'] for item in filtered_data]
            t = [tc/10 for tc in t]
            fig = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(fig)
        if option == 'Sky':
            d = [item['dt_txt'] for item in filtered_data]
            t = [item['weather'][0]['main'] for item in filtered_data]
            sky_conditions = [sky_images[condition] for condition in t]
            st.image(sky_conditions, width=100, caption=d)
    except KeyError:
        st.write(f'{place} is not found, Please try with correct place')