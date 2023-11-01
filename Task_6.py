# Напишіть програму, яка зчитує з клавіатури фразу і виводить "True" якщо це слово - паліндром,
# якщо слово не знайдено - вивести "False"


word = input('Type the word: ')
if word == word[::-1]:
    print(f'Is the "{word}" a palindrome? -', True)
else:
    print(f'Is the "{word}" a palindrome? -', False)
