import pandas as pd

# Создание Series с повторяющимися индексами
data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'a', 'c'])
print(data)

# Обращение к элементам по повторяющемуся индексу 'a'
print(data['a'])


#3 Создание Series из словаря с индексом из ограниченного списка ключей
dict_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
limited_keys = ['a', 'c', 'e']

limited_series = pd.Series(dict_data, index=limited_keys)
print(limited_series)


# Создание Series из квадратов чисел от 1 до 20
squares_series = pd.Series([i**2 for i in range(1, 21)])
print(squares_series)


# Фильтрация: выбор элементов индекс которых не делится на 3
filtered_series = squares_series[squares_series.index % 3 != 0]
print(filtered_series)

#4 Дан файл "students.csv" с информацией об учениках:
# Имя, Возрас, Класс
# Анна, 13, 7
# Петр, 12, 6
# Мария, 14, 8
# Иван, 13, 7


#1 Считайте данные из файла "students.csv" с помощью метода read_csv.

students_df = pd.read_csv("students.csv")

#2 Выведите первые 3 строки датафрейма с помощью метода head.
print(students_df.head(3))

#3 Выведите последние 2 строки датафрейма с помощью метода tail.
print(students_df.tail(2))

#4 Получите общую информацию о датафрейме с помощью метода info.
students_df.info()