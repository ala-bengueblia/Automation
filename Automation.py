import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog, ttk

# Function to automate file organization with progress bar
def organize_files():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        file_types = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif'],
            'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
            'Videos': ['.mp4', '.avi', '.mkv'],
            'Music': ['.mp3', '.wav'],
            'Archives': ['.zip', '.rar'],
        }

        total_files = len(os.listdir(folder_selected))
        progress['maximum'] = total_files
        progress.start()

        for folder_name, extensions in file_types.items():
            folder_path = os.path.join(folder_selected, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            for file_name in os.listdir(folder_selected):
                file_ext = os.path.splitext(file_name)[1]
                if file_ext in extensions:
                    shutil.move(os.path.join(folder_selected, file_name), folder_path)
                    progress.step(1)
                    root.update_idletasks()

        progress.stop()
        progress['value'] = 0
        messagebox.showinfo("Success", "Files organized successfully!")

# Function to clear the organized folders with progress bar
def clear_organized_files():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        total_folders = len(os.listdir(folder_selected))
        progress['maximum'] = total_folders
        progress.start()

        for folder_name in os.listdir(folder_selected):
            folder_path = os.path.join(folder_selected, folder_name)
            if os.path.isdir(folder_path):
                shutil.rmtree(folder_path)
                progress.step(1)
                root.update_idletasks()

        progress.stop()
        progress['value'] = 0
        messagebox.showinfo("Success", "Organized folders cleared!")

# Create the main window
root = tk.Tk()
root.title("Automation with Python Scripts")
root.geometry("600x500")
root.config(bg="#1C2833")

# Add a title label with dynamic color
title_label = tk.Label(root, text="File Organizer", font=("Arial", 28, "bold"), fg="#F7DC6F", bg="#1C2833")
title_label.pack(pady=20)

# Function to add hover effects on buttons
def on_enter(e):
    e.widget.config(bg="#76D7C4", fg="#154360")
def on_leave(e):
    e.widget.config(bg="#3498DB", fg="white")

# Create buttons with hover effects
organize_button = tk.Button(root, text="Organize Files", command=organize_files, font=("Arial", 16, "bold"), bg="#3498DB", fg="white", padx=15, pady=10)
organize_button.pack(pady=15)
organize_button.bind("<Enter>", on_enter)
organize_button.bind("<Leave>", on_leave)

clear_button = tk.Button(root, text="Clear Organized Folders", command=clear_organized_files, font=("Arial", 16, "bold"), bg="#3498DB", fg="white", padx=15, pady=10)
clear_button.pack(pady=15)
clear_button.bind("<Enter>", on_enter)
clear_button.bind("<Leave>", on_leave)

# Add a progress bar for better user feedback
progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=400, mode='determinate')
progress.pack(pady=20)

# Add an exit button with hover effect
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 16, "bold"), bg="#E74C3C", fg="white", padx=15, pady=10)
exit_button.pack(pady=20)
exit_button.bind("<Enter>", lambda e: exit_button.config(bg="#C0392B"))
exit_button.bind("<Leave>", lambda e: exit_button.config(bg="#E74C3C"))

root.mainloop()
