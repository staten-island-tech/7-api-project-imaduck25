import requests

def cs():
    data = {"model": "default"}
    response = requests.post("http://colormind.io/api/", json=data)
    x = response.json()
    print(x)
cs()

import tkinter as tk

root = tk.Tk()
root.title("Shade Seeker")
root.geometry("700x500")
root.resizable(False, False)

prompt = tk.Label(root, text="                      Which color belongs?",
font=("Serif", 20))
prompt.grid(row=0, column=2, columnspan=6, pady=10) 

frame = tk.Frame(root)
frame.grid(row=0, column=0)

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

tk.Button(root, text="Hello", command=say_hello).grid(row=4, column=2, columnspan=3,pady=10)
tk.Button(root, text="Goodbye", command=say_goodbye).grid(row=5, column=1, columnspan=3, pady=10)

root.mainloop()