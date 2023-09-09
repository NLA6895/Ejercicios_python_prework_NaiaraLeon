''' Condicionales
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
'''
x = 2
if x<0 :
  print('Este número es negativo')
else :
  print('Este número es positivo')

y = -88
if y % 2 == 0:
  print('Este número es par')
else:
  print('Este número es impar')

num1 = 8
num2 = 35
num3 = 9
if num1 >= num2 and num1 >= num3:
  mayor = num1
elif num2 >= num1 and num2 >= num3:
  mayor = num2
else:
  mayor = num3
print('El mayor de los 3 numeros es:', mayor)

