# Ввод - рекурсивная функция sum(a, b), возвращающая сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# return sum(a,b-1) + 1 - Так делать нельзя

a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))

def result (a, b):
    if a == 0:
        return b
    else:
        return result (a - 1, b + 1)

print(result (a, b))