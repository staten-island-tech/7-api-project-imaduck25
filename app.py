""" import requests

def cs():
    data = {"model": "default"}
    response = requests.post("http://colormind.io/api/", json=data)
    x = response.json()
    print(x)
cs() """


import tkinter as tk
def say_hello():
    print("Hello there!")

    window = tk.Tk()
    window.title("Button Example")
    # Create the button

    my_button = tk.Button(
        window, # parent container
        text="Say Hello", # label text
        command=say_hello, # function to call when clicked
        font=("Arial", 16), # nice big font
        bg="lightblue", # background color
        fg="black", # text color
        relief="raised", # gives it a 3D look
        padx=10, pady=5 # padding around the text

)
    window.mainloop()