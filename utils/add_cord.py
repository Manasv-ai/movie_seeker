import requests
import time
from data import data   # 👈 importing your existing data
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")


def get_lat_long(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    params = {
        "address": address,
        "key": GOOGLE_API_KEY
    }

    response = requests.get(url, params=params)
    res = response.json()

    if res["status"] == "OK":
        loc = res["results"][0]["geometry"]["location"]
        return loc["lat"], loc["lng"]
    else:
        print(f"Error: {res['status']} for {address}")
        return None, None


for theatre in data["Bangalore"]:
    address = theatre["address"]

    lat, lng = get_lat_long(address)

    theatre["latitude"] = lat
    theatre["longitude"] = lng

    print(f"{theatre['theatre']} → {lat}, {lng}")

    time.sleep(0.2)


# Save back to Python file (VERY IMPORTANT)
with open("data_with_coords.py", "w", encoding="utf-8") as f:
    f.write("data = ")
    f.write(str(data))

print("✅ Done! Saved in data_with_coords.py")