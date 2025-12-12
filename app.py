""" import requests

def cs():
    data = {"model": "default"}
    response = requests.post("http://colormind.io/api/", json=data)
    x = response.json()
    print(x)
cs() """

import tkinter as tk

window = tk.Tk()
window.title("Image Example")
window.geometry("400x400")