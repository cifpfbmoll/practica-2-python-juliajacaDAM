'''
Práctica 2. Ejercicio 2
Convertir de grados centígrados a grados Farenheit
'''
print('''
Convertir de grados centígrados a grados Farenheit
--------------------------------------------------
''')
grados_cent = float(input("Introduce los grados centígrados \n"))
grados_far = grados_cent * 9 / 5 + 32
print(f'{grados_cent}°C son {grados_far}°F')