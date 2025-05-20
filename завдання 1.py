import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a + c <= 0:
            raise ValueError("a + c має бути більше 0 (логарифм не визначений).")

        numerator = math.exp(b) + 3 * math.log(a + c)
        denominator = math.atan(a)  # арктангенс
        result = numerator / denominator + int(b * c)

        label_result.config(text=f"Результат: {result:.4f}")
    except ValueError as e:
        messagebox.showerror("Помилка", str(e))

# Вікно
root = tk.Tk()
root.title("Формула 8")
root.geometry("440x320")

# Формула
label_formula = tk.Label(
    root,
    text="f = (e^b + 3 ln(a + c)) / arctg(a) + [bc]",
    font=("Arial", 12, "italic")
)
label_formula.pack(pady=10)

# Введення значень
tk.Label(root, text="Введіть a:").pack()
entry_a = tk.Entry(root)
entry_a.pack()
entry_a.insert(0, "-5")

tk.Label(root, text="Введіть b:").pack()
entry_b = tk.Entry(root)
entry_b.pack()
entry_b.insert(0, "3.2")

tk.Label(root, text="Введіть c:").pack()
entry_c = tk.Entry(root)
entry_c.pack()
entry_c.insert(0, "9")

# Кнопка
tk.Button(root, text="Обчислити", command=calculate).pack(pady=10)

# Результат
label_result = tk.Label(root, text="Результат: ", font=("Arial", 11, "bold"))
label_result.pack()

# Запуск
root.mainloop()