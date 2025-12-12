""" import requests

def cs():
    data = {"model": "default"}
    response = requests.post("http://colormind.io/api/", json=data)
    x = response.json()
    print(x)
cs()

 """

import tkinter as tk # bring in tkinter and call it tk
# Create the main window (like your app's frame)
window = tk.Tk()
window.title("Message Reverser") # title at the top of the window
window.geometry("400x250") # set the size (width x height)
window.resizable(False, False) # keep it from being resized
# --- Widgets (the things that go inside the window) ---
# Label: tells user what to do
prompt = tk.Label(window, text="Type your message below:",
font=("Arial", 14))
prompt.pack(pady=10) 
# Entry box: where the user types their message
entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5)
# Label to display the reversed message later
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="blue")
result_label.pack(pady=15)

# --- Functionality (what happens when you click the button) ---
def reverse_message():
    text = entry.get() # get whatever the user typed
    reversed_text = text[::-1] # slice trick to reverse a string
    result_label.config(text=f"Backwards: {reversed_text}")
# Button: when clicked, it calls reverse_message()
reverse_button = tk.Button(window, text="Reverse Message!",
font=("Arial", 14),

command=reverse_message)

reverse_button.pack(pady=10)
# Keeps the window open and waiting for clicks or typing
window.mainloop()