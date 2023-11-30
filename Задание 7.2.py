nums =  [19, 65, 57, 39, 152, 639, 121, 44, 90, 190] 
print("Исходный список:") 
print(nums)
result = list(filter(lambda x: (x % 19 == 0 or  x % 13 == 0), nums))
print("Числа приведенного выше списка, делящиеся на девятнадцать или тринадцать:") 
print(result)
