import streamlit as st

# Page settings
st.set_page_config(
    page_title="Weather App",
    page_icon="🌦️"
)

# Title
st.title("🌦️ Weather App")

st.write(
    "Enter a city name to check the current weather."
)

# City input
city = st.text_input(
    "Enter City Name:",
    placeholder="Example: Gurdaspur"
)

# Search button
if st.button("🔍 Check Weather"):

    if city:

        st.success(
            f"Searching weather for {city}..."
        )

    else:

        st.warning(
            "Please enter a city name."
        )

# Weather display section
st.divider()

st.subheader("📊 Weather Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🌡️ Temperature",
        "-- °C"
    )

with col2:
    st.metric(
        "💧 Humidity",
        "-- %"
    )

with col3:
    st.metric(
        "💨 Wind Speed",
        "-- km/h"
    )

st.write("🌤️ **Weather Condition:** --")