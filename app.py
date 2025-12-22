import requests
import tkinter as tk

def cs():
    data = {"model": "default"}
    response = requests.post("http://colormind.io/api/", json=data)
    x = response.json()
    print(x)
cs()

root = tk.Tk()
root.title("Shade Seeker")
root.geometry("600x400")
root.resizable(False, False)
root.configure(bg= "#D79179")

prompt = tk.Label(root, text="Which color belongs?",
font=("Courier New", 20), bg="#D79179", fg="#594654")
prompt.grid(row=0, column=2, padx=10, pady=10) 

button_frame = tk.Frame(root, bg="#D79179")
button_frame.grid(row=2,column=2, pady=20)

buttons= []

def check(answer):
    result_label = prompt
    if answer == correct_answer:
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Wrong!")
    for btn in buttons:
        btn.config(state=tk.DISABLED)
        button_frame.destroy()

correct_answer = "2"

def next_round():
    global button_frame, buttons
    button_frame.destroy()
    button_frame = tk.Frame(root, bg="#D79179")
    button_frame.grid(row=4, column=0, columnspan=4, rowspan = 4, pady=20, padx= 50)
    for i in range(4):
            btn = tk.Button(
            button_frame,
            text=i,
            width=8,
            command=lambda a=i: check(a)
            )
            btn.grid(row=0, column=i, padx=10)
            buttons.append(btn)
next_round()

next_btn = tk.Button(root, text="Next Round", command=next_round, bg = "#A05F62", fg= "#FAF9FA")
next_btn.grid(row=8, column=0, columnspan=4, rowspan = 4, pady=20)

root.mainloop()