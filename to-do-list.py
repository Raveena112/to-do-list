import tkinter as tk
from tkinter import ttk, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        
        self.tasks = []
        
        self.create_widgets()

    def create_widgets(self):
        # Frame for the input box and add button
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        self.task_var = tk.StringVar()
        self.task_entry = ttk.Entry(input_frame, textvariable=self.task_var, width=30)
        self.task_entry.grid(row=0, column=0, padx=10)

        add_button = ttk.Button(input_frame, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, height=15, width=50, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Frame for the action buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        delete_button = ttk.Button(button_frame, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=0, column=0, padx=10)

        clear_button = ttk.Button(button_frame, text="Clear All Tasks", command=self.clear_all_tasks)
        clear_button.grid(row=0, column=1, padx=10)

    def add_task(self):
        task = self.task_var.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def clear_all_tasks(self):
        self.tasks.clear()
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
