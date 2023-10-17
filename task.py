# Функція обчислення суми рядку
def sum_of_row(row):
    return sum(row)

#Розмір масиву NxN
N = int(input("Введіть розмір масиву (NxN) у вигляді числа : "))

# Робимо порожній масив NxN
matrix = []

# Заповнюємо масив
for i in range(N):
    row = list(map(int, input(f"Введіть {i+1}-й рядок ({N} чисел через пробіл): ").split()))
    matrix.append(row)

# Обчислюємо суми рядків і зберігаємо їх разом з індексами рядків
row_sums = [(i, sum_of_row(matrix[i])) for i in range(N)]

# Сортуємо рядки за зростанням їх сум
sorted_rows = sorted(row_sums, key=lambda x: x[1])

# Створюємо новий відсортований масив
sorted_matrix = [matrix[i] for i, _ in sorted_rows]

# Виводимо відсортований масив
print("Відсортований масив:")
for row in sorted_matrix:
    print(" ".join(map(str, row)))
