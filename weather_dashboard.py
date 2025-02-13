import streamlit as st
import requests

# Function to get weather data
def get_weather(city_name, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

# Streamlit app
def main():
    st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")  # Set page title and icon
    
    # Custom background style (optional)
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f8ff;  # Light sky blue background
        }
        </style>
        """, unsafe_allow_html=True)

    # Title of the app
    st.title("Weather App 🌤️")

    # API Key and input field
    api_key = 'f092ccf4408aaa4d428a9a18c67248d1'  # Replace with your actual OpenWeatherMap API Key
    city_name = st.text_input("Enter City Name:", placeholder="e.g., New York, London, Tokyo")

    if city_name:
        with st.spinner("Fetching weather data..."):
            weather_data = get_weather(city_name, api_key)

        if weather_data.get('cod') == 200:
            # Display weather data with better formatting and icons
            st.write(f"### Weather in {city_name} 🌆")
            st.write(f"**Temperature:** {weather_data['main']['temp']}°C")
            st.write(f"**Weather:** {weather_data['weather'][0]['description']} ☁️")
            st.write(f"**Humidity:** {weather_data['main']['humidity']}% 💧")
            st.write(f"**Wind Speed:** {weather_data['wind']['speed']} m/s 💨")
        else:
            # Display error message
            st.error("City not found or invalid API key. Please try again.")
    
if __name__ == "__main__":
    main()
