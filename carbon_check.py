import requests, sys

# Public UK Carbon Intensity API (no key required)
API_URL = "https://api.carbonintensity.org.uk/intensity"
THRESHOLD = 200  # gCO2/kWh – you can change this number

def main():
    try:
        r = requests.get(API_URL, timeout=10)
        data = r.json()
        value = data["data"][0]["intensity"]["forecast"]
        print(f"Carbon intensity = {value}")
        if value < THRESHOLD:
            print("✅ Green enough, proceed")
            sys.exit(0)
        else:
            print("⛔ Too high, skip")
            sys.exit(1)
    except Exception as e:
        print("⚠️ Error fetching carbon data:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
