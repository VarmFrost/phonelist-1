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
    
print("""
  Hallo and welcome to the phone list, the available commands/instructions are:
  ADD, DELETE, LIST, QUIT
  --------------------------
    ADD    [A] - Add a phone number
    DELETE [D] - Delete a contact
    LIST   [L] - List all phone numbers
    QUIT   [Q] - Quit the program
  --------------------------
  """)

while True: ## REPL - Read Execute Program Loop
    commandInstruction = input("Command/Instruction: ")
    if commandInstruction == "LIST" or commandInstruction == "L":
        print(read_phonelist(connectToDB))
    elif commandInstruction == "ADD" or commandInstruction == "A":
        name = input("  Name: ")
        phone = input("  Phone: ")
        add_phone(connectToDB, name, phone)
    elif commandInstruction == "DELETE" or commandInstruction == "D":
        name = input("  Name: ")
        delete_phone(connectToDB, name)
    elif commandInstruction == "QUIT" or commandInstruction == "Q":
        save_phonelist(connectToDB)
        exit()
