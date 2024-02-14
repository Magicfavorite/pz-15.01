def count_elements(lst, num):
    count = 0
    for element in lst:
        if element == num:
            count += 1
    return count

# Пользовательский ввод
lst = list(map(int, input("Введите элементы списка через пробел: ").split()))
num = int(input("Введите число: "))

#  вывод результата
result = count_elements(lst, num)
print(f"Число {num} встречается в списке {result} раз(а).")
