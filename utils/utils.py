from langchain_core.tools import tool
import requests
from bs4 import BeautifulSoup
import json

from langchain_core.tools import tool

@tool
def available_movies(city:str)->list:
    """gives list of movies available in that city """
    url=f"https://ticketnew.com/movies/{city.lower()}" 
    response=requests.get(url) 
    soup=BeautifulSoup(response.text,"html.parser") 
    movies=[] 
    movies_list=soup.find_all("h5",class_="dds-tracking-tight dds-text-lg dds-font-semibold dds-overflow-hidden dds-whitespace-normal dds-line-clamp-2 dds-text-primary dds-my-0") 
    for list in movies_list: 
        movies.append(list.get_text()) 
        
    return json.dumps(movies if movies else ["No movies found"])
####
@tool
def movie_link(movie_name: str, city: str):
    """this returns movie link"""
    url=f"https://ticketnew.com/movies/{city.lower()}" 
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")

    div_list=soup.find_all("div",class_="dds-w-full dds-h-full item-cards")
    main_url="https://ticketnew.com"
    final_link=None
    for div in div_list:
        anchor=div.find("a")
        if anchor and anchor.get("href"):
            link=anchor["href"]
            slug=link.split("/")[-1]
            slug_name=slug.split("-movie-detail")[0]
            
            if movie_name.lower().replace(" ","-") in slug_name:
                return json.dumps({"link": main_url + link})

    return json.dumps({"error": "Movie not found"})

