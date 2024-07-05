import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os

# Import customtkinter (assuming you have imported and initialized it)
import customtkinter

# Set appearance and theme (assuming customtkinter supports this)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Initialize the main application window with customtkinter
app = customtkinter.CTk()
app.wm_iconbitmap('folder_archive_zip_22613.ico')
app.title("UnZipper")
app.geometry("400x300")
app.resizable(False, False)


def file():
    # Ask user to select ZIP file
    zip_file = filedialog.askopenfilename(
        initialdir="C://",
        title="Select ZIP File",
        filetypes=(("ZIP Files", "*.zip"),)
    )
    if zip_file:
        # Ask user to select extraction directory
        extract_to = filedialog.askdirectory(
            initialdir="C://",
            title="Select Directory to Extract Files"
        )
        if extract_to:
            # Call function to extract ZIP file
            extract_zip(zip_file, extract_to)


def extract_zip(zip_file, extract_to):
    # Create a folder named after the zip file within the selected extraction directory
    zip_filename = os.path.splitext(os.path.basename(zip_file))[0]
    extract_path = os.path.join(extract_to, zip_filename)

    # Make sure the extraction directory exists
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        message = f"Successfully extracted '{os.path.basename(zip_file)}' to '{extract_path}'"
        show_message_box("Extraction Successful", message, 'info')
    except zipfile.BadZipFile:
        message = f"Error: '{os.path.basename(zip_file)}' is not a valid ZIP file."
        show_message_box("Extraction Error", message, 'error')
    except Exception as e:
        message = f"An error occurred while extracting '{os.path.basename(zip_file)}': {e}"
        show_message_box("Extraction Error", message, 'error')


def show_message_box(title, message, icon='info'):
    # Function to show a message box using tkinter's messagebox
    if icon == 'info':
        messagebox.showinfo(title, message)
    elif icon == 'warning':
        messagebox.showwarning(title, message)
    elif icon == 'error':
        messagebox.showerror(title, message)


# Create a frame for buttons (using customtkinter)
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

# Button to select ZIP file (using customtkinter)
button_1 = customtkinter.CTkButton(master=frame_1, text="Select File", command=file, fg_color="#208fff",
                                   font=("Arial", 15, 'bold'))
button_1.pack(pady=80, padx=10)

# Start the main loop
app.mainloop()
