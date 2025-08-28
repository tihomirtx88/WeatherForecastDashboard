import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forcast for the Next Days");
place = st.text_input("Place: ");
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days");
option = st.selectbox("Select data to view", ("Temperature", "Sky"));
st.subheader(f"{option} for next {days} days in {place}");

if place:
    try:
        # Set temperature/sky data
        filtered_data = get_data(place, days);

        if option == "Temperature":
            temperatures = [data["main"]["temp"] / 10 for data in filtered_data];
            dates = [data["dt_txt"] for data in filtered_data];
            # Create temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperatures (C)"});
            st.plotly_chart(figure);

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"};
            sky_conditions = [data["weather"][0]["main"] for data in filtered_data];
            image_path = [images[condition] for condition in sky_conditions];
            st.image(image_path, width=115);
    except KeyError:
        st.write("This place does not exist");
