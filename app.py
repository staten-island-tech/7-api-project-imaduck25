import requests

def cs():
    data = {"model": "default"}
    response = requests.post("http://colormind.io/api/", json=data)
    x = response.json()
    print(x)
cs()

import tkinter as tk

window = tk.Tk()
window.title("Shade Seeker")
window.geometry("400x400")
window.resizable(True, True)

prompt = tk.Label(window, text="Which color belongs?",
font=("Sans Serif", 14))
prompt.pack(pady=10) 

window.mainloop()