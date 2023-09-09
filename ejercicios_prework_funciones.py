'''Funciones
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Define una función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa.'''

def suma_num(num1, num2):
  suma = num1 + num2
  return suma
resultado = suma_num(6,8)
print(resultado)

def factorial_num(numeros):
  factorial = 1
  for numero in range(1, numeros + 1):
    factorial *= numero
  return factorial
resultado_factorial = factorial_num(5)
print(resultado_factorial)

def es_primo(num):
  if num <= 1:
    return False
  elif num <= 3:
    return True
  elif num % 2 == 0 or num % 3 == 0:
    return False
  n = 15
  while n * n <= num:
    if n % num == 0 or n % (n + 2) == 0:
      return False
    n += 6
  return True
number = 6
if es_primo(number):
  print(f"{number} es un numero primo")
else:
  print(f"{number} no es un numero primo")

def suma_numeros(list_number):
  total = 0 
  for number in list_number:
    total += number
  return total

resultado_suma = suma_numeros([2,5,6,7,8])
print('La suma de estos numeros es', resultado_suma)

def cadena_texto(texto_reversa):
  return texto_reversa[::-1]
texto = ('Buenos dias')
cadena_texto_reversa = cadena_texto(texto)
print(cadena_texto_reversa)
