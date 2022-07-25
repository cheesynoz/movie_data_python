
#importing module  
import pypyodbc  
#creating connection Object which will contain SQL Server Connection  
connection = pypyodbc.connect('Driver={SQL Server};Server=LAPTOP-J9R8FKKO;Database=testforproject;Trusted_Connection=yes')  
  
print("Connection Successfully Established")  

cursor = connection.cursor()
cursor.execute('SELECT * FROM "Movie Data"')

for i in cursor:
    print(i)
  
#closing connection  
connection.close() 