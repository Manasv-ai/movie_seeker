from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
import os
from dotenv import load_dotenv

from tools import recommend_best_theatre,get_all_theatres
from utils.utils import available_movies, movie_link

load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

from tools import (
    recommend_best_theatre,
    get_all_theatres,
    get_theatre_details
)



model=init_chat_model("groq:openai/gpt-oss-120b")


message = """
You are MovieSeeker, a friendly conversational movie assistant.

DEFAULT CITY: Bengaluru — always use this if user doesn't mention a city.

TOOLS YOU HAVE:
1. available_movies(city) — list all movies in a city
2. movie_link(movie_name, city) — get booking link for a movie
3. recommend_best_theatre(city, lat, lng) — get top 5 theatres in a city
4. get_all_theatres(city) — get all theatres in a city

RULES:
- If user asks for theatres WITHOUT mentioning a movie → call get_all_theatres(city)
- If user asks for theatres FOR a movie → call movie_link then recommend_best_theatre
- If user asks what movies are playing → call available_movies(city)
- Never ask for movie if user just wants theatres
- Never ask for city — use Bengaluru by default
- Be friendly and conversational

WHEN RETURNING THEATRES (no movie), respond as plain text listing theatres nicely.

WHEN RETURNING THEATRES (with movie), return this JSON:
{
  "movie": "<name>",
  "link": "<url>",
  "theatres": [
    {"theatre": "...", "price": 270, "distance": 1.6, "rating": 4.2, "address": "..."}
  ]
}

IMPORTANT: Do NOT call a tool named JSON.
"""


agent = create_agent(
    model=model,
    tools=[
        available_movies,
        movie_link,
        recommend_best_theatre,
        get_all_theatres
    ],
    system_prompt=message,
)

def find_cheap_ticket(movie_name, city, lat, lng):
    query = f"Movie: {movie_name}\nCity: {city}\nLocation: ({lat}, {lng})"
    
    result = agent.invoke({
        "messages": [{"role": "user", "content": query}]
    })
    
    # Get only the final JSON response
    return result["messages"][-1].content




if __name__ == "__main__":
    result = find_cheap_ticket(
        "Biker",
        "Bengaluru",
        12.9716,
        77.5946
    )
    
    print(result)



