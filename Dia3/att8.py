def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    return soma / quantidade
try:
  notas = [8, 7, 9, 2]
  media = calcular_media(notas)
  print(f"Média: {media:.2f}")
except ZeroDivisionError:
   print("Média inválida, Divisão por 0")
