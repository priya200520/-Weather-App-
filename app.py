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

/* Main background */
.stApp {
    background-color: #000000;
    color: white;
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: white;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #b0b0b0;
}

/* Weather cards */
[data-testid="stMetric"] {
    background-color: #1c1c1c;
    border: 1px solid #333333;
    padding: 20px;
    border-radius: 12px;
}

/* Input box */
input {
    background-color: #1c1c1c !important;
    color: white !important;
}

/* Footer */
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


# Display city
display_city = city if city else "Your City"


# Weather section
st.markdown(f"### 📍 {display_city}")
st.caption("Current Weather Information")


# Main weather cards
col1, col2 = st.columns(2)

with col1:
    st.metric("🌡️ Temperature", "-- °C")
    st.metric("☁️ Weather", "--")

with col2:
    st.metric("💧 Humidity", "-- %")
    st.metric("💨 Wind Speed", "-- km/h")


st.divider()


# Additional details
st.subheader("📊 Weather Details")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌡️ Feels Like", "-- °C")

with col2:
  st.metric("📊 Pressure", "-- hPa")

with col3:
    st.metric("👁️ Visibility", "-- km")


# Footer
st.divider()

st.markdown(
    '<p class="footer">🌦️ WeatherNow • Built with Python & Streamlit</p>',
    unsafe_allow_html=True
)