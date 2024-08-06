import welcome_message
from tkinter import Tk
from sign_up import first_use
from login import not_first_use
from data_correctness import cursor
import center_window
import sys
import os
from tkinter import PhotoImage
welcome_message.play()



root = Tk()
root.title('Personal_Notebook')


def get_resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



root.configure(bg='black')
root.title("Notebook.")

try :
    cursor.execute("""SELECT * FROM Users""")
except :
    pass

users = cursor.fetchall()
if users :
    center_window.center_window(root, 350, 300)
    not_first_use(root)
else :
    center_window.center_window(root, 350, 250)
    first_use(root)










