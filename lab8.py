import tkinter as tk

def calculate_minimum():
    n = int(entry.get())
    K = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    K.append([i, j, k, l])

    min_sum = float('inf')
    min_combination = None

    for combination in K:
        # Проверяем ограничения на четность и нечетность элементов
        if all(x % 2 == 1 for x in combination[::2]) and all(x % 2 == 0 for x in combination[1::2]):
            # Вычисляем значение целевой функции
            sum_mod = sum(abs(x) for x in combination) % 6
            # Обновляем минимальное значение и комбинацию переменных
            if sum_mod < min_sum:
                min_sum = sum_mod
                min_combination = combination

    result_label.config(text="Минимальное значение: {}\nНабор переменных, при котором достигается минимум: {}".format(min_sum, min_combination))

root = tk.Tk()
root.title("Расчет минимума")

label = tk.Label(root, text="Введите значение n:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Рассчитать", command=calculate_minimum)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
