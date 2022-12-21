
# https://api.themoviedb.org/3/movie/550?api_key=434b05ce426ea940d14735803b0e13f6
import requests,json,csv,os
from itertools import islice
import pprint
import urllib.parse
import time




#fill in your specific api key
api_key = '434b05ce426ea940d14735803b0e13f6'



#Movie class will contain all information about a movie that will be stored 
class Movie:
    title = ''
    movie_id = 0
    genres = []
    director = ''
    release_date = ''
    country = ''
    rating = -1
    date_watched = ''
    language = ''
    overview = ''

    def __repr__(self):
        return "Movie(title={self.title!r}, ID={self.movie_id!r}, genres={self.genres!r}, director={self.director!r}, release date={self.release_date!r}, country={self.country!r}, rating={self.rating!r}, date watched={self.date_watched!r}, language={self.language!r})".format(self=self)




#uses title and year to search for information using moviedata api and create a movie object that that will be added to database
def get_movies(title, year, rating, date_watched):
    try:
        movie = Movie()
        movie.title = title
        movie.date_watched = date_watched
        movie.rating = rating

        #establish query to search for movie with moviedata api
        query = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}&year={}'.format(api_key, title, year)

        # Make the request
        response = requests.get(query)

    
        d = response.json()
        if response.status_code == 200:
            try:
                movie.movie_id = d.get('results')[0].get('id')
                movie.director = get_director(movie)
                movie.country = get_country(movie)
                movie.release_date = str(d.get('results')[0].get('release_date'))
                movie.language = d.get('results')[0].get('original_language')
                movie.overview = d.get('results')[0].get('overview')
                genres = []
                genre_index = 0
                for genre_id in d.get('results')[0].get('genre_ids'):
                    genre_query = 'https://api.themoviedb.org/3/genre/movie/list?api_key={}'.format(api_key)
                    genre_response = requests.get(genre_query)
                    g = genre_response.json()
        

                    genre_list = (g.get('genres'))
                    for d in genre_list:
                        if d.get('id') == genre_id:
                            genre = d.get('name')
                            break
        
                    genres.append(genre)
                    genre_index = genre_index + 1

                movie.genres = genres
                genre_index = 0

                return movie
            except IndexError:
                print(('Could not find an entry for {}').format(title))
        else:
            print(f"An error occurred: {response.status_code}")
    except ConnectionResetError:
        get_movies(title, year, rating, date_watched)



def get_director(movie):
    try:
        movie_id = movie.movie_id
    
        query = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=en-US".format(movie_id, api_key)

        response = requests.get(query)

        if response.status_code == 200:
            data = response.json()
            directors = []
            director = ''
            title = movie.title
            for crew_member in data['crew']:
                if crew_member['job'] == 'Director':
                    directors.append(crew_member['name'])
            if len(directors) > 1:
                for d in directors:
                    director = director + d + ' & '
                director = director[:-3]
            elif len(directors) == 1:
                director = directors[0]
                return director
            return director
        
        else:
            print(f"An error occurred: {response.status_code}")
    except ConnectionResetError:
        get_director(movie)

def get_country(movie):
    try:
    
        movie_id = movie.movie_id
    
        query = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US".format(movie_id, api_key)

        response = requests.get(query)

        if response.status_code == 200:
            data = response.json()
            countries = []
            country = ''
            title = movie.title
            for c in data['production_countries']: 
                countries.append(c['name'])
            if len(countries) > 1:
                for c in countries:
                    country = country + c + ' & '
                country = country[:-3]
                print('The production countries of {} are {}'.format(title, country))
            elif len(countries) == 1:
                country = countries[0]
                print('The production country of {} is {}'.format(title, country))
                return country
            return country
        
        else:
            print(f"An error occurred: {response.status_code}")
    except ConnectionResetError:
        get_country(movie)


    




#iterates through csv to find title, year, rating, and date watched
def read_csv(file):
    movies = []
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        #first_ten_rows = islice(reader, 260, 268)
        #for row in first_ten_rows:
        for row in reader:
            title = row[1]
            year = int(row[2])
            if isinstance(row[4], int):    
                rating = int(float(row[4])*2)
            else:
                rating = -1
            date_watched = row[7]
            
            m = get_movies(title, year, rating, date_watched)
            movies.append(m)
    
        
    return movies
