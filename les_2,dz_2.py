list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list[1] = '"05"'
list[3] = '"17"'
list[-1] = '"+05"'
print(list) # заменены значения

list2 = ''

for i in list:
  list2 += i
  list2 += ' '
print(list2) # список -> строка