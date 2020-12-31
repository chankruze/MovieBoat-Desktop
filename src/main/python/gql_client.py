"""
Author: chankruze (chankruze@geekofia.in)
Created: Wed Dec 30 2020 02:51:01 GMT+0530 (India Standard Time)

Copyright (c) Geekofia 2020 and beyond
"""

import requests
import json

API_URL = "https://yts.geekofia.in/api/graphql"

# MOVIES_QUERY = """
# {
#   getMovies(limit: 50) {
#     movie_count
#         limit
#         page_number
#         movies {
#             id
#             title
#             year
#             rating
#             genres
#             medium_cover_proxy
#         }
#     }
# }
# """


def query_movies(query_string):
    url = f"https://yts.mx/api/v2/list_movies.json?{query_string}"

    query = f"""
    {{
        getSearchedMovies(url: "{url}") {{
            movies {{
              id
              title
              year
              rating
              genres
              medium_cover_proxy
            }}
        }}
    }}
    """

    # print("-------- DEBUG --------")
    print(url)
    print(query)
    # print("-------- DEBUG --------")

    resp = requests.post(API_URL, json={'query': query}).json()

    # print("-------- DEBUG --------")
    print(resp)
    # print("-------- DEBUG --------")

    movies = resp["data"]["getSearchedMovies"]["movies"]
    return movies
