import streamlit as st
import plotly.express as px
from backend import get_forecast_data


#Webapp body
st.title(body="Weather forecast for the next days", anchor=False)
place = st.text_input(label="Place:", value="Toronto").capitalize()
days = st.slider(label="Forecast days", min_value=1, max_value=5,
          help="This will be the number of forecasted days",
          value=2)
option = st.selectbox(label="Select the data to view",
                      options=("Temperature", "Sky"))
st.divider()
st.header(body=f"{option} for the next {days} days in {place}", anchor=False)

data = get_forecast_data(place, days)

if option == "Temperature":
    temperatures = [dict["main"]["temp"] for dict in data]
    dates = [dict["dt_txt"] for dict in data]
    figure = px.line(x=dates, y=temperatures)
    st.plotly_chart(figure_or_data=figure)
    
if option == "Sky":
    sky = [dict["weather"][0]["main"] for dict in data]

