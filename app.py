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

frame = tk.Frame(root)
frame.grid(row=0, column=0)

for i in range(4):
    root.columnconfigure(i, weight=1)
    tk.Button(root, text=f"B{i}").grid(row=4, column=i, columnspan=2, sticky="ew")


root.mainloop()