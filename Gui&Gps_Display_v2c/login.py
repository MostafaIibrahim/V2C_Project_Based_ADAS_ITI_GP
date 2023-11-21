import tkinter as tk
from ttkbootstrap import Style
#import GUI2

from tkinter import ttk
import ttkbootstrap as ttk
from PIL import ImageTk,Image
import json

import os


def login():
    username = username_entry.get()
    password = password_entry.get()

    # Replace this with your authentication logic
    if username == "ITI" and password == "123":
        login_status.config(text="Login successful", fg="green")
        
        GUI_display_path = 'GUI_Display.py'
       # AWS_getData_path = 'AWS_getData.py'
        #GPS_createHtml_path = 'Gps_Create-html.py'
        
        os.system(f'python {GUI_display_path}')
        #os.system(f'python {AWS_getData_path}')
        #os.system(f'python {GPS_createHtml_path}')
        
 
    else:
        login_status.config(text="Invalid username or password", fg="red")
        

root = tk.Tk()
style = Style(theme='lumen')  # You can choose different themes here

# Adding an image to the right side
image = tk.PhotoImage(file="las/ITINexusWhite.png")  # Replace "path_to_your_image.png" with the image path
image_label = tk.Label(root, image=image)
image_label.image = image  # Keep a reference to avoid garbage collection
image_label.pack(side=tk.TOP, padx=20)


root.title("Login Page")
root.geometry("600x300")  # Adjusted window size

frame = tk.Frame(root)
frame.pack(padx=20, pady=30)

label_style = {'font': ('Helvetica', 11)}  # Custom label style
entry_style = {'font': ('Helvetica', 11)}  # Custom entry style

tk.Label(frame, text="Username:", **label_style).grid(row=1, column=0, padx=5, pady=5)
username_entry = tk.Entry(frame, **entry_style)
username_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Password:", **label_style).grid(row=2, column=0, padx=5, pady=5)
password_entry = tk.Entry(frame, show="*", **entry_style)
password_entry.grid(row=2, column=1, padx=5, pady=5)

login_button = tk.Button(frame, text="Login", command=login, **entry_style)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

login_status = tk.Label(frame, text="", fg="black", **label_style)
login_status.grid(row=4, column=0, columnspan=2)



root.mainloop()
