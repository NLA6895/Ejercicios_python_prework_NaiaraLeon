'''Bucles
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100
'''
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
  print(numero)

num = 1
while num <= 20:
  if num % 2 == 0:
   print(num)
  num += 1

suma = 0
z = 1
while z <= 100:
  suma += z
  z += 1
print('La suma del los numeros del 1 al 100 es', suma)