import tkinter as tk
from tkinter import messagebox
import os

# --- 1. DATA MODELS (Classes & Objects) ---

class User:
    def __init__(self, name):
        self.name = name

class Post:
    def __init__(self, user, title, content):
        self.user = user
        self.title = title
        self.content = content
        # Format: username_title.txt
        self.filename = f"{self.user.name}_{self.title}.txt"

    def save_to_file(self):
        """File Handling: Writing to a file"""
        with open(self.filename, "w") as f:
            f.write(f"Author: {self.user.name}\n")
            f.write(f"Title: {self.title}\n")
            f.write("-" * 20 + "\n")
            f.write(self.content)

# --- 2. THE APPLICATION CLASS (GUI & Logic) ---

class MiniBlogApp:
    def __init__(self, window):
        self.window = window
        self.window.title("MiniBlog Desktop")
        self.window.geometry("500x600")

        # --- GUI Widgets ---
        tk.Label(window, text="Username:").pack(pady=5)
        self.name_entry = tk.Entry(window, width=40)
        self.name_entry.pack()

        tk.Label(window, text="Post Title:").pack(pady=5)
        self.title_entry = tk.Entry(window, width=40)
        self.title_entry.pack()

        tk.Label(window, text="Post Content:").pack(pady=5)
        self.content_text = tk.Text(window, width=40, height=8)
        self.content_text.pack()

        # Save Button
        self.save_btn = tk.Button(window, text="Save Post", command=self.handle_save, bg="#4CAF50", fg="white")
        self.save_btn.pack(pady=10)

        # Listbox for viewing
        tk.Label(window, text="Saved Posts List:").pack(pady=5)
        self.post_listbox = tk.Listbox(window, width=50, height=6)
        self.post_listbox.pack()

        # View Button
        self.view_btn = tk.Button(window, text="View Selected Post", command=self.handle_view, bg="#2196F3", fg="white")
        self.view_btn.pack(pady=5)

        self.refresh_list()

    # --- Actions ---

    def handle_save(self):
        """Exception Handling for input and saving"""
        name = self.name_entry.get().strip()
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()

        if not name or not title or not content:
            messagebox.showwarning("Warning", "Please fill in all fields!")
            return

        try:
            # Creating Objects from Classes
            current_user = User(name)
            new_post = Post(current_user, title, content)
            
            # File Handling: Save
            new_post.save_to_file()
            
            messagebox.showinfo("Success", f"Saved as {new_post.filename}")
            self.refresh_list()
        except Exception as e:
            messagebox.showerror("System Error", f"Could not save: {e}")

    def handle_view(self):
        """File Handling: Reading from a file"""
        try:
            selection = self.post_listbox.curselection()
            if not selection:
                raise ValueError("No post selected!")

            filename = self.post_listbox.get(selection[0]) + ".txt"

            with open(filename, "r") as f:
                data = f.read()

            self.content_text.delete("1.0", tk.END)
            self.content_text.insert("1.0", data)

        except ValueError as ve:
            messagebox.showwarning("Selection Error", ve)
        except FileNotFoundError:
            messagebox.showerror("Error", "File has been moved or deleted!")

    def refresh_list(self):
        self.post_listbox.delete(0, tk.END)
        for file in os.listdir("."):
            if "_" in file and file.endswith(".txt"):
                self.post_listbox.insert(tk.END, file.replace(".txt", ""))

# --- 3. START THE APP ---
if __name__ == "__main__":
    root = tk.Tk()
    app = MiniBlogApp(root)
    root.mainloop()