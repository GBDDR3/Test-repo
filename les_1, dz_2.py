numbers = [x ** 3 for x in range(3, 1000, 2)]
print(numbers)
list_1 = []
for i in numbers:
    sum_numbers = 0
    while i != 0:
        sum_numbers = sum_numbers + i%10
        i = i // 10
    list_1.append(sum_numbers)
print(type(list_1))

list_2 = []
for d in list_1:
    if d % 7 == 0:
        list_2.append(d)
print(list_2)

answer = 0
for s in list_2:
    answer = answer + s
print(answer)