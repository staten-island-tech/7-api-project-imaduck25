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
""" root.resizable(False, False) """
root.configure(bg= "#D79179")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

prompt = tk.Label(root, text="Which color belongs?",
font=("Courier New", 20), 
bg="#D79179", 
fg="#594654")
prompt.grid(row=0, column=1, padx=10, pady=10)

palette = tk.Label(root,
    text="Palettee:",
    font=("Courier New", 12, "bold"),
    bg="#D79179",
    fg="#594654")
palette.grid(row=1, column=1, padx=10, pady=10)

palette_frame = tk.Frame(root)
palette_frame.grid(row=2,column=1)

colors = ["#D79179", "#594654", "#A05F62","#859A9D"]
for i, color in enumerate(colors):
     sq = tk.Label(
          palette_frame,
          bg=color,
          width=10,
          height=5
     )
     sq.grid(row=0, column=i, padx=5)

button_frame = tk.Frame(root, bg="#D79179")
button_frame.grid(row=5,column=1, pady=20)

def check(answer):
    result_label = prompt
    if answer == correct_answer:
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Wrong!")
    for btn in buttons:
        btn.config(state=tk.DISABLED)

correct_answer = "2"

def next_round():
    global button_frame, buttons
    button_frame.destroy()
    button_frame = tk.Frame(root, bg="#D79179")
    button_frame.grid(row=3, column=1,pady=20)
    buttons = []
    for i in range(4):
            btn = tk.Button(
            button_frame,
            text=i,
            width=10,
            fg="#A05F62",
            font=("Courier New", 10, "bold"),
            command=lambda a=i: check(a)
            )
            btn.grid(row=0, column=i, padx=10)
            buttons.append(btn)
next_round()

next_btn = tk.Button(root, 
text="Next Round", 
command=next_round, 
bg = "#859A9D", 
fg= "#FAF9FA")
next_btn.grid(row=9, column=0, columnspan=4, rowspan = 4, pady=20)

root.mainloop()