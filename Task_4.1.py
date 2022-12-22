# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import Random, randint

file = open('data1.txt','w', encoding = 'utf-8') 

k = int(input('Введите k: '))

string = ''
   
while k >= 0:
        number = randint(0, 2)
        if k > 1:
            string += f'{number}x^{k}'
        elif k == 1:
            string += f'{number}x'
        elif k == 0:
            string += f'{number} = 0'
        if k > 0:
            string += ' + '
        k -= 1 

file.write(str(string))
file.close()

print(string)