import forget_retrieve as forget
import tkinter as tk
import data_correctness as data_c
from tkinter import messagebox
import center_window
import login
import update_existing_subjects as update


#functions for users
#======================================================================================================================#
def create_user_table():
    try:
        data_c.cursor.execute(f"""CREATE TABLE "Users" 
        ("USERNAME" TEXT NOT NULL,
        "PASSWORD" TEXT NOT NULL,
        "YEAR" INT NOT NULL,
        "UNI_ID" TEXT NOT NULL);""")
    except:
        pass
def profile_creation(entry_1, entry_2, entry_3, entry_4):
    data_c.cursor.execute(
        """INSERT INTO [Users] (USERNAME, PASSWORD, YEAR ,UNI_ID)
            VALUES (?, ?, ?, ?);""",
        (entry_1, entry_2, entry_3, entry_4,)
    )
    username = entry_1
    data_c.cursor.execute(f"""CREATE TABLE "{username}" 
            ("USERNAME" TEXT NOT NULL);""")
    data_c.connection.commit()
    data_c.cursor.execute(
        f"""INSERT INTO [{username}] (USERNAME)
                    VALUES (?);""",
        (username,))
    data_c.connection.commit()
    messagebox.showinfo("Success", 'Successful sign up.\nYou will be redirected soon.')




#functions for subjects
#======================================================================================================================#




#user enters new subjects in the table
def insert_into_subject_table(root,username) :
    center_window.center_window(root,401,290)
    def on_click_1():
        data_c.check_entry(entry)
        if entry.get() != '' :
            lesson = entry.get().lower()
            try:
                data_c.cursor.execute(f'ALTER TABLE "{username}" ADD COLUMN "{lesson}" TEXT')
                data_c.connection.commit()
                entry.delete(0, tk.END)
                messagebox.showinfo("Success","Successful insert!\nData saved!")
            except :
                entry.delete(0, tk.END)
                messagebox.showerror("Error","Subject already exists.")
        else :
            messagebox.showerror("Error","Empty entries not allowed")
    def on_click_2(event):
        on_click_1()



    for widget in root.winfo_children() :
        widget.grid_forget()

    root.title(f"{username}'s Notebook")
    root.configure(bg='black')

    label_1 = tk.Label(root,text="\nInsert the subjects' IDs you attend.\n\n",font=('helvetica',15,'bold'),bg='black',fg='white')

    entry = tk.Entry(root, width=20, borderwidth=4, font=('Helvetica', 20))
    entry.bind("<Return>", on_click_2)
    entry.focus()
    button_enter = tk.Button(root,text="Enter",font=('helvetica',17,'bold'),height=1,bg='black',fg='lawngreen',borderwidth=2,width=28,command=lambda :on_click_1())
    button_return = tk.Button(root,text="Return",font=('helvetica',17,'bold'),height=1,bg='black',fg='gold',borderwidth=2,width=28,command=lambda : login.choice_after_login(root,username))
    button_exit = tk.Button(root,text="Exit",font=('helvetica',17,'bold'),height=1,bg='black',fg='red',width=28,borderwidth=2,command=lambda : forget.exit_program(root))


    label_1.grid(row=0)
    entry.grid(row=1)
    button_enter.grid(row=2)
    button_return.grid(row=3)
    button_exit.grid(row=4)

    root.rowconfigure(0,weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)

    root.mainloop()


def display_and_update_subjects(root, username):
    def destroy_root(event) :
        forget.exit_program(root)


    root.bind("<Escape>", destroy_root)
    data_c.cursor.execute(f"PRAGMA table_info({username})")
    column_info = data_c.cursor.fetchall()
    data_c.connection.commit()

    column_names = [row[1] for row in column_info]
    column_names.pop(0)


    if len(column_names) == 0 :
        messagebox.showerror("Error","No subjects found.")

    else:
        for widget in root.winfo_children():
            widget.grid_forget()
        center_window.root_size(root, column_names)
        # Create canvas and configure its size
        canvas = tk.Canvas(root)
        max_height = root.winfo_height()
        canvas.config(height=max_height)
        canvas.grid(row=0, column=0, sticky="nsew")
        canvas.configure(bg='black')

        scrollable_frame = tk.Frame(canvas)
        scrollable_frame.configure(height=max_height)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview,bg="black")
        scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=scrollbar.set)

        label = tk.Label(scrollable_frame, text='Choose a subject to update :\n\n', bg='black', fg='white',
                      font=('helvetica', 14, 'bold'))

        button_return = tk.Button(scrollable_frame, text='Return', font=('Helvetica', 16, 'bold'), bg='black', fg='gold',
                               borderwidth=5, width=28, height=1,
                               command=lambda: login.choice_after_login(root=root, username=username))
        button_exit = tk.Button(scrollable_frame, text='Exit', font=('Helvetica', 16, 'bold'), bg='black', fg='red',
                             borderwidth=5, width=28, height=1, command=lambda: forget.exit_program(root))

        label.grid(row=0, sticky="ew")
        button_return.grid(row=1,sticky="ew")
        count_grid = 2

        windows = [] #list for all roots
        for i in range(0, len(column_names)):
            button = tk.Button(scrollable_frame, text=column_names[i], font=('Helvetica', 16, 'bold'), relief=tk.RAISED,
                               bg='black', fg='white', height=1, borderwidth=5, width=28,
                               command=lambda col = column_names[i]: update.update_existing_subjects(username=username,subject=col,windows=windows))
            button.grid(row=count_grid, columnspan=2, sticky="ew")
            count_grid += 1

        button_exit.grid(row=count_grid+1, sticky="ew")
        scrollable_frame.update_idletasks()
        # Configure the canvas scroll region
        canvas.config(scrollregion=canvas.bbox("all"))
        # Configure all rows and columns to have equal weight
        for i in range(count_grid):
            scrollable_frame.grid_rowconfigure(i, weight=1)



