import tkinter as tk
from math import sqrt

def calculate():
    a, b, c = 15.7, 18.4, 19.2
    wc = sqrt(a * b * (1 - (c**2 / (a + b)**2)))
    wb = sqrt(a * c * (1 - (b**2 / (a + c)**2)))
    result_label.config(text=f"Бісектриса w_c = {wc:.2f} см\nБісектриса w_b = {wb:.2f} см")

root = tk.Tk()
root.title("Варіант 8 — Бісектриси w_c, w_b")
root.geometry("400x180")

info_label = tk.Label(root, text="Сторони трикутника:\na = 15.7 см, b = 18.4 см, c = 19.2 см")
info_label.place(x=100, y=10)

button = tk.Button(root, text="Обчислити", command=calculate)
button.place(x=150, y=60)

result_label = tk.Label(root, text="")
result_label.place(x=80, y=110)

root.mainloop()