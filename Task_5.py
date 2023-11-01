# Напишіть програму, яка зчитує з клавіатури фразу і виводить "True" якщо фраза містить слово "Південь"
# (незалежно від регістру), якщо слово не знайдено - вивести "False"


text = input('Type the text: ')
text_1 = text.title()
word = 'Пiвдень'

if word in text_1:
    print(True)
else:
    print(False)
