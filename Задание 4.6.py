text = input("Введите текст со скобками: ")
content = text.split(')')
content = [text.split('(')[-1] for text in content if'(' in text]
print(*content, sep='\n')
