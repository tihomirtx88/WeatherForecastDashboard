import streamlit as st
import plotly.express as px

st.title("Weather Forcast for the Next Days");
place = st.text_input("Place: ");
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days");
option = st.selectbox("Select data to view", ("Temperature", "Sky"));
st.subheader(f"{option} for next {days} days in {place}");

def get_data(days):
    dates = ["2022-25-10", "2024-16-11", "2021-13-11"];
    temperatures = [11, 12, 14];
    temperatures = [days * i for i in temperatures];
    return days, temperatures

d, t = get_data(days);

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperatures (C)"});
st.plotly_chart(figure);