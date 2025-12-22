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

def clicked(n):
    result_label = prompt
    result_label.config(text=f"You clicked Button {n+1} ", font=("Courier New", 20))
    for btn in buttons:
        btn.config(state=tk.DISABLED)
        button_frame.destroy()

def next_round():
    global button_frame, buttons
    button_frame.destroy()
    button_frame = tk.Frame(root, bg="#D79179")
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

next_btn = tk.Button(root, text="Next Round", command=next_round, bg = "#A05F62", fg= "#FAF9FA")
next_btn.grid(row=8, column=0, columnspan=4, rowspan = 4, pady=20)

root.mainloop()



def check_answer(answer):
    if answer == correct_answer:
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Wrong!", fg="red")

# Create main window
root = tk.Tk()
root.title("Simple Quiz App")
root.geometry("500x200")

# Question
question_label = tk.Label(
    root,
    text="What is 2 + 2?",
    font=("Arial", 16)
)
question_label.pack(pady=10)

# Correct answer
correct_answer = "4"

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Answer buttons
answers = ["3", "4", "5", "6"]

for ans in answers:
    btn = tk.Button(
        button_frame,
        text=ans,
        width=8,
        command=lambda a=ans: check_answer(a)
    )
    btn.pack(side="left", padx=5)

# Result label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14)
)
result_label.pack(pady=10)

# Start the app
root.mainloop()
