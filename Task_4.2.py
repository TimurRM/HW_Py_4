# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


from numpy.polynomial import Polynomial
from random import randint

k1 = int(input('Input K1: '))
k2 = int(input('Input K2: '))

poly1 = Polynomial([randint(-100, 100) for i in range(k1 + 1)])
poly2 = Polynomial([randint(-100, 100) for j in range(k2 + 1)])

print(poly1)
print(poly2)
summa = poly1 + poly2
print(summa)


with open('file01.txt', 'w', encoding='utf-8') as file:
    file.write(f"{poly1}")

with open('file02.txt', 'w', encoding='utf-8') as file:
    file.write(f"{poly2}")

with open('file01.txt','r') as file:
    firstPolyMath = file.readline()
    firstPoly = firstPolyMath.split()

with open('file02.txt','r') as file:
    secondPolyMath = file.readline()
    secondPoly = secondPolyMath.split()

summaPoly = poly1 + poly2

with open('summa_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'({poly1}) + ({poly2}) = {summaPoly}')