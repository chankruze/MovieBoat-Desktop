"""
Author: chankruze (chankruze@geekofia.in)
Created: Wed Dec 30 2020 02:51:01 GMT+0530 (India Standard Time)

Copyright (c) Geekofia 2020 and beyond
"""

import requests
import json

API_URL = "https://yts.geekofia.in/api/graphql"

q = """
{
  getMovies(limit: 4) {
    movie_count
        limit
        page_number
        movies {
            id
            title
            year
            rating
            medium_cover_proxy
            genres
        }
    }
}
"""

resp = requests.post(API_URL, json={'query': q}).json()
movies = resp["data"]["getMovies"]["movies"]

print(movies)
