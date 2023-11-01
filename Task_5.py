# Напишіть програму, яка зчитує з клавіатури фразу і виводить "True" якщо фраза містить слово "Південь"
# (незалежно від регістру), якщо слово не знайдено - вивести "False"


text = input('Type the text: ')
mylist = text.title().split(' ')

word = 'Пiвдень'

if word in mylist:
    print(True)
else:
    print(False)
