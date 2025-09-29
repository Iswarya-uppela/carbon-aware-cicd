import requests
import sys

# Public UK Carbon Intensity API (no key required)
API_URL = "https://api.carbonintensity.org.uk/intensity"
THRESHOLD = 200  # gCO2/kWh

def main():
    try:
        # Fetch data from API
        r = requests.get(API_URL, timeout=10)
        data = r.json()["data"][0]
        
        forecast = data["intensity"]["forecast"]
        actual = data["intensity"]["actual"]
        index = data["intensity"]["index"]

        print(f"📊 Actual carbon intensity = {actual} gCO₂/kWh")
        print(f"🔮 Forecast carbon intensity = {forecast} gCO₂/kWh")
        print(f"🌍 Index = {index}")

        # Step 1: Check current (actual)
        if actual < THRESHOLD:
            print("✅ Current carbon intensity is low → proceed with job")
            sys.exit(0)

        # Step 2: If current is high, check forecast
        elif forecast < THRESHOLD:
            print("⏳ Current is high, but forecast is low → can run later")
            sys.exit(1)

        # Step 3: Both are high
        else:
            print("⛔ Both current and forecast carbon intensities are high → delaying job")
            sys.exit(1)

    except Exception as e:
        print("⚠️ Error fetching carbon data:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
