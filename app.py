import streamlit as st

# Page configuration
st.set_page_config(
    page_title="WeatherNow",
    page_icon="🌦️",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: gray;
}

</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    '<p class="main-title">🌦️ WeatherNow</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Get real-time weather updates for any city</p>',
    unsafe_allow_html=True
)

st.divider()


# Search section
col1, col2 = st.columns([4, 1])

with col1:

    city = st.text_input(
        "Search City",
        placeholder="Enter city name..."
    )

with col2:

    st.write("")
    search = st.button(
        "🔍 Search",
        use_container_width=True
    )


# Default city display
display_city = city if city else "Your City"


# Weather card
st.markdown("### 📍 " + display_city)

st.caption("Current Weather Information")


# Main weather section
col1, col2 = st.columns(2)

with col1:

    st.metric(
        "🌡️ Temperature",
        "-- °C"
    )

    st.metric(
        "☁️ Weather",
        "--"
    )

with col2:

    st.metric(
        "💧 Humidity",
        "-- %"
    )

    st.metric(
        "💨 Wind Speed",
        "-- km/h"
    )


st.divider()


# Additional information
st.subheader("📊 Weather Details")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Feels Like", "-- °C")

with col2:
    st.metric("Pressure", "-- hPa")

with col3:
    st.metric("Visibility", "-- km")


# Footer
st.divider()

st.markdown(
    "<center>🌦️ WeatherNow • Built with Python & Streamlit</center>",
    unsafe_allow_html=True
)