
def action_select():
    #print a vailable actions
    print("OPTIONS: insert, close")

    #user selects an action
    action = input("Select option: ")

    #insert a new movie into database
    if action == ("insert"):
        insert_movie()

    #closes the connection
    elif action == ("close"):
        connection.close()

    else:
        print("not a valid option, please try again")
        action_select()


def insert_movie():
    title = input("Enter the name of the movie: ")
    print(title)





#importing module  
import pypyodbc  
#creating connection Object which will contain SQL Server Connection  
connection = pypyodbc.connect('Driver={SQL Server};Server=LAPTOP-J9R8FKKO;Database=testforproject;Trusted_Connection=yes')  
  
print("Connection Successfully Established")  

cursor = connection.cursor()
cursor.execute('SELECT * FROM "Movie Data"')

for i in cursor:
    print(i)

action_select()

#closing connection  
connection.close() 