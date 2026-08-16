import streamlit as st
from utils import get_weather

# Page configuration
st.set_page_config(
    page_title="WeatherNow",
    page_icon="🌦️",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>

.stApp {
    background-color: #000000;
    color: white;
}

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: white;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #b0b0b0;
}

.weather-icon {
    text-align: center;
    font-size: 100px;
    margin-top: 20px;
}

.weather-status {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: white;
}

[data-testid="stMetric"] {
    background-color: #1c1c1c;
    border: 1px solid #333333;
    padding: 20px;
    border-radius: 12px;
}

.footer {
    text-align: center;
    color: #888888;
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
        "🔍 Search City",
        placeholder="Enter city name..."
    )

with col2:
    st.write("")
    search = st.button(
        "Search",
        use_container_width=True
    )


# Session state
if "weather_data" not in st.session_state:
    st.session_state.weather_data = None


# Search weather
if search:

    if city.strip():

        with st.spinner("Fetching weather data..."):

            weather_data = get_weather(city)

            if weather_data:
                st.session_state.weather_data = weather_data
            else:
                st.error(
                    "City not found or weather data could not be fetched."
                )

    else:
        st.warning("Please enter a city name.")


# Display weather
if st.session_state.weather_data:

    data = st.session_state.weather_data

    st.markdown(
        '<div class="weather-icon">🌤️</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="weather-status">{data["weather"].title()}</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"### 📍 {data['city']}")
    st.caption("Current Weather Information")


    # Main weather cards
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🌡️ Temperature",
            f"{data['temperature']} °C"
        )

        st.metric(
            "☁️ Weather",
            data["weather"].title()
        )

    with col2:
        st.metric(
            "💧 Humidity",
            f"{data['humidity']} %"
        )

        st.metric(
            "💨 Wind Speed",
            f"{data['wind_speed']} m/s"
        )


    st.divider()


    # Additional details
    st.subheader("📊 Weather Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🌡️ Feels Like",
            f"{data['feels_like']} °C"
        )

    with col2:
        st.metric(
            "📊 Pressure",
            f"{data['pressure']} hPa"
        )

    with col3:
        st.metric(
            "👁️ Visibility",
            f"{data['visibility']} km"
        )

else:

    st.markdown(
        '<div class="weather-icon">🌦️</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="weather-status">Search for a city</div>',
        unsafe_allow_html=True
    )


# Footer
st.divider()

st.markdown(
    '<p class="footer">🌦️ WeatherNow • Built with Python & Streamlit</p>',
    unsafe_allow_html=True
)