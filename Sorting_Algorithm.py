import random
import copy
import time

numbers_original = []
for i in range(0, 1000):
    numbers_original.append(i)
random.shuffle(numbers_original)
# time_start = time.time()
numbers = copy.deepcopy(numbers_original)
print(numbers)
0.019

# [4,| 6, 2, 7]
# [6, 4,| 2, 7]
# [6, 4, 2,| 7]
# [6, 4, 7, 2|]
# [6,| 4, 7, 2]
# [6, 4, |7, 2]
# [6, 7, 4, |2]
# [6|, 7, |4, |2]
#
# [6, |7, |4, |8]
# [6, |7, |8, |4]
#
# |||||
#
# [4,| 6, 2, 7]
# [6, 4,| 2, 7]
# [6, 4, 2,| 7]
# [6, 4, |7, 2]
# [6, |7, 4, 2]
# [7, |6, 4, 2]
# [7, 6, |4, 2]
# [7, 6, 4, |2]

#
# [~4~_, |6|, 2, 7]
#
# [~6, ~4~_, |2|, 7]
#
# [~6, ~4,~ 2 ~, |7|]
#
# [7, 6, ~4,~ 2]
#
# [4, 6, 2, |7|]
#
# [7, 4, |6|, 2]
#
# [7, 6, |4|, 2]
#
# [7, 6, 4, 2]


# time_end = time.time()
# print("Time : " + str(time_end - time_start))
print(numbers)



#
#real bubble sort
print("Bubble sort : ")
time_start = time.time()
numbers = copy.deepcopy(numbers_original)
# print(numbers)
sum = 0
for i in range(len(numbers) - 1, 0, -1):
    count = 0
    for j in range(i):
        if numbers[j] < numbers[j + 1]:
            count += 1
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    # print(count)
    sum += count
    if count == 0:
        break
time_end = time.time()
print("Time : " + str(time_end - time_start))
print("Switch : " + str(sum))
print(numbers)

#Shaker sort
print("Shaker Sort : ")
time_start = time.time()
numbers = copy.deepcopy(numbers_original)
# print(numbers)
count_start = 0
sum = 0
for i in range(len(numbers) - 1, 0, -1):
    count = 0
    for j in range(count_start, i):
        if numbers[j] < numbers[j + 1]:
            count += 1
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
    # print(count)
    sum += count
    count = 0
    for j in range(i - 1, count_start, -1):
        if numbers[j - 1] < numbers[j]:
            count += 1
            temp = numbers[j - 1]
            numbers[j - 1] = numbers[j]
            numbers[j] = temp
    # print(count)
    sum += count
    count_start += 1
    if count == 0:
        break
time_end = time.time()
print("Time : " + str(time_end - time_start))
print("Switch : " + str(sum))
# print(numbers)
#
#
#Insertion sort
print("Insertion Sort: ")
time_start = time.time()
numbers = copy.deepcopy(numbers_original)
print(numbers)
count_start = 0
sum = 0
for i in range(0, len(numbers), 1):
    count = 0
    for j in range(0, i):
        if numbers[j] < numbers[i]:
            count += 1
            number_pop = numbers.pop(i)
            numbers.insert(j, number_pop)
            break
    sum += count
time_end = time.time()
print("Time : " + str(time_end - time_start))
print("Switch : " + str(sum))
print(numbers)

#Selection sort
print("Selection Sort")
time_start = time.time()
numbers = copy.deepcopy(numbers_original)
print(numbers)
count_start = 0
sum = 0
for i in range(0, len(numbers), 1):

    nMax = numbers[i]
    nMaxPos = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] > nMax:
            nMax = numbers[j]
            nMaxPos = j
    count += 1
    number_pop = numbers.pop(nMaxPos)
    numbers.insert(i, number_pop)

time_end = time.time()
print("Time : " + str(time_end - time_start))
print("Switch : " + str(sum))
print(numbers)
#
#
def quick(num_list, start, end):
    if end - start <= 1:
        return
    pivot = None
    if end - start == 2:
        if num_list[start] < num_list[end - 1]:
            num_list[start], num_list[end - 1] = num_list[end - 1], num_list[start]
            # print(num_list[start: end])
        return

    # print(num_list[start: end])
    a = num_list[start]
    b = num_list[(start + end) // 2]
    c = num_list[end - 1]

    if a <= b < c or c <= b < a:
        pivot = num_list[(start + end) // 2]
        # print(ran1)
    elif b <= c < a or a <= c < b:
        pivot = num_list[end - 1]
        # print(ran2)
    else:
        pivot = num_list[start]
        # print(ran)

    i = start - 1
    for j in range(start, end):
        if num_list[j] >= pivot:
            i += 1
            num_list[i], num_list[j] = num_list[j], num_list[i]

    # print(num_list[start: end])
    quick(num_list, i+1, end)
    quick(num_list, start, i+1)

#Quick sort
print("Quick Sort: ")
time_start = time.time()
numbers = copy.deepcopy(numbers_original)
print(numbers)

quick(numbers, 0, len(numbers))

time_end = time.time()
print("Time : " + str(time_end - time_start))
print("Switch : " + str(sum))
print(numbers)



# Quick Sort
#
# Merge Sort + Insertion sort
#
# Shell Sort
# == Insertion Sort
#
# ======its like Bubble sort and Shaker Sort

#Bogo Sort

def checksort(num_list):
    for i in range(len(num_list)):
        if numbers_original[i] != num_list[i]:
            return False
    return True

# print("Bogo Sort")
# numbers = copy.deepcopy(numbers_original)
# time_start = time.time()
# sum = 0
# while True:
#     random.shuffle(numbers)
#     sum += 1
#     print(str(1), end="")
#     if checksort(numbers):
#         break
#
# time_end = time.time()
# print("Shuffle : " + str(sum))
# print("Time : " + str(time_end - time_start))