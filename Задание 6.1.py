def is_palindrome(word):
  reversed_word = word[::-1]
  return word == reversed_word
word = input("Введите текст:")
if is_palindrome(word):
  print(True)
else:
  print(False)
