numbers = input("Введите список чисел через пробел: ").split()
n = int(input("Введите степень: "))
numbers = [int(num) ** n for num in numbers]
print(numbers)
