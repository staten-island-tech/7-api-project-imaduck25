""" import requests

def cs():
    data = {"model": "default"}
    response = requests.post("http://colormind.io/api/", json=data)
    x = response.json()
    print(x)
cs() """


import tkinter as tk
window = tk.Tk()
window.title("Label Example")
# Create a label
label = tk.Label(
window,
    text="Hello, Tkinter!",

    font=("Comic Sans MS", 20, "bold"),
    fg="white",
    bg="purple",
    padx=20,
    pady=10,
    relief="ridge"
)
# Place it in the window
label.pack(pady=20)
window.mainloop()