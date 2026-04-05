from geopy.distance import geodesic
from utils.data_with_coords import data
import json
from langchain_core.tools import tool

city_map = {
    "bengaluru": "Bangalore",
    "bangalore": "Bangalore",
}

@tool
def get_all_theatres(city: str):
    """Returns all theatres available in the given city"""
    city = city_map.get(city.lower(), city)

    theatres = data.get(city, [])
    
    return json.dumps(theatres if theatres else [{"error": "No theatres found"}])


def get_theatre_details(theatre_name: str):
    """Returns full details of a theatre from dataset"""
    
    for theatre in data["Bangalore"]:
        if theatre_name.lower() in theatre["theatre"].lower():
            return json.dumps(theatre)
    
    return json.dumps({"error": "Theatre not found"})

def calculate_distance(user_location,theatre):
    """returns distance of theatre from user location """
    theatre_location=(theatre["latitude"], theatre["longitude"])
    return geodesic(user_location, theatre_location).km

def filter_theatres(theatres, min_rating=0, max_price=float("inf")):
    """filters theatres based on rating and price"""
    
    filtered = []
    
    for t in theatres:
        rating = float(t.get("rating") or t.get("rating:") or 0)
        price = t["price_range"]["min"]
        
        if rating >= min_rating and price <= max_price:
            filtered.append(t)
    
    return filtered

def rank_theatres(theatres, user_location):
    """sort theatres by nearest + cheapest"""
    
    for t in theatres:
        theatre_location = (t["latitude"], t["longitude"])
        t["distance"] = geodesic(user_location, theatre_location).km

    return sorted(
        theatres,
        key=lambda x: (x["distance"], x["price_range"]["min"])
    )

@tool
def recommend_best_theatre(city, lat, lng, min_rating=4.0, max_price=500):
    
    """Returns top 5 best theatres based on distance, price, and rating"""
    city = city_map.get(city.lower(), city)

    
    user_location = (lat, lng)
    
    theatres = data.get(city, [])
    
    if not theatres:
        return json.dumps([{"error": "No theatres found"}])
    
    theatres = filter_theatres(theatres, min_rating, max_price)
    
    if not theatres:
        return json.dumps([{"error": "No theatres match filters"}])
    
    theatres = rank_theatres(theatres, user_location)
    
    result = theatres[:5]
    
    return json.dumps(result if result else [{"error": "No results"}])




if __name__ == "__main__":
    user_location = (12.9716, 77.5946)  # Bangalore
    
    results = recommend_best_theatre("Bangalore", user_location)
    
    for t in results:
        print(f"Theatre: {t['theatre']}")
        print(f"Distance: {round(t['distance'], 2)} km")
        print(f"Price: ₹{t['price_range']['min']}")
        print(f"Rating: {t.get('rating:')}")
        print("-" * 40)