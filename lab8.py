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

    result_root = tk.Toplevel(root)
    result_root.title("Результаты")
    result_root.geometry("400x300")

    result_text = tk.Text(result_root, height=20, width=60)
    result_text.pack()

    result_text.insert(tk.END, f"Минимальная сумма: {min_sum}\n"
                               f"Комбинация переменных: {min_combination}\n")


# Создание графического интерфейса
root = tk.Tk()
root.title("Вычисление минимума")
root.geometry("400x300")

entry_label = tk.Label(root, text="Введите число:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Вычислить", command=calculate_minimum)
calculate_button.pack()

root.mainloop()