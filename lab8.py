import tkinter as tk

def calculate_minimum():
    n = int(entry.get())

    min_sum = float('inf')
    min_combination = None
    count_combinations = 0

    for i in range(1, n, 2):
        for j in range(0, n, 2):
            for k in range(1, n, 2):
                for l in range(0, n, 2):
                    sum_mod = (i + k + j + l) % 6
                    if sum_mod < min_sum:
                        min_sum = sum_mod
                        min_combination = [i, j, k, l]
                    count_combinations += 1

    # Закрытие предыдущего окна результатов (если оно было)
    if hasattr(calculate_minimum, 'result_root') and calculate_minimum.result_root.winfo_exists():
        calculate_minimum.result_root.destroy()

    # Создание нового окна результатов
    result_root = tk.Toplevel(root)
    calculate_minimum.result_root = result_root  # Сохраняем ссылку на окно результатов
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

entry_label = tk.Label(root, text="Введите число n > 1, количество переменных:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Вычислить", command=calculate_minimum)
calculate_button.pack()

window_width = 400
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.mainloop()
