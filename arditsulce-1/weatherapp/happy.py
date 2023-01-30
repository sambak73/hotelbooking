import streamlit as st
import plotly.express as px
import pandas as pd

st.title('In Search for Happiness')
df = pd.read_csv('data/happy.csv')
values = []
for col in df.columns:
    value = col.upper()
    value = value.replace("_", " ")
    values.append(value)

xaxis = st.selectbox('Select the data for the x-axis',options=('GDP', 'Generosity', 'Happiness'))
yaxis = st.selectbox('Select the data for the y-axis',options=('GDP', 'Generosity', 'Happiness'))

st.subheader(f'{xaxis} and {yaxis}')


#st.write(df.head(0))
xdata = df[xaxis.lower()]
ydata = df[yaxis.lower()]

fig = px.scatter(x=xdata, y=ydata, labels={"x": xaxis, "y": yaxis})

st.plotly_chart(fig)