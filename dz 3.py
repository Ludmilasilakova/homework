import matplotlib.pyplot as plt

# Оценки учеников
grades = [2, 3, 3, 2, 5, 5, 3, 4, 5, 4]

# Построение гистограммы
plt.hist(grades, bins=[2, 3, 4, 5, 6], edgecolor='black')
plt.xlabel('Оценки')
plt.ylabel('Колличество учеников')
plt.title('Распределение оценок по математике в классе')
plt.show()

import numpy as np

# Создание массива
random_array = np.random.randint(1, 11, size=(4, 4))
print(random_array)


import matplotlib.pyplot as plt

# Данные
total_students = 32
boys = 15 
girls = 17

# Построение круговой диаграммы
labels = ['Мальчики', 'Девочки']
sizes = [boys, girls]
colors = ['blue', 'pink']


plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal') 
plt.title('Соотношение мальчиков и девочек в классе')
plt.show()

