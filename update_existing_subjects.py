import data_correctness as data_c
from tkinter import messagebox
import  tkinter as tk
import center_window

def destroy_old_root(windows):
    try:
        if windows:
            windows[0].destroy()
            windows.pop(0)
    except:
        pass

def update_existing_subjects(username,subject,windows) :
    def on_click(event) :
        on_click_2()
    def on_click_2() :
        data_c.check_entry(entry)
        update_subject(root=new_root,username=username,entry=entry,subject=subject)

    def update_subject(root, username, entry, subject):
        if entry.get():
            try:
                if entry.get().isdigit() and int(entry.get()) > 34:
                    messagebox.showerror("Error",
                                         "The biggest number you can enter is 34.\n(no more weeks in an academic year)")
                    root.focus()
                else:
                   data_c.cursor.execute(f"UPDATE {username} SET '{subject}' = {entry.get()};")
                   data_c.connection.commit()
                   messagebox.showinfo("Success!", "Progress successfully submitted!\nPress Exit/Escape.")
                   root.destroy()
            except:
                if not entry.get().isdigit():
                    messagebox.showerror("Error", "Invalid entry,only numbers allowed.")
                    entry.delete(0, tk.END)
                    root.focus()
                elif "." in entry.get():
                    messagebox.showerror("Error", "Only integers allowed.")
                    root.focus()
        else:
            messagebox.showerror("Error", "Empty entries not allowed.")
            root.focus()





    new_root = tk.Toplevel()
    new_root.focus()
    destroy_old_root(windows)
    windows.append(new_root)


    new_root.configure(bg="black")
    center_window.center_window(new_root,317,250)
    label_1 = tk.Label(new_root,text=f"\nSubmit progress for :\n{subject} \n",bg='black',fg='white',font=('helvetica',15,'bold'))
    empty_label = tk.Label(new_root,text="",bg='black')
    entry= tk.Entry(new_root,width=26,borderwidth=12,relief=tk.RAISED,font=('helvetica',15,'bold'))
    entry.focus_set()
    exit_button = tk.Button(new_root,text='Exit',bg='black',fg='yellow',font=('helvetica',15,'bold'),
                              relief=tk.RAISED,width=26,borderwidth=0,command=lambda : destroy_old_root(windows))
    enter_button = tk.Button(new_root, text='Enter', bg='black', fg='green',font=('helvetica',15,'bold'), relief=tk.RAISED, width=26, borderwidth=0,command=lambda:on_click_2())


    entry.bind("<Return>",on_click)

    label_1.grid(row=0)
    entry.grid(row=1)
    empty_label.grid(row=2)
    enter_button.grid(row=3)
    exit_button.grid(row=4)
    new_root.mainloop()