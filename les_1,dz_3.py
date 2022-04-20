numbers = range(0,100)

for i in numbers:
  i=i+1
  if i % 10 == 1 and i != 11:
    print(i, 'Процент')
  elif i%10 > 1 and i%10 < 5:
    print(i, 'Процентa')
  else:
    print(i, 'Процентов')