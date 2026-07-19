"""
Weather Dashboard
Difficulty: Medium
Concepts: API, JSON, requests, caching
"""

import time
from datetime import datetime, timedelta

try:
    import requests
except ImportError:
    print("Please install required package:")
    print("  pip install requests")
    exit(1)

# City coordinates lookup
CITIES = {
    "london": (51.5074, -0.1278),
    "new york": (40.7128, -74.0060),
    "tokyo": (35.6762, 139.6503),
    "paris": (48.8566, 2.3522),
    "sydney": (-33.8688, 151.2093),
    "berlin": (52.5200, 13.4050),
    "moscow": (55.7558, 37.6173),
    "dubai": (25.2048, 55.2708),
    "mumbai": (19.0760, 72.8777),
    "singapore": (1.3521, 103.8198),
    "toronto": (43.6532, -79.3832),
    "beijing": (39.9042, 116.4074),
    "rio de janeiro": (-22.9068, -43.1729),
    "cairo": (30.0444, 31.2357),
    "mexico city": (19.4326, -99.1332),
    "bangkok": (13.7563, 100.5018),
    "istanbul": (41.0082, 28.9784),
    "seoul": (37.5665, 126.9780),
    "madrid": (40.4168, -3.7038),
    "rome": (41.9028, 12.4964),
}

# Cache storage
_cache = {}
CACHE_DURATION = 600  # 10 minutes in seconds


def get_weather_emoji(code):
    """Map WMO weather codes to emojis."""
    weather_map = {
        0: "☀️",   # Clear sky
        1: "🌤️",  # Mainly clear
        2: "⛅",   # Partly cloudy
        3: "☁️",   # Overcast
        45: "🌫️", # Fog
        48: "🌫️", # Depositing rime fog
        51: "🌧️", # Drizzle light
        53: "🌧️", # Drizzle moderate
        55: "🌧️", # Drizzle dense
        61: "🌦️", # Rain slight
        63: "🌧️", # Rain moderate
        65: "🌧️", # Rain heavy
        71: "🌨️", # Snow slight
        73: "🌨️", # Snow moderate
        75: "❄️",  # Snow heavy
        80: "🌦️", # Rain showers
        81: "🌧️", # Rain showers moderate
        82: "⛈️",  # Rain showers violent
        95: "⛈️", # Thunderstorm
        96: "⛈️", # Thunderstorm with hail
        99: "⛈️", # Thunderstorm with heavy hail
    }
    return weather_map.get(code, "🌡️")


def get_weather_description(code):
    """Get human-readable weather description."""
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Rain showers",
        81: "Moderate showers",
        82: "Violent showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Severe thunderstorm",
    }
    return descriptions.get(code, "Unknown")


def fetch_weather(lat, lon):
    """Fetch weather data from Open-Meteo API with caching."""
    cache_key = f"{lat},{lon}"
    now = time.time()

    # Check cache
    if cache_key in _cache:
        cached_data, cached_time = _cache[cache_key]
        if now - cached_time < CACHE_DURATION:
            print("  📦 Using cached data")
            return cached_data

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
        "daily": "temperature_2m_max,temperature_2m_min,weather_code",
        "timezone": "auto",
        "forecast_days": 4,
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        _cache[cache_key] = (data, now)
        return data
    except requests.RequestException as e:
        print(f"❌ Error fetching weather: {e}")
        return None


def display_current(city, data):
    """Display current weather conditions."""
    current = data.get("current", {})
    code = current.get("weather_code", 0)
    emoji = get_weather_emoji(code)
    desc = get_weather_description(code)

    print(f"\n{'─' * 50}")
    print(f"  🌍 {city.title()}")
    print(f"  {emoji}  {desc}")
    print(f"{'─' * 50}")
    print(f"  🌡️  Temperature:  {current.get('temperature_2m', 'N/A')}°C")
    print(f"  💧 Humidity:     {current.get('relative_humidity_2m', 'N/A')}%")
    print(f"  💨 Wind Speed:   {current.get('wind_speed_10m', 'N/A')} km/h")
    print(f"{'─' * 50}")


def display_forecast(data):
    """Display 3-day forecast."""
    daily = data.get("daily", {})
    dates = daily.get("time", [])
    max_temps = daily.get("temperature_2m_max", [])
    min_temps = daily.get("temperature_2m_min", [])
    codes = daily.get("weather_code", [])

    print(f"\n  📅 3-Day Forecast:")
    print(f"  {'─' * 45}")

    for i in range(min(4, len(dates))):
        if i == 0:
            day_label = "Today"
        elif i == 1:
            day_label = "Tomorrow"
        else:
            day_label = datetime.strptime(dates[i], "%Y-%m-%d").strftime("%A")

        emoji = get_weather_emoji(codes[i])
        desc = get_weather_description(codes[i])
        print(f"  {day_label:<10} {emoji}  {desc:<18}  {min_temps[i]:.0f}° - {max_temps[i]:.0f}°C")

    print(f"  {'─' * 45}")


def compare_cities(city1, city2):
    """Compare weather between two cities."""
    print(f"\n{'=' * 60}")
    print(f"  ⚖️  WEATHER COMPARISON")
    print(f"{'=' * 60}")

    for city in [city1, city2]:
        coords = CITIES.get(city.lower())
        if not coords:
            print(f"❌ City not found: {city}")
            continue

        data = fetch_weather(*coords)
        if data:
            display_current(city, data)


def main():
    """Main application loop."""
    print("=" * 55)
    print("🌤️  WEATHER DASHBOARD")
    print("   Powered by Open-Meteo (Free, No API Key)")
    print("=" * 55)
    print(f"\nSupported cities: {', '.join(sorted(CITIES.keys()))}")

    while True:
        print("\n📂 Menu:")
        print("  1. 🌡️  Current weather")
        print("  2. 📅 3-Day forecast")
        print("  3. ⚖️  Compare two cities")
        print("  4. 🚪 Exit")

        choice = input("\nChoose (1-4): ").strip()

        if choice == "1":
            city = input("\nEnter city name: ").strip().lower()
            coords = CITIES.get(city)
            if not coords:
                print(f"❌ City not found. Try: {', '.join(list(CITIES.keys())[:5])}...")
                continue

            print(f"\n⏳ Fetching weather for {city.title()}...")
            data = fetch_weather(*coords)
            if data:
                display_current(city, data)

        elif choice == "2":
            city = input("\nEnter city name: ").strip().lower()
            coords = CITIES.get(city)
            if not coords:
                print("❌ City not found.")
                continue

            print(f"\n⏳ Fetching forecast for {city.title()}...")
            data = fetch_weather(*coords)
            if data:
                display_current(city, data)
                display_forecast(data)

        elif choice == "3":
            city1 = input("\nFirst city: ").strip().lower()
            city2 = input("Second city: ").strip().lower()
            compare_cities(city1, city2)

        elif choice == "4":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
