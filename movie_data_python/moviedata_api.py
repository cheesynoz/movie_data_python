#434b05ce426ea940d14735803b0e13f6
# https://api.themoviedb.org/3/movie/550?api_key=434b05ce426ea940d14735803b0e13f6
import requests,json,csv,os

#document all the parameters as variables
api_key = '434b05ce426ea940d14735803b0e13f6'
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



def write_file(filename, text):
    dataset = json.loads(text)
    csvFile = open(filename,'a')
    csvwriter = csv.writer(csvFile)
    #unpack the result to access the "collection name" element
    try:
        collection_name = dataset['belongs_to_collection']['name']
    except:
        #for movies that don't belong to a collection, assign null
        collection_name = None
    result = [dataset['original_title'],collection_name]
    # write data
    csvwriter.writerow(result)
    print (result)
    csvFile.close()'''

    
def get_movies():

    # Set the API endpoint URL
    endpoint = "https://api.moviedata.com/search"

    query = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}&year={}'.format(api_key, "The Matrix", 1999)

    # Set the query parameters
    params = {
      "q": "The Matrix"
    }

    # Make the request
    response = requests.get(query)


    # Print the response
    d = response.json()
    print(d.get('results')[0].get('title'))

    #for key, value in d.items():
       # print(key + ": " + str(value))


    #info = raw_info['title']

    
    

    # Returns a list of movies matching the search query, including the movie's ID

    [
      {
        "id": 12345,
        "title": "The Matrix",
        "year": 1999,
        "genre": "Sci-fi"
      },
      
    ]



#movie_list = ['464052','508442']
#write header to the file
#csvFile = open('movie_collection_data.csv','a')
#csvwriter = csv.writer(csvFile)
#csvwriter.writerow(['Movie_name','Collection_name'])
#csvFile.close()
#for movie in movie_list:
#    text = get_data(API_key, movie)
#    #make sure your process breaks when the pull was not successful 
#    #it's easier to debug this way
#    if text == "error":
#        break
#    write_file('movie_collection_data.csv', text)

get_movies()