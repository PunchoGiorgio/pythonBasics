# Напишіть програму, яка обчислює вік кота в людських роках та виводить значення на екран.
# На вхід програмі подається число n - кількість кошачих років
# Перший рік кота == 15 років життя людини
# Кожен наступний рік == 9 років життя людини


n = int(input('Real age of the cat is '))
first_year = 15
next_years = 9

if 17 >= n > 0:
    result = first_year + (n - 1) * next_years
    print('Cat age in human years is', result)
else:
    print('Check input data')
