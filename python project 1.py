from tkinter import *

# Window
root = Tk()
root.title("Aesthetic To Do List")
root.geometry("500x600")
root.config(bg="#f8e8ee")   # soft pink background

# Heading
title = Label(
    root,
    text="TO DO LIST ✨",
    font=("Times New Roman", 28, "bold"),
    bg="#f8e8ee",
    fg="#5c374c"
)
title.pack(pady=20)

# Entry Box
task_entry = Entry(
    root,
    font=("Arial", 16),
    width=25,
    bd=0,
    bg="white",
    fg="#5c374c"
)
task_entry.pack(pady=10, ipady=8)

# Listbox Frame
frame = Frame(root, bg="#f8e8ee")
frame.pack(pady=20)

# Scrollbar
scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)

# Task List
task_list = Listbox(
    frame,
    font=("Arial", 14),
    width=30,
    height=12,
    bg="white",
    fg="#5c374c",
    bd=0,
    yscrollcommand=scroll.set,
    selectbackground="#d291bc",
    activestyle="none"
)

task_list.pack()
scroll.config(command=task_list.yview)

# Add Task Function
def add_task():
    task = task_entry.get()

    if task != "":
        task_list.insert(END, "✦ " + task)
        task_entry.delete(0, END)

# Delete Task Function
def delete_task():
    selected = task_list.curselection()

    if selected:
        task_list.delete(selected)

# Buttons Frame
btn_frame = Frame(root, bg="#f8e8ee")
btn_frame.pack(pady=10)

# Add Button
add_btn = Button(
    btn_frame,
    text="Add Task",
    font=("Arial", 12, "bold"),
    bg="#d291bc",
    fg="white",
    padx=15,
    pady=5,
    bd=0,
    command=add_task
)
add_btn.grid(row=0, column=0, padx=10)

# Delete Button
delete_btn = Button(
    btn_frame,
    text="Delete",
    font=("Arial", 12, "bold"),
    bg="#5c374c",
    fg="white",
    padx=15,
    pady=5,
    bd=0,
    command=delete_task
)
delete_btn.grid(row=0, column=1, padx=10)

# Run Window
root.mainloop()