# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел. 
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. 
# Ввод чисел продолжается до ввода пустой строки.
# Входные данные
# 36
# 12
# 144
# 18

import math
from functools import reduce

list = []
while True:
    current = input()
    if current.isdigit():
        list.append(int(current))
    else:
        break

print(list)
print()
for i in range(0, len(list)-1, +1):
    a = list[i]
    b = list[i+1]
    res = reduce(lambda a, b: math.gcd(a, b), list)
print(res)