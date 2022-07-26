
def action_select():
    #print a vailable actions
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
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM "Movie Data"')

    for i in cursor:
        print(i)


def insert_movie():
    title = input("Enter the name of the movie: ")
    genre = input("Enter the genre of the movie: ")
    director = input("Enter the name of the director: ")
    release_year = get_release_year()
    print(release_year)
    country = input("Enter the country of origin of the movie: ")
    rating = get_rating()


#gets the release year and makes sure it is valid
def get_release_year():
    while True:
        try:
            year = int(input("Enter the year the movie was released: "))
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


def get_rating():
    stars = input("Enter your rating for the movie(from 0 to 10 up to one decimal place): ")
    try:
        stars = float(stars)
    except ValueError:
        print("not a number")
        get_rating()
    if stars < 0.0 or stars > 10.0:
        print("this is not a valid rating")
        get_rating()








#importing module  
import pypyodbc  
#creating connection Object which will contain SQL Server Connection  
connection = pypyodbc.connect('Driver={SQL Server};Server=LAPTOP-J9R8FKKO;Database=testforproject;Trusted_Connection=yes')  
  
print("Connection Successfully Established")  

action_select()
