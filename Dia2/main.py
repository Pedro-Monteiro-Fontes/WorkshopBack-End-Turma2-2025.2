import math 

def calcular_raiz(numero:  float) -> float:
  return math.sqrt(numero)

def main():
  valor = float(input("Digite um número: "))
  resultado = calcular_raiz(valor)
  return f"A raiz quadrada do {valor} é:  {resultado}"

print(main())