import subjects_update as s_u
import tkinter as tk
from tkinter import messagebox
import forget_retrieve as forget
import data_correctness as data_c
import center_window


def first_use(root) :
    welcome_label = tk.Label(root, text="Welcome to Studying Calendar.\nWe notice its your first time using it.\nPlease sign up.\n\n",
                          font=('helvetica', 14, 'bold'), bg='black', fg='white')
    button_sign_up = tk.Button(root, text="Sign up", font=('Helvetica', 15, 'bold'), fg='black', borderwidth=16, width=26,
                            height=1, command=lambda: sign_user_up(root))
    button_exit = tk.Button(root, text="Exit", font=('Helvetica', 14, 'bold'), fg='black', borderwidth=16, width=26,
                         height=1, command=lambda: (forget.exit_program(root)))

    welcome_label.grid(row=0, columnspan=2)
    button_sign_up.grid(row=1, column=0)
    button_exit.grid(row=2, column=0)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.mainloop()
def sign_user_up(root) :
    def update_database(root,entry_1,entry_2,entry_3,entry_4) :

        if data_c.data_correctness(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get()) == 0 :
            messagebox.showerror("Error","Invalid input.\n\nRequirements :\n\n->Password no less than 9 characters.\n"
                                         "->Username must be unique.\n->Year must be between 1 and 4.\n->No empty boxes allowed.")
            data_c.clear_entries(entry_1,entry_2,entry_3,entry_4)
        else :
            root.unbind("<Return>")
            s_u.profile_creation(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get())
            s_u.insert_into_subject_table(root=root,username=entry_1.get())


    def on_click(event) :
        update_database(root,entry_1,entry_2,entry_3,entry_4)

    s_u.create_user_table()

    for widget in root.winfo_children() :
        widget.grid_forget()


    center_window.center_window(root,401,550)
    starting_label = tk.Label(root, text='Insert your credentials\n', bg='black', fg='white', font=('helvetica', 15))
    username_label = tk.Label(root, text='Username :', bg='black', fg='white', font=('helvetica', 15))
    entry_1 = tk.Entry(root, width=24, borderwidth=19, font=('Helvetica', 20))
    entry_1.focus()
    user_password_label = tk.Label(root, text='Password :', font=('helvetica', 15), bg='black', fg='white')
    entry_2 = tk.Entry(root, width=24, borderwidth=19, font=('Helvetica', 20))
    user_id = tk.Label(root, text='Year of studies :', font=('helvetica', 15), bg='black', fg='white')
    entry_3 = tk.Entry(root, width=24, borderwidth=19, font=('Helvetica', 20))
    user_year_in_uni = tk.Label(root, text='Uni_id :', font=('helvetica', 15), bg='black', fg='white')
    entry_4 = tk.Entry(root, width=24, borderwidth=19, font=('Helvetica', 20))


    button_enter = tk.Button(root, text='Enter', bg='black', fg='white', relief=tk.RAISED, font=('helvetica', 16, 'bold'),
                          width=15, borderwidth=0, height=2,
                          command=lambda: update_database(root,entry_1,entry_2,entry_3,entry_4))
    root.bind("<Return>",on_click)

    button_exit = tk.Button(root, text='Exit', relief=tk.RAISED, bg='black', fg='white', font=('helvetica', 16, 'bold'),
                         width=15, borderwidth=0, height=2, command=lambda: forget.exit_program(root))

    starting_label.grid(row=0, columnspan=2)
    username_label.grid(row=1, columnspan=2)
    entry_1.grid(row=2, columnspan=2)
    user_password_label.grid(row=3, columnspan=2)
    entry_2.grid(row=4, columnspan=2)
    user_id.grid(row=5,columnspan=2)
    entry_3.grid(row=6,columnspan=2)
    user_year_in_uni.grid(row=7,columnspan=2)
    entry_4.grid(row=8,columnspan=2)
    button_enter.grid(row=9, column=0)
    button_exit.grid(row=9, column=1)

