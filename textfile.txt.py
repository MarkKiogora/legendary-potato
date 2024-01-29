import json
import tkinter as tk
from tkinter import messagebox

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = {}
    return tasks

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks, task_name, listbox):
    tasks[task_name] = False
    listbox.insert(tk.END, f"{task_name} - Not Completed")
    messagebox.showinfo("Task Added", f'Task "{task_name}" added successfully!')

def remove_task(tasks, task_name, listbox):
    if task_name in tasks:
        del tasks[task_name]
        listbox.delete(tk.ACTIVE)
        messagebox.showinfo("Task Removed", f'Task "{task_name}" removed successfully!')
    else:
        messagebox.showwarning("Task Not Found", f'Task "{task_name}" not found.')

def mark_task_complete(tasks, task_name, listbox):
    if task_name in tasks:
        tasks[task_name] = True
        index = listbox.curselection()
        listbox.delete(index)
        listbox.insert(tk.END, f"{task_name} - Completed")
        messagebox.showinfo("Task Completed", f'Task "{task_name}" marked as completed!')
    else:
        messagebox.showwarning("Task Not Found", f'Task "{task_name}" not found.')

def main():
    tasks = load_tasks()

    root = tk.Tk()
    root.title("To-Do List Application")
    root.configure(bg="#e0e0e0")  # Set background color

    # Entry and label frame
    entry_frame = tk.Frame(root, bg="#e0e0e0")
    entry_frame.pack(pady=10)

    label = tk.Label(entry_frame, text="Enter task name:", bg="#e0e0e0")
    label.pack(side=tk.LEFT)

    entry = tk.Entry(entry_frame, bg="white")
    entry.pack(side=tk.LEFT)

    # Listbox frame
    listbox_frame = tk.Frame(root, bg="#e0e0e0")
    listbox_frame.pack()

    listbox = tk.Listbox(listbox_frame, selectbackground="#a6a6a6")
    listbox.pack()

    # Populate listbox with existing tasks
    for task, status in tasks.items():
        listbox.insert(tk.END, f"{task} - {'Completed' if status else 'Not Completed'}")

    # Button frame
    button_frame = tk.Frame(root, bg="#e0e0e0")
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Add Task", command=lambda: add_task(tasks, entry.get(), listbox), bg="#4caf50", fg="white")
    add_button.pack(side=tk.LEFT, padx=5)

    remove_button = tk.Button(button_frame, text="Remove Task", command=lambda: remove_task(tasks, entry.get(), listbox), bg="#f44336", fg="white")
    remove_button.pack(side=tk.LEFT, padx=5)

    complete_button = tk.Button(button_frame, text="Mark as Completed", command=lambda: mark_task_complete(tasks, entry.get(), listbox), bg="#2196f3", fg="white")
    complete_button.pack(side=tk.LEFT, padx=5)

    save_button = tk.Button(root, text="Save and Exit", command=lambda: [save_tasks(tasks), root.destroy()], bg="#607d8b", fg="white")
    save_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
