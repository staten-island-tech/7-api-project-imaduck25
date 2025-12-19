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
root.geometry("700x700")
root.resizable(False, False)
root.configure(bg= "#D79179")

prompt = tk.Label(root, text="Which color belongs?",
font=("Courier New", 20))
prompt.grid(row=0, column=2, padx=10, pady=10) 

button_frame = tk.Frame(root)
button_frame.grid(row=2,column=2, pady=20)

buttons= []

def clicked(n):
    result_label = prompt
    result_label.config(text=f"You clicked Button {n+1}")
    for btn in buttons:
        btn.config(state=tk.DISABLED)

def next_round():
    global button_frame, buttons
    button_frame.destroy()
    button_frame = tk.Frame(root)
    button_frame.grid(row=4, column=0, columnspan=4, rowspan = 4, pady=20, padx= 50)
    for i in range(4):
            b = tk.Button(
                button_frame,
                text=f"Option {i+1}",
                command=lambda i=i: clicked(i),
                width=12
            )
            b.grid(row=0, column=i, padx=10)
            buttons.append(b)
next_round()

next_btn = tk.Button(root, text="Next Round", command=next_round)
next_btn.grid(row=8, column=0, columnspan=4, rowspan = 4, pady=20, 
              bg = "#A05F62")

root.mainloop()