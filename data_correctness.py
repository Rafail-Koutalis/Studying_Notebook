from sqlite3 import connect
from tkinter import END
connection = connect('Personal_Progress.db') #δημιουργούμε την σύνδεση με την βάση δεδομένων.
cursor = connection.cursor()

def check_entry(entry)  :
    try :
        while entry.get()[0] == " " :
            entry.delete(0)
    except :
        pass
def clear_entries (entry_1, entry_2, entry_3, entry_4) :
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_1.focus()
def data_correctness(username,password,year,uni_id) :
    cursor.execute(f"""SELECT USERNAME FROM Users WHERE USERNAME = '{username}'""")
    name_already_exists = cursor.fetchone()

    if  name_already_exists or not username:
        return 0
    elif  len(password) < 9 or not password:
        return 0
    elif  len(year) != 1 or not year.isdigit()  or not year:
        return 0
    elif not uni_id :
        return 0
    return 1

