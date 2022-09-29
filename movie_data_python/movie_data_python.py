
from asyncio.windows_events import NULL


def action_select():
    #print available actions
    print("OPTIONS: view, insert, delete, search, sort, or close")

    #user selects an action
    action = input("Select option: ")

    #view the table
    if action == ("view"):
        view()
        action_select()

    #insert a new movie into database
    elif action == ("insert"):
        insert_movie()

    #removes a movie from the database
    elif action == ("delete"):
        delete_movie()

    #searches through entries
    elif action == ("search"):
        search()

    #closes the connection
    elif action == ("close"):
        connection.close()

    else:
        print("not a valid option, please try again")
        action_select()



#prints all the entries
def view():
    cursor.execute('SELECT * FROM "Movie Data"')

    for i in cursor:
        print(i)
    action_select()

#Inserts a new entry into the database
def insert_movie():
    title = input("Enter the name of the movie: ")
    genre = input("Enter the genre of {}: ".format(title))
    director = input("Enter the name of the director of {}: ".format(title))
    release_year = get_release_year(title)
    country = input("Enter the country of origin of {}: ".format(title))
    rating = get_rating(title)
    is_favorite = get_is_favorite(title)
    date = get_date(title)
    if (date):
        cursor.execute('''
                    INSERT INTO "Movie Data" (Title, Genre, Director, "Release Year", Country, Rating, "Favorite?", "Date Watched")
                    VALUES
                    ('{}', '{}', '{}', {}, '{}', {}, '{}', '{}')
                    '''.format(title, genre, director, release_year, country, rating, is_favorite, date))
    else: 
        cursor.execute('''
                    INSERT INTO "Movie Data" (Title, Genre, Director, "Release Year", Country, Rating, "Favorite?", "Date Watched")
                    VALUES
                    ('{}', '{}', '{}', {}, '{}', {}, '{}', NULL)
                    '''.format(title, genre, director, release_year, country, rating, is_favorite))
    connection.commit()
    action_select()

#Deletes an entry from database
def delete_movie():
    print("Would you like to delete entry by id or title? (or enter back to go back)")
    option = input()
    if option == "id":
        id = get_id()
        cursor.execute('''
                    SELECT Title FROM "Movie Data" WHERE id='{}'
        '''.format(id))
        title = str(cursor.fetchone())
        cursor.execute('''
                    DELETE FROM "Movie Data" WHERE id='{}'
        '''.format(id))
        connection.commit()
        deleted = cursor.rowcount
        if deleted == 0:
            print("nothing to delete at this id")
        else:
            print("successfully deleted {}".format(title))
        action_select()
    elif option == "title":
        title = input("Enter the name of the movie: ")
        cursor.execute('''
                    DELETE FROM "Movie Data" WHERE Title='{}'
        '''.format(title))
        connection.commit()
        deleted = cursor.rowcount
        if deleted == 0:
            print("There is no entry with this title")
        elif deleted == 1:
            print("successfully deleted {}".format(title))
        else:
            print("successfully deleted {} entries of {}".format(deleted, title))
        action_select()
    elif option == "back":
        action_select()
    else:
        print("not a valid option, please try again")
        delete_movie()

    
#Searches through entries based on selected criteria

def search():
    print("search by id, title, genre, director, release year, country, rating, favorites, date watched, or go back?")
    term = input()
    if term == "id":
        #search for a specific id
        id = get_id()
        cursor.execute('''
                    SELECT * FROM "Movie Data" WHERE id='{}'
        '''.format(id))
        entry = cursor.fetchone()
        print(entry)
    elif term == "title":
        #search for a specific title
        title = get_title()  
        cursor.execute('''
                    SELECT * FROM "Movie Data" WHERE Title='{}'
        '''.format(title))
        for i in cursor:
            print(i)
    elif term == "genre":
        #search for a specific genre
        genre = get_genre()  
        cursor.execute('''
                    SELECT * FROM "Movie Data" WHERE Genre='{}'
        '''.format(genre))
        for i in cursor:
            print(i)
    elif term == "director":
        #search for a specific director
        director = get_director()
        cursor.execute('''
                    SELECT * FROM "Movie Data" WHERE Director='{}'
        '''.format(director))
        for i in cursor:
            print(i)
    elif term == "release year":
        #search for a specific release year or decade
        year = get_release_year("this is just for search")
        cursor.execute('''
                    SELECT * FROM "Movie Data" WHERE "Release Year"='{}'
        '''.format(year))
        for i in cursor:
            print(i)
    elif term == "country":
        #search for a specific country
        country = get_country()
        cursor.execute('''
                    SELECT * FROM "Movie Data" WHERE Country='{}'
        '''.format(country))
        for i in cursor:
            print(i)
    elif term == "rating":
        #search for a specific rating
        rating = get_rating("this is just for search")
        cursor.execute('''
                    SELECT * FROM "Movie Data" WHERE Rating='{}'
        '''.format(rating))
        if cursor.rowcount == 0:
            print("There are no entries with this rating")
        else:
            for i in cursor:
                print(i)
    elif term == "date watched":
        #search for a specific day, month, year
        search_date()
    elif term == "back" or term == "go back":
        action_select()
    else:
        print("Not a valid option")
        action_select()

    action_select()
       
    
    


