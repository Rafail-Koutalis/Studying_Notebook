import center_window
import data_correctness as data_c
import tkinter as tk
from tkinter import messagebox

import login


#getting the column names
def get_names(username) :
    data_c.cursor.execute(f"PRAGMA table_info({username})")
    columns_info = data_c.cursor.fetchall()
    column_names = [column_info[1] for column_info in columns_info]
    return column_names

def delete_subjects_main(root,username) :
    def on_click(event) :
        returning()
    def returning() :
        login.choice_after_login(root,username)


    column_names = get_names(username)
    if len(column_names) <= 1:
        messagebox.showerror("Error","No subjects found!")

    else :
        data_c.cursor.execute(f"""SELECT * FROM {username}""")
        tuple_subject_values = data_c.cursor.fetchall()
        count_not_deleted = 0
        for tuple in tuple_subject_values :
            for subject_value in range(len(tuple)) :
                if tuple[subject_value] != "DELETED" :
                    count_not_deleted += 1

        if count_not_deleted == 1 :
            messagebox.showerror("Error","No subjects found.")
        else :
            for widget in root.winfo_children():
                widget.grid_forget()

            center_window.center_window(root, 397, 300)
            label_1 = tk.Label(root,text='Choose a function\n\n',bg='black',fg='white',font=('helvetica',19,'bold'))
            button_delete_all = tk.Button(root,text='Delete All',bg='white',fg='black',borderwidth=10,
                                       font=('helvetica',19,'bold'),width=25,command=lambda :delete_all_subjects(root,username))
            button_delete_selected = tk.Button(root, text='Delete Selected', bg='white', fg='black', borderwidth=10,width=25,
                                       font=('helvetica', 19, 'bold'),command=lambda :delete_selected_subject(root,username))
            button_return = tk.Button(root, text='Return', bg='white', fg='black', borderwidth=10,
                                       font=('helvetica', 19, 'bold'),width=25,command=lambda :returning())

            label_1.grid(row=0)
            button_delete_all.grid(row=1)
            button_delete_selected.grid(row=2)
            button_return.grid(row=3)

def delete_all_subjects(root,username) :
    column_names = get_names(username)
    for i in range(1,len(column_names)) :
        data_c.cursor.execute(f"""UPDATE {username} SET '{column_names[i]}' = 'DELETED' ;""")
        data_c.connection.commit()
    messagebox.showinfo("Success","Deletion was successful.")
    login.choice_after_login(root,username)


def delete_selected_subject(root,username) :
    def returning(root,username) :
        delete_subjects_main(root,username)
    def on_click_delete(event) :
        deletion_process()
    def deletion_process() :
        column_names = get_names(username)
        if entry_for_deletion.get() != '' :
            data_c.check_entry(entry_for_deletion)
            count_found = 0
            for i in range(1, len(column_names)):
                if entry_for_deletion.get() == column_names[i] :
                    data_c.cursor.execute(f"SELECT * FROM {username}")
                    tuple_deleted = data_c.cursor.fetchall()
                    if tuple_deleted[0][i] == 'DELETED' :
                        count_found += 1
                        messagebox.showerror("Error","Subject not found,must be already deleted")
                    else :
                        count_found += 1
                        data_c.cursor.execute(f"""UPDATE {username} SET '{column_names[i]}' = 'DELETED' ;""")
                        data_c.connection.commit()
                        messagebox.showinfo("Success", "Subject was deleted successfully.")
                        delete_subjects_main(root, username)
            if count_found == 0 :
                messagebox.showerror("Error","Subject not found.")
        else :
            messagebox.showerror("Error","No empty entries allowed.")



    for widget in root.winfo_children() :
        widget.grid_forget()

    entry_for_deletion = tk.Entry(root, font=('helvetica', 17, 'bold'),borderwidth=10,width=28)
    entry_for_deletion.focus()

    label_1 = tk.Label(root,text="\nInsert Subject for deletion!\n",bg='black',fg='white',font=('helvetica',15,'bold'))

    button_enter = tk.Button(root, text='Enter', bg='black', fg='lawn green', width=28, borderwidth=0,
                           font=('helvetica', 17, 'bold'), command=lambda: deletion_process())
    button_enter.bind("<Return>", on_click_delete)
    button_return = tk.Button(root, text='Return', bg='black', fg='yellow', width=28, borderwidth=0,
                          font=('helvetica', 17, 'bold'), command=lambda: returning(root,username))
    button_exit = tk.Button(root,text='Exit',bg='black',fg='red',width=28,borderwidth=0,font=('helvetica',17,'bold'),command=lambda :root.destroy())

    label_1.grid(row=0)
    entry_for_deletion.grid(row=1,pady=20)
    button_enter.grid(row=2)
    button_return.grid(row=3)
    button_exit.grid(row=4)


