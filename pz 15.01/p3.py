n = int(input("Введите количество элементов в списке: "))
elements = []

for i in range(n):
    element = int(input("Введите элемент списка: "))
    elements.append(element)

sum_elements = sum(elements)
average = sum_elements / n

print(f"Сумма всех элементов списка: {sum_elements}")
print(f"Среднее арифметическое всех элементов списка: {average}")
