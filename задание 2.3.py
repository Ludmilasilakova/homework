#Проверить является ли клетка шахматной доски белой
a = int(input())
b = int(input())
if ( a + b ) % 2 == 1:
  print("Yes")
else:
  print("No")
