import random
import copy
import time

numbers_original = []
for i in range(0, 1000):
    numbers_original.append(i)
random.shuffle(numbers_original)

#fake bubble sort
# print("fake bubble sort")
# time_start = time.time()
# numbers = copy.deepcopy(numbers_original)
# print(numbers)
# count_end = 0
# while True:
#     count = 0
#     for i in range(len(numbers) - count_end):
#         for j in range(i):
#             if numbers[j] < numbers[j+1]:
#                 count += 1
#                 temp = numbers[j]
#                 numbers[j] = numbers[j+1]
#                 numbers[j+1] = temp
#     count_end += 1
#     print(count)
#     if count == 0:
#         print(count)
#         break
# time_end = time.time()
# print("Time : " + str(time_end - time_start))
# print("Switch : " + str(sum))
# print(numbers)


# numbers = copy.deepcopy(numbers_original)
# print(numbers)
# count_end = 0
# count_start = 0
# while True:
#     count = 0
#     for i in range(count_start, len(numbers) - count_end):
#         for j in range(i):
#             if numbers[j] < numbers[j+1]:
#                 count += 1
#                 temp = numbers[j]
#                 numbers[j] = numbers[j+1]
#                 numbers[j+1] = temp
#
#     print(count)
#     for i in range(0, len(numbers)):
#         if numbers[i] == 99:
#             print("pos 99 " + str(i))
#     count_end += 1
#
#     for i in range(len(numbers) - count_end, count_start, -1):
#         for j in range(i):
#             if numbers[j - 1] < numbers[j]:
#                 count += 1
#                 temp = numbers[j -1]
#                 numbers[j-1] = numbers[j]
#                 numbers[j] = temp
#
#     count_start += 1
#     print(count)
#     if count == 0:
#         break
# print(numbers)

#real bubble sort
print("Bubble sort : ")
time_start = time.time()
numbers = copy.deepcopy(numbers_original)
print(numbers)
sum = 0
for i in range(99, 0, -1):
    count = 0
    for j in range(i):
        if numbers[j] < numbers[j + 1]:
            count += 1
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
    sum += count
    if count == 0:
        break
time_end = time.time()
print("Time : " + str(time_end - time_start))
print("Switch : " + str(sum))
print(numbers)


#Shaker sort
# print("Shaker Sort : ")
# time_start = time.time()
# numbers = copy.deepcopy(numbers_original)
# print(numbers)
# count_start = 0
# sum = 0
# for i in range(99, 0, -1):
#     count = 0
#     for j in range(count_start, i):
#         if numbers[j] < numbers[j + 1]:
#             count += 1
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#     print(count)
#     sum += count
#     count = 0
#     for j in range(i - 1, count_start, -1):
#         if numbers[j - 1] < numbers[j]:
#             count += 1
#             temp = numbers[j - 1]
#             numbers[j - 1] = numbers[j]
#             numbers[j] = temp
#     print(count)
#     sum += count
#     count_start += 1
#     if count == 0:
#         break
# time_end = time.time()
# print("Time : " + str(time_end - time_start))
# print("Switch : " + str(sum))
# print(numbers)


#Shaker sort
print("Shaker Sort : ")
time_start = time.time()
numbers = copy.deepcopy(numbers_original)
print(numbers)
count_start = 0
sum = 0
for i in range(99, 0, -1):
    count = 0
    for j in range(count_start, i):
        if numbers[j] < numbers[j + 1]:
            count += 1
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
    print(count)
    sum += count
    count = 0
    for j in range(i - 1, count_start, -1):
        if numbers[j - 1] < numbers[j]:
            count += 1
            temp = numbers[j - 1]
            numbers[j - 1] = numbers[j]
            numbers[j] = temp
    print(count)
    sum += count
    count_start += 1
    if count == 0:
        break
time_end = time.time()
print("Time : " + str(time_end - time_start))
print("Switch : " + str(sum))
print(numbers)


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


def quick(num_list, start, end):
    if end - start <= 1:
        return
    # print(num_list[start : end])

    pivot = num_list[random.randint(start, end-1)]

    # a = num_list[start]
    # b = num_list[(start + end) // 2]
    # c = num_list[end - 1]

    # if a <= b < c or c <= b < a:
    #     pivot = num_list[(start+end)//2]
    #     # print(ran1)
    # elif b <= c < a or a <= c < b:
    #     pivot = num_list[end - 1]
    #     # print(ran2)
    # else:
    #     pivot = num_list[start]
        # print(ran)

    # if end - start == 2:
    #     if num_list[start] < num_list[end - 1]:
    #         num_list[start], num_list[end - 1] = num_list[end - 1], num_list[start]
    #         print(num_list[start: end])
    #     return

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


# def quick(num_list, start, end):
#     ran = random.randint(0, len(num_list) - 1)
#     ran1 = random.randint(0, len(num_list) - 1)
#     ran2 = random.randint(0, len(num_list) - 1)
#
#     pivot = None
#     pivot_pos = None
#     if num_list[ran] < num_list[ran1] < num_list[ran2]:
#         pivot = num_list[ran1]
#         print(ran1)
#     elif num_list[ran1] < num_list[ran2] < num_list[ran]:
#         pivot = num_list[ran2]
#         print(ran2)
#     else:
#         pivot = num_list[ran]
#         print(ran)
#
#     print(pivot)
#     while True:
#         smallPos = 0
#         bigPos = 0
#         for i in range(len(num_list)):
#             if pivot >= num_list[i]:
#                 for j in range(len(num_list) -1, 0, -1):
#                     if pivot < num_list[j]:
#                         bigPos = j
#                         smallPos = i
#                         break
#                 break
#         if smallPos < bigPos:
#             temp = num_list[smallPos]
#             print("Temp")
#             num_list[smallPos] = num_list[bigPos]
#             num_list[bigPos] = temp
#         else:
#             return num_list
