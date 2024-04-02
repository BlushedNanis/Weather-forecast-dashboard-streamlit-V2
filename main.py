import streamlit as st
import plotly.express as px


st.title(body="Weather forecast for the next days", anchor=False)

place = st.text_input(label="Place:",
                      placeholder="Write the name of the place").capitalize()

days = st.slider(label="Forecast days", min_value=1, max_value=5,
          help="This will be the number of forecasted days",
          value=2)

option = st.selectbox(label="Select the data to view",
                    options=("Temperature", "Sky"))

st.divider()

st.header(body=f"{option} for the next {days} days in {place}", anchor=False)

