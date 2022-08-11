
from asyncio.windows_events import NULL


def action_select():
    #print available actions
    print("OPTIONS: view, insert, close")

    #user selects an action
    action = input("Select option: ")

    #view the table
    if action == ("view"):
        view()
        action_select()

    #insert a new movie into database
    elif action == ("insert"):
        insert_movie()

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


def insert_movie():
    title = input("Enter the name of the movie: ")
    genre = input("Enter the genre of {}: ".format(title))
    director = input("Enter the name of the director of {}: ".format(title))
    release_year = get_release_year(title)
    country = input("Enter the country of origin of {}: ".format(title))
    rating = get_rating(title)
    is_favorite = get_is_favorite(title)
    date = get_date(title)
    print(date)
    cursor.execute('''
                INSERT INTO "Movie Data" (Title, Genre, Director, "Release Year", Country, Rating, "Favorite?", "Date Watched")
                VALUES
                ('{}', '{}', '{}', {}, '{}', {}, '{}', '{}')
                '''.format(title, genre, director, release_year, country, rating, is_favorite, date))
    connection.commit()
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
        fav = input("Add {} to your favorites? (yes or no)".format(title))
        if fav != "yes" and fav!= "no":
            print("Please answer yes or no")
            continue
        else:
            if fav == "yes":
                return True
            return False

def get_date(title):
    while True:
        try:
            date = input("Enter the date you watched {} in the form of YYYY/MM/DD (leave blank if you don't know): ".format(title))
            if not date:
                return NULL
            else:
                stripped = datetime.strptime(date, '%Y/%m/%d')
                date_query = str(stripped.date())
                return date_query
        except ValueError:
            print("incorrect date format")
            continue











#importing module  
import pypyodbc  
from datetime import datetime
#creating connection Object which will contain SQL Server Connection  
#fill in your own Server and Database name
print("Loading...")
connection = pypyodbc.connect('Driver={SQL Server};Server=LAPTOP-J9R8FKKO;Database=testforproject;Trusted_Connection=yes')  
cursor = connection.cursor()
  
print("Connection Successfully Established")  

action_select()
