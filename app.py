import requests
import tkinter as tk
import random

score=0

def cs():
    data = {"model": "default"}
    response = requests.post("http://colormind.io/api/", json=data)
    x = response.json()
    print(x)
cs()

root = tk.Tk() #root and window are same thing btw
root.title("Shade Seeker")
root.geometry("600x400")
root.resizable(False, False)
root.configure(bg= "#D79179")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
#makes 3 equal columns so code is centered

prompt = tk.Label(root, text="Which color belongs?",
font=("Courier New", 20), 
bg="#D79179",
fg="#594654")
prompt.grid(row=0, column=1, padx=10, pady=10)
#.grid allows you to put a widget in a specific row and column of window

score_label = tk.Label(
    root,
    text= "SCORE:0 ",
    font=("Courier New", 14),
    bg="#D79179",
    fg= "#A05F62"
    )
score_label.grid(row=0, column=2)

palette = tk.Label(root,
    text="Palettee:",
    font=("Courier New", 12, "bold"),
    bg="#D79179",
    fg="#594654")
palette.grid(row=1, column=1, padx=10, pady=10)
 
palette_frame = tk.Frame(root, bg="#D79179")
palette_frame.grid(row=2,column=1)
#basically a box to hold color sq

colors = [ "#FAF9FA", "#594654", "#A05F62","#859A9D"]
#testing palete
squares = []
#store sq and colors

for i, color in enumerate(colors):
     sq = tk.Label(
          palette_frame,
          bg=color,
          width=10,
          height=5
     )
     sq.grid(row=0, column=i, padx=5)
     squares.append((sq, color))
     #saves sq so it can be hudden later

button_frame = tk.Frame(root, bg="#D79179")
button_frame.grid(row=5,column=1, pady=20)
#hold answer buttons

def check(answer):
    global score
    #global is when instead of creating a local variable in a function, you use a variable outside the function; in ths case, we arent making a new score variable that only exists in the function, we are using the score variable outside the functipm

    result_label = prompt
    if answer == correct_answer:
        result_label.config(text="Correct!", fg= "#A05F62")
        #.config changes smth abt the widget
        score+=1
        score_label.config(text=f"SCORE:{score}", fg= "#A05F62")
    else:
        result_label.config(text="Wrong!", fg= "#A05F62")
        hidden_square.grid()
    for btn in buttons:
        btn.config(state=tk.DISABLED) #tk.DISABLED makes the widget "turn off" so that the player cnat click it

def rgbtohex(r, g,b):
    return f"#{r:02x}{g:02x}{b:02x}"
#done b4 gp() to define it

def gp():
    # gp stands for get palette
    data = {"model": "default"}
    response = requests.post("http://colormind.io/api/", json=data)
    x = response.json()
    palette = x["result"] #x is dictionary, a list of 5 colors is stored under ["result"]
    hex_colors = [] #empty list in which we will store hex codes
    for r,g,b in palette:
        hex_colors.append(rgbtohex(r,g,b))
    return hex_colors
gp()

def next_round():
    global button_frame, buttons, correct_answer, palette_frame, squares

    prompt.config(text="Which color belongs?", fg="#594654")
    #resets question, had to do bcuz the wrong/correct labels weren't cahnaging

    palette_colors = gp() #get a new palette, all 5 colors

    pb=gp() #pb= palette b
    wrong_choices=random.sample(pb,3)
    #get a 2nd palette for the wrong answers, take 3 of the colors

    squares.clear() #empties list called sq
    palette_frame.destroy() #deletes palette frame from screen
    palette_frame = tk.Frame(root, bg="#D79179")
    palette_frame.grid(row=2, column=1)
    #delete old palette and make a new 1

    for i, color in enumerate(palette_colors):
     #i=index, position number of color, used to place tge color in correct coloum
     sq = tk.Label(
          palette_frame,
          bg=color,
          width=10,
          height=5
     )
     sq.grid(row=0, column=i, padx=5)
     squares.append((sq, color))
    #draw the new sq

    global hidden_square
    hidden_square, hidden_color = random.choice(squares) #splits the widget and hex into 2 variables
    #hidden_sqare= tkinter widget, hidden_color=hex / colcor of square
    hidden_square.grid_remove()
    correct_answer = hidden_color
    #hide a sq, save as correct color

    answer_colors = [correct_answer]+ wrong_choices #combine the 2 lists togther
    random.shuffle(answer_colors)
    #mix correct and wrong answers

    button_frame.destroy()
    button_frame = tk.Frame(root, bg="#D79179")
    button_frame.grid(row=3, column=1,pady=20)

    buttons = [] #outside loop since if its inside then it will reset everytime and the data will be lost
    for i, color in enumerate(answer_colors):
            btn = tk.Button(
            button_frame,
            bg=color,
            width=10,
            height=5,
            fg="#FAF9FA",
            font=("Courier New", 10, "bold"),
            command=lambda a=color:check(a)
            ) #lambda= shorter version of smth like:
            #def add(a,b): 
            #   return a+b
            #NEED to use lambda so that function doesnt run immediately and waits for click
            #command=lambda a=color:check(a) = freeze current value of "color", store it in new varianle "a", each button gets its own copy of color; make the buttons "remeber" their OWN colors
            #must do ts entire line to fix the "dont run now" problem and the loop overwriting "color" variable---the buttons rember differnet colors, not only last color
            btn.grid(row=0, column=i, padx=10)
            buttons.append(btn) #stores the buttons so that i can work with them later (ex. destroying old buttons, disabling or hiding buttons, keeping track of which was clicked)
next_round()

next_btn = tk.Button(root, 
text="Next Round", 
command=next_round, #when next round button is clicked, this function is ran
bg = "#859A9D", 
fg= "#FAF9FA")
next_btn.grid(row=9, column=1, pady=20)

root.mainloop()