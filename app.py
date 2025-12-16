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
root.geometry("600x500")
root.resizable(False, False)

prompt = tk.Label(root, text="Which color belongs?",
font=("Serif", 20))
prompt.grid(row=0, column=2, pady=10) 

def clicked(n):
    print(f"You clicked button {n}")

for i in range(4):
    tk.Button(
        root,
        text=f"Button {i}",
        command=lambda i=i: clicked(i)
    ).grid(row=10, column=i, padx=10)

root.mainloop()