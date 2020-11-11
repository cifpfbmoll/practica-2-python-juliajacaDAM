'''
Práctica 2. Ejercicio 4
Diagrama para calcular el mayor de dos números
'''

print('''
Vamos a calcular cuál es el mayor de los siguientes dos números
--------------------------------------------------
''')
num_1 = float(input("Introduce el primer número \n"))
num_2 = float(input("Introduce el segundo número \n"))

if num_1 > num_2:
    print(f'{num_1} es mayor que {num_2}')
else:
    print(f'{num_2} es mayor que {num_1}')