import sign_up
import tkinter as tk
import forget_retrieve as forget
import data_correctness as data_c
from tkinter import messagebox
import subject_history as history
import subjects_update as s_u
import center_window

def choice_after_login(root,username) :
    for widget in root.winfo_children() :
        widget.grid_forget()

    root.destroy()
    root = tk.Tk()
    root.configure(bg='black')
    root.title(f"{username}'s Notebook")
    center_window.center_window(root, 397, 365)
    label_1 = tk.Label(root,text="\n\tChoose a function !\t\n",font=('helvetica',16,'bold'),bg='black',fg='white')
    button_insert_subject = tk.Button(root,text="New subjects",font=('helvetica',15,'bold'),
                                   relief=tk.RAISED,width=31,borderwidth=10,bg='white',fg='black',command=lambda : s_u.insert_into_subject_table(root=root,username=username))
    button_update_existing_subjects = tk.Button(root,text="Update subjects",
                                             font=('helvetica',15,'bold'),relief=tk.RAISED,width=31,borderwidth=10,
                                             bg='white',fg='black',command=lambda : s_u.display_and_update_subjects(root,username))
    button_print_history = tk.Button(root, text='Print history', bg='white', fg='black',
                                  relief=tk.RAISED, font=('helvetica', 15, 'bold'), width=31, borderwidth=10,
                                  command=lambda: history.print_history(username))
    button_delete_history = tk.Button(root, text='Delete history', bg='white', fg='black',
                                  relief=tk.RAISED, font=('helvetica', 15, 'bold'), width=31, borderwidth=10,
                                  command=lambda: history.delete_subjects_main(root,username))
    button_exit = tk.Button(root,text="Exit",font=('helvetica',15,'bold'),relief=tk.RAISED,width=31,borderwidth=10,bg='white',fg='black',command=lambda :forget.exit_program(root))

    label_1.grid(row=0)
    button_insert_subject.grid(row=1)
    button_update_existing_subjects.grid(row=2)
    button_print_history.grid(row=3)
    button_delete_history.grid(row=4)
    button_exit.grid(row=5)



def not_first_use(root) :
    for widget in root.winfo_children() :
        widget.grid_forget()

    welcome_label = tk.Label(root, text="Welcome to Studying Calendar.\nSign up for new users.\nLog in for existing accounts.\n\n",
                          font=('helvetica', 14, 'bold'), bg='black', fg='white')
    button_login = tk.Button(root, text="Login", font=('Helvetica', 15, 'bold'), fg='black', borderwidth=14, width=26,
                          height=1, command=lambda: login(root))
    button_sign_up = tk.Button(root, text="Sign up", font=('Helvetica', 15, 'bold'), fg='black', borderwidth=14, width=26,
                            height=1, command=lambda: sign_up.sign_user_up(root))
    button_exit = tk.Button(root, text="Exit", font=('Helvetica', 15, 'bold'), fg='black', borderwidth=14, width=26,
                         height=1, command= lambda :(forget.exit_program(root)))

    welcome_label.grid(row=0, columnspan=2)
    button_login.grid(row=2, columnspan=2)
    button_sign_up.grid(row=3, columnspan=2)
    button_exit.grid(row=4, columnspa=2)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.mainloop()



def login(root) :
    center_window.center_window(root, 350, 350)
    def on_click(event) :
        get_credentials(entry_1,entry_2)
    def on_click_2(event) :
        entry_2.focus()

    def get_credentials(entry_1,entry_2) :
        user_name = entry_1.get()
        pass_word = entry_2.get()
        login_user_statement = f"""SELECT * FROM "Users" WHERE USERNAME = '{user_name}' AND PASSWORD = '{pass_word}'"""
        data_c.cursor.execute(login_user_statement)
        credentials = data_c.cursor.fetchone()
        data_c.connection.commit()

        if not credentials:
            messagebox.showerror("Error","Your login credentials are not valid.\nPlease retype them.")
            entry_1.delete(0, tk.END)
            entry_2.delete(0, tk.END)
        else:
            choice_after_login(root,username=credentials[0])


    for widget in root.winfo_children():
        widget.grid_forget()


    starting_label = tk.Label(root,text='Insert your credentials\n',bg='black',fg='white',font=('helvetica',15))
    username_label = tk.Label(root,text='Username :',bg='black',fg='white',font=('helvetica',15))
    entry_1 = tk.Entry(root, width=24, borderwidth=19, font=('Helvetica', 20))
    user_password_label = tk.Label(root,text='Password :',font=('helvetica',15),bg='black',fg='white')
    entry_2 = tk.Entry(root,width=24,borderwidth=19,font=('Helvetica',20))
    entry_1.focus()
    entry_1.bind("<Return>",on_click_2)
    entry_2.bind("<Return>",on_click)
    button_enter = tk.Button(root,text='Enter',bg='black',fg='lawn green',
                          relief=tk.RAISED,font=('helvetica',16,'bold'),width=30,borderwidth=0,command=lambda :get_credentials(entry_1,entry_2))


    button_return = tk.Button(root, text='Return',
                         relief=tk.RAISED, bg='black', fg='yellow', font=('helvetica', 16, 'bold'), width=30, borderwidth=0,
                          command=lambda: not_first_use(root))
    button_exit = tk.Button(root, text='Exit',
                         relief=tk.RAISED,bg='black',fg='red', font=('helvetica', 16, 'bold'), width=30, borderwidth=0,command=lambda : forget.exit_program(root))

    starting_label.grid(row=0,columnspan=2)
    username_label.grid(row=1,columnspan=2)
    entry_1.grid(row=2,columnspan=2)
    user_password_label.grid(row=3,columnspan=2)
    entry_2.grid(row=4,columnspan=2)
    button_enter.grid(row=5,columnspan=2)
    button_return.grid(row=6,columnspan=2)
    button_exit.grid(row=7,columnspan=2)


    root.rowconfigure(0,weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)







