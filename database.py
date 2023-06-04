import os.path
import sqlite3 as sl
userchoice = 0

def db_initialization():
    global con 
    db_check = os.path.exists('login.db') #Cheaks the local directory for the database. Returns true or false based on the finding
    #If database check finds a database it runs the following if statement
    if db_check == 1:
        print('db in place')
        con = sl.connect('login.db')
        return con

    #if database check does not find a database, the following code is run
    if db_check == 0:
        con = sl.connect('login.db') # This line creates the actual database
        with con:
            #This section of code creates tables in the database
            con.execute("""
                        CREATE TABLE USER (
                            name TEXT PRIMARY KEY,
                            password TEXT,
                            level INTEGER
                            );
                        """)
            con.execute("""
                        CREATE TABLE CUSTOMER (
                            phoneNumber TEXT PRIMARY KEY,
                            name TEXT
                            );
                        """)
        #Once the database and tables have been made, the database creates a admin level account for the user
        con.commit()
    return con
#------------------------------------------------------------------------------------------------------------------


#Database data reading and manipulation
#The following fuctions relate to manipulating, adding and deleting data within the database
#------------------------------------------------------------------------------------------------------------------
def create_user():
    print("Create user")
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")
    level = input("Please enter security level: ")

    con.execute(f"INSERT INTO USER VALUES ('{username}','{password}', '{level}')")
    con.commit()
    print("User Created")
    return

def create_customer():
    print("Create customer")
    cust_number = input("Please enter customer number: ")
    cust_name = input("Please enter customer phone name: ")

    con.execute(f"INSERT INTO CUSTOMER VALUES ('{cust_number}','{cust_name}')")
    con.commit()
    print("Customer Created")
    return


def update_user():
    oldusername = input("Please enter old username: ")
    username = input("Please enter new a username: ")
    password = input("Please enter new a password: ")
    level = input("Please enter a new security level: ")

    query = "UPDATE USER SET name = ?, password = ?, level = ? WHERE name = ?"
    con.execute(query, (username, password, level, oldusername))

    con.commit()

def update_customer():
    oldname = input("Please enter old customer number: ")
    cust_name = input("Please enter a new customer name: ")
    cust_number = input("Please enter a new customer phone number: ")

    query = "UPDATE CUSTOMER SET phoneNumber = ?, name = ? WHERE phoneNumber = ?"
    con.execute(query, (cust_number, cust_name, oldname))
    con.commit()

def delete_user():
    username = input("Please enter a username to delete: ")
    query = "DELETE FROM USER WHERE name = ?"
    con.execute(query, (username,))
    con.commit()

def delete_customer():
    cust_name = input("Please enter customer number to delete: ")
    query = "DELETE FROM CUSTOMER WHERE phoneNumber = ?"
    con.execute(query, (cust_name,))
    con.commit()

def get_user():
    info = con.execute(f'SELECT * FROM USER')
    con.commit()
    for line in info:
        print(f'Name: {line[0]}')
        print(f'Password: {line[1]}')
        print(f'Security: {line[2]}')
        print('\n')

def get_customer():
    info = con.execute(f'SELECT * FROM CUSTOMER')
    con.commit()
    for line in info:
        print(f'Phone: {line[0]}')
        print(f'Name: {line[1]}')
        print('\n')


db_initialization()

while userchoice != 9:   
    print('1. Create User')
    print('2. Create Customer')
    print('3. Update User')
    print('4. Update Customer')
    print('5. Delete User')
    print('6. Delete Customer')
    print('7. Get User')
    print('8. Get Customer')
    print('9. Exit')
    userchoice = int(input('Please enter your choice: '))
    print('\n')
    if userchoice == 1:
        create_user()
    if userchoice == 2:
        create_customer()
    if userchoice == 3:
        update_user()
    if userchoice == 4:
        update_customer()
    if userchoice == 5:
        delete_user()
    if userchoice == 6:
        delete_customer()
    if userchoice == 7:
        get_user()
    if userchoice == 8:
        get_customer()
