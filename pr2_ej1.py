'''
Práctica 2. Ejercicio 1
Hacer un diagrama para calcular y mostrar el área de un triángulo
'''

print('''
Calculadora de áreas de triángulo
--------------------------------------------------
''')
base = float(input("Introduce la base \n"))
altura = float(input("Introduce la altura \n"))
area = base * altura / 2
print(f'El área de un triángulo con base = {base} y altura = {altura} es {area}')