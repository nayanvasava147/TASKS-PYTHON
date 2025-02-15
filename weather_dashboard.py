import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your OpenWeatherMap API key
API_KEY = "8672dc07b4153c1c8e0df807b3c5bf68"
CITY = "London"  # You can change this to any city
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data
def fetch_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Function to parse weather data
def parse_weather_data(data):
    main_data = data.get("main", {})
    wind_data = data.get("wind", {})
    weather_info = data.get("weather", [{}])[0]

    parsed_data = {
        "City": data.get("name"),
        "Temperature (°C)": main_data.get("temp"),
        "Humidity (%)": main_data.get("humidity"),
        "Wind Speed (m/s)": wind_data.get("speed"),
        "Weather Condition": weather_info.get("description"),
    }
    return parsed_data

# Function to create visualizations
def create_visualizations(df):
    sns.set(style="whitegrid")

    # Create a bar plot for temperature and humidity
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    sns.barplot(x=df.index, y=df["Temperature (°C)"], palette="coolwarm")
    plt.title(f"Temperature in {df['City'].iloc[0]}")
    plt.ylabel("Temperature (°C)")

    plt.subplot(2, 1, 2)
    sns.barplot(x=df.index, y=df["Humidity (%)"], palette="Blues")
    plt.title(f"Humidity in {df['City'].iloc[0]}")
    plt.ylabel("Humidity (%)")

    plt.tight_layout()
    plt.show()

    # Create a pie chart for weather condition
    plt.figure(figsize=(6, 6))
    weather_condition = df["Weather Condition"].iloc[0]
    plt.pie([1], labels=[weather_condition], autopct="%1.1f%%", colors=["lightblue"])
    plt.title(f"Weather Condition in {df['City'].iloc[0]}")
    plt.show()

# Main script
if __name__ == "__main__":
    # Fetch weather data
    weather_data = fetch_weather_data(CITY)
    if weather_data:
        print("Weather data fetched successfully!")
        
        # Parse and organize data
        parsed_data = parse_weather_data(weather_data)
        df = pd.DataFrame([parsed_data])
        print(df)

        # Generate visualizations
        create_visualizations(df)
    else:
        print("Failed to fetch weather data.")