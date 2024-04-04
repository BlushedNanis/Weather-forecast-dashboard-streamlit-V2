import streamlit as st
import plotly.express as px
from backend import get_forecast_data


st.set_page_config(page_title="Weather Forecast", layout="wide")

col1, col2 = st.columns(2)

with col1:
#Webapp body
    st.title(body="Weather forecast for the next days", anchor=False)
    st.divider()
    place = st.text_input(label="Place:",
                        placeholder="Type the name of the city",
                        help="If the city name exists in different countries"\
                            " add a comma followed by the country abbreviation"\
                            " i.e. ,ca ,mx, us").capitalize()
    days = st.slider(label="Forecast days", min_value=1, max_value=5,
            help="This will be the number of forecasted days",
            value=2)
    option = st.selectbox(label="Select the data to view",
                        options=("Temperature", "Sky"))
    st.divider()
    
with col2:
    try:
        
        if place:
            data = get_forecast_data(place, days)
            
            if option == "Temperature":
                temperatures = [dict["main"]["temp"] for dict in data]
                dates = [dict["dt_txt"] for dict in data]
                figure = px.line(x=dates, y=temperatures)
                st.plotly_chart(figure_or_data=figure)
                
            if option == "Sky":
                icons = {"Clear": "icons\\sunny.png", "Rain": "icons\\rainy.png",
                        "Clouds": "icons\\cloudy.png", "Snow": "icons\\snowy.png"}
                sky_conditions = [dict["weather"][0]["main"] for dict in data]
                icons_paths = [icons[condition] for condition in sky_conditions]
                st.image(icons_paths, width=115)

    except KeyError:
        st.warning("Looks like you introduced a non-existing city, please try again.")