#funcs about data deletion



#funcs about printing history


def print_history(username):
    def on_click(event) :
        new_root.destroy()

    subject_names = get_names(username)

    if  len(subject_names) <= 1:
        messagebox.showerror("Error","No subjects entered yet.")

    else :
        data_c.cursor.execute(f"""SELECT * FROM {username}""")
        subject_progress_tuple = data_c.cursor.fetchall()
        subject_progress_list = []

        for tuple in subject_progress_tuple :
            for lesson in range(len(tuple)) :
                if tuple[lesson] == 'DELETED' :
                    subject_names.pop(1)
                    continue
                else :
                    subject_progress_list.append(tuple[lesson])

        if len(subject_names) == 1 :
            messagebox.showerror("Error","No subjects found.")
        else :
            new_root = tk.Tk()
            new_root.bind("<Escape>", on_click)
            new_root.title(f"{username}'s Notebook")
            new_root.configure(bg='black')
            max_height = center_window.root_size(new_root,subject_progress_list)
            max_height+=100
            new_root.geometry(f"520x{max_height}")

            canvas = tk.Canvas(new_root)
            canvas.grid(row=0, column=0, sticky="nsew")
            canvas.configure(bg='black', width=500, borderwidth=0, height=max_height)

            scrollable_frame = tk.Frame(new_root, bg='black', borderwidth=0, width=500)
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=500)

            scrollbar = tk.Scrollbar(new_root, orient="vertical", command=canvas.yview)
            scrollbar.grid(row=0, column=1, sticky="ns")
            scrollbar.bind("<>")
            canvas.configure(yscrollcommand=scrollbar.set)

            user_id = tk.Label(scrollable_frame,
                               text=f"User : {username}\n", font=("Helvetica", 23, "bold"), bg="black", fg="white")
            Lesson = tk.Label(scrollable_frame,
                              text=("Subjects :\n"), font=("Helvetica", 19, 'bold'), bg="black", fg="white")
            Progress = tk.Label(scrollable_frame, text=("Progress :\n"), font=("Helvetica", 19, 'bold'), bg="black",
                                fg="white")

            user_id.grid(row=0, columnspan=2, sticky="ew")
            Lesson.grid(row=1, column=0)
            Progress.grid(row=1, column=1)

            count_row = 3
            for value in range(1, len(subject_names)):
                if subject_progress_list[value] == 'DELETED' :
                    continue
                label_subject = tk.Label(scrollable_frame, text=str(f"{subject_names[value]}"),
                                        font=("Helvetica", 16, 'bold'),
                                        bg="black", fg="white")
                label_progress = tk.Label(scrollable_frame, text=str(f"{subject_progress_list[value]}"), font=("Helvetica", 14),
                                          bg="black",
                                          fg="white")
                label_subject.grid(row=count_row + 1, column=0, padx=10, sticky="ew")
                label_progress.grid(row=count_row + 1, column=1, padx=10, sticky="ew")
                count_row += 1

            scrollable_frame.columnconfigure(0, weight=1)
            scrollable_frame.columnconfigure(1, weight=1)

            new_button_exit = tk.Button(scrollable_frame, text="EXIT", font=('helvetica', 14, 'bold'), bg='black', fg='red',
                                        width=3, borderwidth=0, command=lambda: new_root.destroy())

            new_button_exit.grid(row=len(subject_names) + 4, columnspan=2, pady=10, sticky="ew")
            scrollable_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
            new_root.mainloop()


