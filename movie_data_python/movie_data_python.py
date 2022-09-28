
from asyncio.windows_events import NULL


def action_select():
    #print available actions
    print("OPTIONS: view, delete, insert, close")

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
    view_options()

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
    
    


#       HELPER FUNCTIONS FOR ABOVE FUNCTIONS
#
#
#


def view_options():
    print("Would you like to sort, search, or go back?")
    option = input()
    if option == "search":
        search()
    elif option == "sort":
        #sort
        return 0
    elif option == "back" or option == "go back":
        action_select()
    else:
        print("Not a valid option")


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
        return 0
    elif term == "release year":
        #search for a specific release year or decade
        return 0
    elif term == "country":
        #search for a specific country
        return 0
    elif term == "rating":
        #search for a specific rating
        return 0
    elif term == "favorites":
        #search for favorites
        return 0
    elif term == "date watched":
        #search for a specific day, month, year
        return 0
    elif term == "back" or term == "go back":
        view_options()
    else:
        print("Not a valid option")
        action_select()

    action_select()








#gets the release year and makes sure it is valid
def get_release_year(title):
    while True:
        try:
            year = int(input("Enter the year {} was released: ".format(title)))
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


def get_rating(title):
    while True:
        try:
            stars = float(input("Enter your rating for {} (from 0 to 10 up to one decimal place): ".format(title)))
        except ValueError:
            print("not a number")
            continue
        else:
            if stars < 0.0 or stars > 10.0:
                print("this is not a valid rating")
                continue
            else:
                break
    return stars

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

def get_date(title):
    while True:
        date = input("Enter the date you watched {} in the form of YYYY/MM/DD (leave blank if you don't know): ".format(title))
        if not date:
            return None
        else:
            return date

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
            return title

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
                return genre
        else:
            print("not a valid genre")
            print("The genres are Action, Comedy, Crime, Documentary, Drama, Fantasy, Horror, Science Fiction, and Western")
  


            













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
