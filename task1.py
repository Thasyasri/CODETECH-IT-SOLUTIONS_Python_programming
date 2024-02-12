import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, name, priority=0, due_date=None, category=None, notes=None, completed=False):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.category = category
        self.notes = notes
        self.completed = completed

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Initialize variables
        self.tasks = []
        self.sort_by_completion = False
        self.filter_completed_tasks = False

        # Configure styles
        self.configure_styles()

        # Create GUI elements
        self.create_widgets()

    def configure_styles(self):
        self.root.configure(bg="#E8E8E8")
        self.frame_style = {"bg": "#E8E8E8", "padx": 20, "pady": 10}
        self.font_style = ("Arial", 12)

    def create_widgets(self):
        # Add a frame for better organization
        self.frame = tk.Frame(self.root, **self.frame_style)
        self.frame.pack()

        # Create and place GUI elements
        self.task_entry = tk.Entry(self.frame, width=40, font=self.font_style)
        self.task_entry.grid(row=0, column=0, padx=10, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task, font=self.font_style)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_list = tk.Listbox(self.frame, width=40, height=10, selectmode=tk.SINGLE, font=self.font_style)
        self.task_list.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.delete_label = tk.Label(self.frame, text="Enter Task Number to Delete:", **self.frame_style, font=self.font_style)
        self.delete_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.task_delete_entry = tk.Entry(self.frame, width=10, font=self.font_style)
        self.task_delete_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task, font=self.font_style)
        self.delete_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.sort_button = tk.Button(self.frame, text="Sort Tasks", command=self.sort_tasks, font=self.font_style)
        self.sort_button.grid(row=4, column=0, padx=5, pady=5)

        self.filter_button = tk.Button(self.frame, text="Filter Tasks", command=self.filter_tasks, font=self.font_style)
        self.filter_button.grid(row=4, column=1, padx=5, pady=5)

        self.complete_button = tk.Button(self.frame, text="Mark Complete", command=self.mark_complete, font=self.font_style)
        self.complete_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    def add_task(self):
        task_name = self.task_entry.get()
        if task_name:
            self.tasks.append(Task(name=task_name))
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
            messagebox.showinfo("Task Added", f"Task '{task_name}' added to the list.")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            task_index = int(self.task_delete_entry.get()) - 1
            if 0 <= task_index < len(self.tasks):
                del self.tasks[task_index]
                self.update_task_list()
                messagebox.showinfo("Task Deleted", f"Task {task_index + 1} has been removed.")
            else:
                messagebox.showwarning("Warning", f"Task #{task_index + 1} was not found.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid task number.")

    def sort_tasks(self):
        self.sort_by_completion = not self.sort_by_completion
        self.tasks.sort(key=lambda x: x.completed)
        self.update_task_list()

    def filter_tasks(self):
        self.filter_completed_tasks = not self.filter_completed_tasks
        self.update_task_list()

    def mark_complete(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            task.completed = not task.completed
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            if not self.filter_completed_tasks or not task.completed:
                status = "[✔️]" if task.completed else "[ ]"
                self.task_list.insert(tk.END, f"{index}. {status} {task.name}")

# Create main application window
root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
