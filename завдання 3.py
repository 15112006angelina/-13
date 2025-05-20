import tkinter as tk
from math import log, atan

def calculate():
    try:
        x = float(entry.get())
        if x <= 0:
            raise ValueError
        s = sum(5 * log(2 * x) / (atan(2 * x) + k**2) for k in range(1, 6))
        result_label.config(text=f"Сума = {s:.5f}")
    except:
        result_label.config(text="Помилка! x має бути > 0")

root = tk.Tk()
root.title("Варіант 8 — Сума")
tk.Label(root, text="∑[5·ln(2x)/(arctg(2x) + k²)], k=1..5").grid(row=0, columnspan=2, pady=5)

tk.Label(root, text="Введіть x:").grid(row=1, column=0, padx=5)
entry = tk.Entry(root)
entry.grid(row=1, column=1, padx=5)

tk.Button(root, text="Обчислити", command=calculate).grid(row=2, columnspan=2, pady=10)
result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2)

root.mainloop()