list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
name_ing = list[0][-5:]
name_acc = list[1][-6:].lower() .title()
name_tur = list[2][-7:].lower() .title()
name_dir = list[3][-6:].title()
print(f'Привет, {name_ing}'"!")
print(f'Привет, {name_acc}'"!")
print(f'Привет, {name_tur}'"!")
print(f'Привет, {name_dir}'"!")