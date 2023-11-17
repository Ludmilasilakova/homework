a = int(input('a'))
b = int(input('b'))
c = int(input('c'))
m = a
if b > a:
  m = b
  if c > m:
    m = c
    print(m)
