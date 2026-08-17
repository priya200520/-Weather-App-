import streamlit as st
from utils import get_weather


# Page configuration
st.set_page_config(
    page_title="WeatherNow",
    page_icon="🌦️",
    layout="wide"
)


# Function for dynamic weather icon
def get_weather_icon(weather):

    weather = weather.lower()

    if "clear" in weather:
        return "☀️"

    elif "cloud" in weather:
        return "☁️"

    elif "rain" in weather or "drizzle" in weather:
        return "🌧️"

    elif "thunderstorm" in weather:
        return "⛈️"

    elif "snow" in weather:
        return "❄️"

    elif "mist" in weather or "fog" in weather or "haze" in weather:
        return "🌫️"

    else:
        return "🌦️"


# Function for dynamic weather theme
def get_weather_theme(weather):

    weather = weather.lower()

    if "clear" in weather:
        return "#4a90e2"

    elif "cloud" in weather:
        return "#596275"

    elif "rain" in weather or "drizzle" in weather:
        return "#34495e"

    elif "thunderstorm" in weather:
        return "#2c3e50"

    elif "snow" in weather:
        return "#7f8c8d"

    elif "mist" in weather or "fog" in weather or "haze" in weather:
        return "#636e72"

    else:
        return "#000000"


# Session state
if "weather_data" not in st.session_state:
    st.session_state.weather_data = None

if "search_history" not in st.session_state:
    st.session_state.search_history = []


# Get current theme
if (
    st.session_state.weather_data
    and "weather" in st.session_state.weather_data
):
    background_color = get_weather_theme(
        st.session_state.weather_data["weather"]
    )
else:
    background_color = "#000000"


# Dynamic styling
st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {background_color};
        color: white;
    }}

    .main-title {{
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        color: white;
    }}

    .subtitle {{
        text-align: center;
        font-size: 18px;
        color: #dcdde1;
    }}

    .weather-icon {{
        text-align: center;
        font-size: 100px;
        margin-top: 20px;
    }}

    .weather-status {{
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: white;
    }}

    [data-testid="stMetric"] {{
        background-color: rgba(0, 0, 0, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 12px;
    }}

    .footer {{
        text-align: center;
        color: #dcdde1;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# Sidebar - Recent Searches
st.sidebar.title("📍 Recent Searches")

if st.session_state.search_history:

    for recent_city in st.session_state.search_history:

        if st.sidebar.button(
            recent_city,
            key=f"history_{recent_city}"
        ):

            with st.spinner("Fetching weather data..."):

                weather_data = get_weather(recent_city)

                if weather_data and "error" not in weather_data:
                    st.session_state.weather_data = weather_data
                    st.rerun()

                else:
                    st.sidebar.error("Could not fetch weather.")

else:

    st.sidebar.write("No recent searches yet.")


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


# Search weather
if search:

    if city.strip():

        with st.spinner("Fetching weather data..."):

            weather_data = get_weather(city.strip())

            if weather_data and "error" in weather_data:

                st.session_state.weather_data = None

                st.error(
                    f"⚠️ Error: {weather_data['error']}"
                )

            elif weather_data:

                st.session_state.weather_data = weather_data

                city_name = weather_data["city"]

                # Add to search history without duplicates
                if city_name in st.session_state.search_history:
                    st.session_state.search_history.remove(city_name)

                st.session_state.search_history.insert(
                    0,
                    city_name
                )

                # Keep only last 5 searches
                st.session_state.search_history = (
                    st.session_state.search_history[:5]
                )

                st.rerun()

            else:

                st.session_state.weather_data = None

                st.error(
                    "City not found or weather data could not be fetched."
                )

    else:

        st.warning("Please enter a city name.")


# Display weather
if (
    st.session_state.weather_data
    and "weather" in st.session_state.weather_data
):

    data = st.session_state.weather_data

    weather_icon = get_weather_icon(
        data["weather"]
    )

    st.markdown(
        f'<div class="weather-icon">{weather_icon}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="weather-status">'
        f'{data["weather"].title()}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"### 📍 {data['city']}"
    )

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