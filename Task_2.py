# Напишіть програму, яка впорядковує три числа від більшого до меншого.
# Програма має вивести три числа, кожне на окремому рядку, упорядкованих від більшого до меншого.


n1 = int(input("Введіть n1:: "))
n2 = int(input("Введіть n2:: "))
n3 = int(input("Введіть n3:: "))

mylist = [n1, n2, n3]

max_numb = max(mylist)
min_numb = min(mylist)
middle_numb = sum(mylist) - max_numb - min_numb

print(f'{max_numb}\n{middle_numb}\n{min_numb}')


