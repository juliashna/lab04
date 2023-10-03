def count_elements(*lists):
    if len(lists) < 2:
        return 0
    elements = set(lists[0])

    for i in range(1, len(lists)):
        elements = elements.intersection(set(lists[i]))

    return len(elements)

# Получение количества списков от пользователя
n = int(input("Введите количество списков: "))

# Получение элементов каждого списка
lists = []
for i in range(n):
    elements = input(f"Введите элементы {i + 1}-го списка через пробел: ").split()
    lists.append(elements)

# Вызов функции count_common_elements
common_count = count_elements(*lists)
print(f"Количество одинаковых элементов в списках: {common_count}")