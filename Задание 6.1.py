def is_palindrome(word):
  word = word.replace(" ", "")
  word = word.lower()
  return word == word[::-1]
word = input("Введите текст:")
if is_palindrome(word):
  print(True)
  #если иначе
else:
  print(False)
