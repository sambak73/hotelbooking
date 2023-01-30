import streamlit as st

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days:', min_value=1, max_value=5,
                 help='Slide and place the pointer to select the number of days')
option = st.selectbox('Select the data to view',('Temperature','Sky'))

st.subheader(f'{option} for the next {days} days in {place}')
