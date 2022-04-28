numbers = {
  'один' : 'one',
  'два' : 'two',
  'три' : 'three',
  'четыре' : 'four',
  'пять' : 'five',
  'шесть': 'six',
  'семь' : 'seven',
  'восемь' : 'eight',
  'девять' : 'nine',
  'десять' : 'ten'
}

def num_translate(numbers):
  keys = input('Введите значение: ')
  print(numbers[keys])
num_translate(numbers)