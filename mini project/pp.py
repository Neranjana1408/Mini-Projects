import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os 

def submit_profile():
    name = name_entry.get()
    age = age_entry.get()
    sex = sex_var.get()
    height = height_entry.get()
    weight = weight_entry.get()
    os.system('python bmi.py')
    
def log_out():
    root.destroy()

   

# Create the main window
root = tk.Tk()
root.geometry('925x500+300+200')
root.title("Profile Page")

# Set the background color to light blue
root.configure(bg="#ADD8E6")

label_name = ttk.Label(root, text="Name:", font=("Helvetica", 12), background="#ADD8E6")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="E")
name_entry = ttk.Entry(root, width=30, font=("Helvetica", 12))
name_entry.grid(row=0, column=1, padx=10, pady=5)

label_age = ttk.Label(root, text="Age:", font=("Helvetica", 12), background="#ADD8E6")
label_age.grid(row=1, column=0, padx=10, pady=5, sticky="E")
age_entry = ttk.Entry(root, width=30, font=("Helvetica", 12))
age_entry.grid(row=1, column=1, padx=10, pady=5)

label_sex = ttk.Label(root, text="Sex:", font=("Helvetica", 12), background="#ADD8E6")
label_sex.grid(row=2, column=0, padx=10, pady=5, sticky="E")
sex_var = tk.StringVar()
sex_combobox = ttk.Combobox(root, textvariable=sex_var, values=["Male", "Female", "Other"], font=("Helvetica", 12))
sex_combobox.grid(row=2, column=1, padx=10, pady=5)

label_height = ttk.Label(root, text="Height:", font=("Helvetica", 12), background="#ADD8E6")
label_height.grid(row=3, column=0, padx=10, pady=5, sticky="E")
height_entry = ttk.Entry(root, width=30, font=("Helvetica", 12))
height_entry.grid(row=3, column=1, padx=10, pady=5)

label_weight = ttk.Label(root, text="Weight:", font=("Helvetica", 12), background="#ADD8E6")
label_weight.grid(row=4, column=0, padx=10, pady=5, sticky="E")
weight_entry = ttk.Entry(root, width=30, font=("Helvetica", 12))
weight_entry.grid(row=4, column=1, padx=10, pady=5)

# Add an image to the right side
image_path = 'profile img.jpg'  # Replace with the actual image file path
image = Image.open(image_path)
photo_image = ImageTk.PhotoImage(image)
image_label = ttk.Label(root, image=photo_image, background="#ADD8E6")
image_label.grid(row=0, column=2, rowspan=7, padx=10, pady=10)

# Create a custom style for the buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

submit_button = ttk.Button(root, text="Submit", command=submit_profile, style="TButton")
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

logout_button = ttk.Button(root, text="Log Out", command=log_out, style="TButton")
logout_button.grid(row=6, column=0, columnspan=2, pady=10)

# Add a style to set the background color of the buttons
style.configure("TButton", background="#4682B4")

# Run the Tkinter event loop
root.mainloop()
