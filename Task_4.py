# Напишіть програму, яка зчитує з клавіатури фразу і виводить текст:
# "Фраза [введений рядок] має довжину [довжина введеного рядка] символів".


text = input('Type a text: ')
print(f'Фраза "{text}" має довжину {len(text)} символів')
