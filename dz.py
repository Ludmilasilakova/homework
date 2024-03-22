#Домашнее задание по работе с модулем scipy.stats

#1 Работа с распределениями:
 
from scipy import stats

    # Создание объекта распределения
dist = stats.norm(loc=0, scale=1)

    # Получение значения функции плотности вероятности
pdf_value = dist.pdf(0)

    # Получение значения функции распределения
cdf_value = dist.cdf(1)
 
    # Генерация случайных чисел из распределения
random_value = dist.rvs(size=10)


#2 Задание на статистические тесты:
from scipy import stats

    # Одновыборочный t-текст
sample = [1, 2, 3, 4, 5]
t_statistic, p_value = stats.ttest_1samp(sample, popmean=3)

    # Двухвыборочный t-тест
sample1 = [1, 2, 3, 4, 5]
sample2 = [6, 7, 8, 9, 10]
t_statistic, p_value = stats.ttest_ind(sample1, sample2)