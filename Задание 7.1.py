a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
# если длина списков разная,то короткий расширяем нулями
a.extend([0,] * (len(b) - len(a)))
b.extend([0,] * (len(a) - len(b)))
# обработка
c = map(sum, zip(a,b))
print(list(c))
