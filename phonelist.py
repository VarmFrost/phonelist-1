#import sqlite3
#connectToDB = sqlite3.connect("phone.db")

import psycopg2
connectToDB = psycopg2.connect(
               host="localhost",
               database="phone", 
               user="phone", 
               password="abc123") 

def read_phonelist(aConnection):
    cursorDB = aConnection.cursor()
    cursorDB.execute("SELECT * FROM phonelist;")
    rows = cursorDB.fetchall()
    cursorDB.close()
    return rows

def add_phone(aConnection, aName, aPhone):
    cursorDB = aConnection.cursor()
    cursorDB.execute(f"INSERT INTO phonelist VALUES ('{aName}', '{aPhone}');")
    print(str(aName) + " added!")
    #print("{} added!".format(aName))
    cursorDB.close()
    
def delete_phone(aConnection, aName):
    cursorDB = aConnection.cursor()
    cursorDB.execute(f"DELETE FROM phonelist WHERE name = '{aName}';")
    print(str(aName) + " deleted!")
    #print("{} deleted!".format(aName))
    cursorDB.close()
    
def save_phonelist(aConnection):
    cursorDB = aConnection.cursor()
    try:
        cursorDB.execute("COMMIT;")
        print("Committing all changes to the database and quitting! Good bye!")
    except:
        print("No changes!")
        
    cursorDB.close()
    
print("""Welcome to the phone list, the following commands/instructions are available:
    LIST, ADD, DELETE, QUIT!""")

while True: ## REPL - Read Execute Program Loop
    commandInstruction = input("Command/Instruction: ")
    if commandInstruction == "LIST":
        print(read_phonelist(connectToDB))
    elif commandInstruction == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        add_phone(connectToDB, name, phone)
    elif commandInstruction == "DELETE":
        name = input("  Name: ")
        delete_phone(connectToDB, name)
    elif commandInstruction == "QUIT":
        save_phonelist(connectToDB)
        exit()
