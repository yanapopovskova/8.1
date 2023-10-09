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
    count_combinations = 0

    for combination in K:
        if all(x % 2 == 1 for x in combination[::2]) and all(x % 2 == 0 for x in combination[1::2]):
            sum_mod = sum(abs(x) for x in combination) % 6
            if sum_mod < min_sum:
                min_sum = sum_mod
                min_combination = combination
            count_combinations += 1

    # Закрытие предыдущего окна результатов (если оно было)
    if hasattr(calculate_minimum, 'result_root') and calculate_minimum.result_root.winfo_exists():
        calculate_minimum.result_root.destroy()

    # Создание нового окна результатов
    result_root = tk.Toplevel(root)
    calculate_minimum.result_root = result_root # Сохраняем ссылку на окно результатов
    result_root.title("Результаты")
    result_root.geometry("400x300")

    result_text = tk.Text(result_root, height=20, width=60)
    result_text.pack()

    result_text.insert(tk.END, f"Минимальная сумма: {min_sum}\n"
                               f"Количество допустимых комбинаций: {count_combinations}\n"
                               f"Комбинация переменных: {min_combination}\n")

# Создание графического интерфейса
root = tk.Tk()
root.title("Вычисление минимума")
root.geometry("400x300")

entry_label = tk.Label(root, text="Введите число n, "
                                  "количество переменных:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Вычислить", command=calculate_minimum)
calculate_button.pack()

root.mainloop()
