import streamlit as st
import pandas as pd
from backend import get_forecast_data, filter_data


st.set_page_config(page_title="Weather Forecast")


#Webapp body
st.title(body="Weather Forecast for the Next Days", anchor=False)
st.divider()
place = st.text_input(label="Place:",
                    placeholder="Type the name of the city",
                    help="If the city name exists in different countries"\
                        " add a comma followed by the country abbreviation"\
                        " i.e. ,ca ,mx, us").capitalize()
days = st.slider(label="Forecast days", min_value=1, max_value=5,
        help="This will be the number of forecasted days",
        value=3)
st.divider()

#Tabs set up
tab1, tab2, tab3, tab4 = st.tabs([":thermometer: Temperature Chart, C",
                                  ":mostly_sunny: Weather Conditions",
                                  ":cyclone: Wind Chart, m/s",
                                  ":sweat_drops: Humidity Chart, %"])
try:
    if place:
        
        data = get_forecast_data(place, days)    
        filtered_data = filter_data(data)
        dates = pd.to_datetime(filtered_data["dates"])
        
        with tab1:
            #Temperature chart in tab 1
            temp_data = {"Temperature": filtered_data["temperature"],
                        "Feels like": filtered_data["feel temperature"],
                        "Dates": dates}
            temp_df = pd.DataFrame(temp_data)
            st.line_chart(temp_df, x="Dates", y=["Temperature","Feels like"],
                        color=["#036bfc","#fc0303"])
                    
        with tab2:
            #Weather conditions in tab2
            icons_paths = [f"https://openweathermap.org/img/wn/{icon}@2x.png"
                        for icon in filtered_data["weather icons"]]
            icons_description = [f"{date.strftime("%Y-%m-%d %H %p")} \n"\
                f"{description.title()}" for date, description in
                zip(dates,filtered_data["weather description"])]
            st.image(icons_paths, caption=icons_description,
                    width=115)

        with tab3:
            #Wind chart tab3
            wind_data = {"Wind": filtered_data["wind speed"],
                        "Dates": dates}
            wind_df = pd.DataFrame(wind_data)
            st.line_chart(wind_df, x="Dates", y="Wind")
            
        with tab4:
            #Humidity chart tab4
            humidity_data = {"Humidity": filtered_data["humidity"],
                            "Dates": dates}
            humidity_df = pd.DataFrame(humidity_data)
            st.line_chart(humidity_df, x="Dates", y="Humidity", color="#2dfc03")
        
except KeyError:
    st.warning(":rotating_light: Looks like you introduced a non-existing"\
        " city, please try again. :rotating_light:")