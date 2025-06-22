import tkinter as tk
from tkinter import messagebox, simpledialog
import os

file_name = "tasks.txt"

def save_tasks():
    with open(file_name, "w") as f:
        for task in tasks:
            f.write(f"{task[0]}|{task[1]}\n")

def load_tasks():
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            for line in f:
                t = line.strip().split("|")
                if len(t) == 2:
                    tasks.append([t[0], t[1]])

def refresh():
    listbox.delete(0, tk.END)
    for task in tasks:
        icon = "✅" if task[1] == "done" else "❌"
        listbox.insert(tk.END, f"{icon} {task[0]}")

def add():
    t = entry.get().strip()
    if t:
        tasks.append([t, "not done"])
        entry.delete(0, tk.END)
        refresh(); save_tasks()

def update():
    i = listbox.curselection()
    if i:
        new = simpledialog.askstring("Update", "New task:")
        if new:
            tasks[i[0]][0] = new
            refresh(); save_tasks()

def delete():
    i = listbox.curselection()
    if i:
        tasks.pop(i[0])
        refresh(); save_tasks()

def mark_done():
    i = listbox.curselection()
    if i:
        tasks[i[0]][1] = "done"
        refresh(); save_tasks()

root = tk.Tk()
root.title("To-Do App")
root.geometry("400x400")

tasks = []
load_tasks()

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Add", command=add).pack()
tk.Button(root, text="Update", command=update).pack()
tk.Button(root, text="Delete", command=delete).pack()
tk.Button(root, text="Mark as Done", command=mark_done).pack()

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

refresh()
root.mainloop()
