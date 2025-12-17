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
prompt.grid(row=0, column=2, columnspan=6, pady=10) 

tk.Button(root, text="Wide Button").grid(
    row=1,
    column=0,
    columnspan=2
)

root.mainloop()