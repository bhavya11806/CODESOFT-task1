import tkinter as tk
from tkinter import messagebox

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks, start=1):
        status = "[✔] " if task["completed"] else "[ ] "
        listbox.insert(tk.END, f"{idx}. {status}{task['title']}")

def add_task():
    title = entry.get()
    if title:
        tasks.append({"title": title, "completed": False})
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty.")

def mark_complete():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        tasks[idx]["completed"] = True
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Select a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        tasks.pop(idx)
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Select a task.")

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=5)

complete_button = tk.Button(root, text="Mark Complete", command=mark_complete)
complete_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

root.mainloop()

