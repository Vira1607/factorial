print('Факториал')

# Дано натуральное число N. Программа находит N! (N факториал)
#
# Запись N! означает следующее:
# N! = 1 * 2 * 3 * 4 * 5 * … * N
#
# Пример:
#
# Введите число: 5
# Факториал числа 5 равен 120

number = int(input(''))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print('Факториал числа', number, 'равен', factorial)
