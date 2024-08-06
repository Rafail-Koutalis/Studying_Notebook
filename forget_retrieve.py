from tkinter import *
import os
import sys

import center_window


def forget_all(*args) :
    """makes all widgets from the tkinter window disappear, to create a new interface on the root."""
    for arg in args :
        arg.grid_forget()

def delete_digit(entry) :
    """This function doesn't allow the input of more than 2 decimal places (eg 2.41241) or other mistakes
    such as 2.3..4.21. Used in Withdraw and Deposit"""
    entry.delete(entry.index("end") - 1)


def retrieve_all(root,*args):
    for widget in root.winfo_children():
        widget.grid_forget()

    count = 0
    for i in args :
        i.grid(row=count,column=count%2)
        count +=1


def exit_program(root_2) :
    for child in root_2.winfo_children() :
        child.destroy()

    center_window.center_window(root_2,505,700)
    def destroy_new_root(event):
        root_2.destroy()

    root_2.bind("<Button>", destroy_new_root)
    root_2.bind("<Escape>", destroy_new_root)


    def get_resource_path(relative_path):
        """ Get the absolute path to the resource, works for dev and PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

        # Use the function to get the full path to the image


    filepath = get_resource_path("sleep.png")
    img = PhotoImage(file=filepath)
    image_label = Label(root_2, image=img,bg='black')
    label_1 = Label(root_2, text='\n Proud of you for studying.\n', font=('helvetica', 14, 'bold'),
                    bg='black', fg='white')
    label_2 = Label(root_2, text='\n Press anywhere on the frame to proceed.', font=('helvetica', 14, 'bold'),
                        bg='black', fg='white')
    label_1.grid(row=0)
    image_label.grid(row=1)
    label_2.grid(row=2, column=0)
    root_2.rowconfigure(0,weight=1)
    root_2.rowconfigure(1,weight=1)
    root_2.mainloop()
