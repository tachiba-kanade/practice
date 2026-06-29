"""
GOAL 1

- user search movies
- user add movie/save to local 
- user can view the saved

Data layer: Trakt API, saved movies, ratings, movie details
Logic layer: add movie, mark watched, calculate stats

First make search_movies(query)
Then make save_movie(movie)
Then make mark_watched(movie_id)

movie-tracker
→ search movie
→ add to watchlist
→ view watchlist
→ mark watched
→ rate movie
→ view watched history

Search movie → add to watchlist → mark watched → rate → view dashboard.

Version 1:
- Search movie from Trakt
- Show movie results in Streamlit
- Add selected movie to watchlist
- Store watchlist locally
- Display watchlist

Version 2:
- Mark movie as watched
- Add personal rating
- Add watched date
- Separate Watchlist and Watched pages

Version 3:
- Stats dashboard
- Favorite genres
- Highest-rated movies
- Recently watched list

"""

def mov_search():
    pass

def mov_add():
    pass

def view_saved():
    pass



from trakt import Trakt
import logging


# Enable DEBUG Logging
logging.basicConfig(level=logging.DEBUG)

# Setup client defaults
Trakt.configuration.defaults.client(
    id='mock-client_id',
    secret='mock-client_secret'
)
