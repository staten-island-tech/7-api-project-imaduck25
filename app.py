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
window.geometry("600x500")
window.resizable(False, False)

prompt = tk.Label(window, text="Which color belongs?",
font=("Serif", 20))
prompt.pack(pady=10) 

my_button = tk.Button(
window,
text="                      ",
font=("Serif", 16), 
bg="lightblue", 
fg="black", 
relief="raised", 
padx=10, pady=5 

)
my_button.pack(pady=20)

window.mainloop()