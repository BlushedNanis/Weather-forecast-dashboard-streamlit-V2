import streamlit as st
import pandas as pd
from backend import get_forecast_data


st.set_page_config(page_title="Weather Forecast")


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
        value=3)
option = st.selectbox(label="Select the data to view",
                    options=("Temperature", "Sky"))
st.divider()


tab1, tab2, tab3 = st.tabs([":thermometer: Temperatures Chart",
                     ":mostly_sunny: Weather Conditions",
                     ":cyclone: Wind Chart"])

if place:
    
    weather, city = get_forecast_data(place, days)
    
    with tab1:
        
        temp_data = {"Temperatures": [dict["main"]["temp"] for dict in weather]}
        temp_data["Dates"] = pd.to_datetime([dict["dt_txt"] for dict in weather])
        temp_df = pd.DataFrame(data=temp_data)
        st.line_chart(temp_df, x="Dates", y="Temperatures")
                  
    with tab2:
        st.title("Test")
        icons = {"Clear": "icons\\sunny.png", "Rain": "icons\\rainy.png",
                "Clouds": "icons\\cloudy.png", "Snow": "icons\\snowy.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in weather]
        icons_paths = [icons[condition] for condition in sky_conditions]
        st.image(icons_paths, width=115)
        
    with tab3:
        st.title("Test")
        
        '''        except KeyError:
            st.warning("Looks like you introduced a non-existing city, please try again.")'''