n = int(input("Введите число:"))
p = 0
if n == 0 :
    print('0! = 0')
else:
    p = 1
    for i in range(2, n + 1):
        p = p * i
print(n,'!', '=', p)
