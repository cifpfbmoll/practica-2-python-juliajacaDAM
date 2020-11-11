'''
Práctica 2. Ejercicio 3
Diagrama que diga si un número es par o non
'''

numero = int(input("Introduce un número entero \n"))
if numero % 2 == 0 :
    print(f'El número {numero} SI es par')
else:
    print(f'El número {numero} NO es par')