#       HELPER FUNCTIONS FOR ABOVE FUNCTIONS
#
#
#




#gets the release year and makes sure it is valid
def get_release_year(title):
    while True:
        try:
            if title != "this is just for search":
                year = int(input("Enter the year {} was released: ".format(title)))
            else:
                year = int(input("Enter the year of relase: "))
        except ValueError:
            print("that is not a year")
            continue
        else:
            if year < 1800 or year > 2050:
                print ("this year is not possible")
                continue
            else:
                break
    return year

#Gets the rating and makes sure it is valid
def get_rating(title):
    while True:
        try:
            if title != "this is just for search":
                rating = float(input("Enter your rating for {} (from 0 to 10 up to one decimal place): ".format(title)))
            else:
                rating = int(input("Enter the rating: "))
        except ValueError:
            print("not a number")
            continue
        else:
            if rating < 0.0 or rating > 10.0:
                print("this is not a valid rating")
                continue
            else:
                break
    return rating

#Determines if movie will be added to favorites
def get_is_favorite(title):
    while True:
        fav = input("Add {} to your favorites? (yes or no): ".format(title))
        if fav != "yes" and fav!= "no":
            print("Please answer yes or no")
            continue
        else:
            if fav == "yes":
                return True
            return False

#Used to get the date the movie was watched or returns None if not known
def get_date(title):
    while True:
        date = input("Enter the date you watched {} in the form of YYYY/MM/DD (leave blank if you don't know): ".format(title))
        if not date:
            return None
        else:
            return date

#Used to get id of entry when searching by id
def get_id():
    while True:
        try:
            id = int(input("What is the id of the entry? "))
        except ValueError:
            print("not a number")
            continue
        else:
            cursor.execute('SELECT max(id) FROM "Movie Data"')
            max_id = cursor.fetchone()[0]
            if id < 0 or id > max_id:
                print("this is not a valid id")
                continue
            else:
                break
    return id

#Used to get title of movie
def get_title():
    while True:
        print("What is the title of the movie?")
        title = input()
        cursor.execute('''
                    SELECT * FROM "Movie Data" WHERE Title='{}'
        '''.format(title))
        if cursor.rowcount == 0:
            print("There are no entries with this title")
            search()
        else:
            break
    return title

#Used to get the genre of the movie
def get_genre():
    while True:
        genres = ["Action", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Horror", "Science Fiction", "Western"]
        print("What is the genre of the movie?")
        genre = input()
        if genre in genres:
            cursor.execute('''
                    SELECT * FROM "Movie Data" WHERE Genre='{}'
            '''.format(genre))
            if cursor.rowcount == 0:
                print("There are no entries with this genre")
                search()
            else:
                break
        else:
            print("not a valid genre")
            print("The genres are Action, Comedy, Crime, Documentary, Drama, Fantasy, Horror, Science Fiction, and Western")
        return genre

#Used to get the director of movie 
def get_director():
    while True:
        print("Who is the director of the movie?")
        director = input()
        cursor.execute('''
                    SELECT * FROM "Movie Data" WHERE Director='{}'
        '''.format(director))
        if cursor.rowcount == 0:
            print("There are no entries with this Director")
            search()
        else:
            break
    return director

#Used to get the country of origin of movie
def get_country():
    while True:
        print("What is the country of origin?")
        country = input()
        cursor.execute('''
                    SELECT * FROM "Movie Data" WHERE Country='{}'
        '''.format(country))
        if cursor.rowcount == 0:
            print("There are no entries from this country")
        else:
            break
    return country

def search_date():
    while True:
        print("Search by year, month, date, or go back?")
        select = input()
        if select == "year":
            #search by year
            try:
                print("What year would you like to search?")
                year = int(input())
            except ValueError:
                print("not a number")
                continue
            if year < 1850 or year > 2050:
                print("this is not a valid year")
            else:
                cursor.execute('''
                        SELECT * FROM "Movie Data" WHERE "Date Watched" LIKE '%{}%'
                '''.format(year))
                if cursor.rowcount == 0:
                    print("There are no movies watched in that year")
                else:
                    for i in cursor:
                        print(i)
        elif select == "month":
            #search by month
            break
        elif select == "date":
            #search by exact date
            break
        elif select == "back":
            search()
        else:
            print("this is not a valid option")
    action_select()
    

            
  


            













#importing module  
import pypyodbc  
from datetime import datetime
#creating connection Object which will contain SQL Server Connection  
#fill in your own Server and Database name
#make sure to set server to not timeout in Microsoft SQL Server Management Studio
print("Loading...")
connection = pypyodbc.connect('Driver={SQL Server Native Client 11.0};Server=LAPTOP-J9R8FKKO;Database=testforproject;Trusted_Connection=yes')  
cursor = connection.cursor()
  
print("Connection Successfully Established")  



action_select()
