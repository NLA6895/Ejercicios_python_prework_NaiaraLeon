'''1. Crea una función para verificar si un número es par o impar y devuelva “El
número es par” o “El número es impar” según corresponda.'''
def es_par(x):
  if x % 2 == 0:
    return 'El número es par.'
  else:
    return 'El número es impar.'

x = int(input("Ingresa un número: "))
resultado_par_impar = es_par(x)
print(resultado_par_impar)

'''2.Crea una función a la que pases un número como argumento, calcule el factorial
de ese número y haga print del resultado'''

def factorial(num1):
  resultado_fact = 1
  for i in range (1, num1 + 1):
    resultado_fact *= i
  return resultado_fact
num = int(input("Ingresa un número: "))
print('El factorial de', num, 'es', factorial(num))

'''Crea una función a la que se le pase un número como argumento, calcule la
cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado
total de dígitos.'''
def contar_digitos(number):
  return len(str(number))
num = int(input("Ingresa un número: "))
print('La cantidad de numeros es:', contar_digitos(num))

'''3. Dada una lista de números, crea una función que devuelva el número máximo
de la lista'''
def encontrar_max(list):
  maximo = max(list)
  return maximo
lista_numeros = [2,5,6,10,85,4]
numero_maximo = encontrar_max(lista_numeros)
print('El numero máximo es:', numero_maximo)

'''Crea una función que, dado un número, sume los dígitos de ese número y
devuelva el resultado'''
def suma_digitos(num4):
  suma = 0
  while num4 > 0:
    digito = num4 % 10
    suma += digito
    num4 //= 10
  return suma
num4 = int(input("Ingresa un número: "))
resultado_sumar_digitos = suma_digitos(num4)
print('La suma de los digitos es:', resultado_sumar_digitos)


'''Dados dos números, crea una función para encontrar el mínimo común múltiplo
(MCM) de los dos números, que se les pasarán como argumento a la función, y
devuelva el MCM'''

def calculo_mcm(a, b):
  if a > b:
    mayor = a
  else:
    mayor = b
  while True:
    if mayor % a == 0 and mayor % b== 0:
      return mayor
    mayor +=1
try:
  numero_a = int(input("Ingrese el primer número: "))
  numero_b = int(input("Ingrese el segundo número: "))
  result = calculo_mcm(numero_a, numero_b)
  print(f"El MSM de {numero_a} y {numero_b} es {result}")
except ValueError:
  print("Por favor ingrese números válidos")