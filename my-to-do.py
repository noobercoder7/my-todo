import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.configure(bg="coral")
root.geometry("300x280")
root.title("To-Do List")

my_tasks = []


def add_text():
    new_task = task_entry.get()
    if new_task:
        my_tasks.append(new_task)
        tasks_box.insert("end", new_task)
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def del_task():
    task = tasks_box.get("active")
    if task in my_tasks:
        my_tasks.remove(task)
        tasks_box.delete("active")


def del_all():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box == True:
        tasks_box.delete(0, "end")
        my_tasks.clear()


lbl_title = tk.Label(root, text="To-Do List", bg="coral",
                     font=('calibre', 18, 'bold'))
lbl_title.grid(row=0, columnspan=2, padx=10, pady=10)

task_label = tk.Label(root, text="Enter task:", bg="coral")
task_label.grid(row=1, padx=10, pady=0)

task_entry = tk.Entry(root, width=20)
task_entry.grid(row=2, padx=10, pady=5)

add_button = tk.Button(root, text="Add Task", command=add_text)
add_button.grid(row=3, padx=10, pady=5)

del_button = tk.Button(root, text="Delete Task", command=del_task)
del_button.grid(row=4, padx=10, pady=5)

del_all_button = tk.Button(root, text="Clear All", command=del_all)
del_all_button.grid(row=5, padx=10, pady=5)

exit_button = tk.Button(root, text="Exit", command=exit)
exit_button.grid(row=6, padx=10, pady=5)

tasks_box = tk.Listbox(root, selectmode=tk.SINGLE)
tasks_box.grid(row=1, column=1, rowspan=6,
               padx=10, pady=10)


root.mainloop()
