import math 

def arredondamento(num: float) -> dict: 
  return {
    "piso": math.floor(num),
    "teto": math.ceil(num),
    "arredondao": round(num)
  }

valor = float(input("Coloque um número quebrado: "))
resultado = arredondamento(valor)

print(resultado)
