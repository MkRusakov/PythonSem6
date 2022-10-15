# Измените код одной-двух решенных ранее задач (с прошлых семинаров
# или домашних работ), применив лямбды, filter, map, zip, enumerate,
# списочные выражения.

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

######   1

# def SumOfNum (num):
#     nums = str(num)
#     result = 0
#     for i in range(0, len(nums), +1):
#         if nums[i].isdigit():
#             result += int(nums[i])
#     print(result)
# SumOfNum(6782)
# SumOfNum(0.56)



def SumOfNum (num):
    nums = str(num)
    nums = list(filter(lambda i: i != ".", nums))
    result = 0
    for i in range(0, len(nums), +1):
            result += int(nums[i])
    print(result)

SumOfNum(6782)
SumOfNum(0.56)

