#434b05ce426ea940d14735803b0e13f6
# https://api.themoviedb.org/3/movie/550?api_key=434b05ce426ea940d14735803b0e13f6
import requests,json,csv,os
from itertools import islice
import pprint


#document all the parameters as variables
api_key = '434b05ce426ea940d14735803b0e13f6'


class Movie:
    title = ''
    movie_id = 0
    genres = []
    director = ''
    release_date = ''
    country = ''
    rating = -1
    favorite = False
    date_watched = ''
    language = ''
    overview = ''

    def __repr__(self):
        return "Movie(title={self.title!r}, ID={self.movie_id!r}, genres={self.genres!r}, director={self.director!r}, release date={self.release_date!r}, country={self.country!r}, rating={self.rating!r}, favorite={self.favorite!r}, date watched={self.date_watched!r}, language={self.language!r})".format(self=self)


'''Movie_ID = '464052'
#write a function to compose the query using the parameters provided
def get_data(API_key, Movie_ID):
    query = 'https://api.themoviedb.org/3/movie/'+Movie_ID+'?
             api_key='+API_key+'&language=en-US'
    response =  requests.get(query)
    if response.status_code==200: 
    #status code ==200 indicates the API query was successful
        array = response.json()
        text = json.dumps(array)
        return (text)
    else:
        return ("error")



'''



    
def get_movies(title, year, date_watched, rating):

    movie = Movie()
    Movie.title = title
    Movie.date_watched = date_watched
    Movie.rating = rating

    #establish query to search for movie with moviedata api
    query = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}&year={}'.format(api_key, title, year)

    # Make the request
    response = requests.get(query)

    
    d = response.json()
    movie.movie_id = d.get('results')[0].get('id')
    movie.release_date = d.get('results')[0].get('release_date')
    movie.language = d.get('results')[0].get('original_language')
    movie.overview = d.get('results')[0].get('overview')
    genres = []
    genre_index = 0
    for genre_id in d.get('results')[0].get('genre_ids'):
        print(genre_id)
        genre_query = 'https://api.themoviedb.org/3/genre/movie/list?api_key={}&with_genres={}'.format(api_key, genre_id)
        genre_response = requests.get(genre_query)
        g = genre_response.json()

        genre = (g.get('genres')[0].get('name'))
        
        
        genres.append(genre)
        genre_index = genre_index + 1

    movie.genres = genres
    genre_index = 0

    pprint.pprint(movie)
    print('\n')


def read_csv(file):
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        first_ten_rows = islice(reader, 200, 268)
        for row in first_ten_rows:
            title = row[1]
            year = int(row[2])
            rating = int(float(row[4])*2)
            date_watched = row[7]
            get_movies(title, year, rating, date_watched)




path = r'C:\Users\simon\Downloads\movie_csv\diary.csv'
read_csv(path)
#get_movies('The Matrix', 1999)