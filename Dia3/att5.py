def dividir(a, b):
    return a / b
try:
  num1 = input("Digite o primeiro número: ")
  num2 = input("Digite o segundo número: ")
  resultado = dividir(int(num1), int(num2))
  print(f"Resultado: {resultado}")
except ValueError:
   print("Não foi possivel realizar a divisão")
except ZeroDivisionError:
   print("Não é possivel realizar uma divisão por 0 ")

# Erro em divisão por 0, string, números quebrados

# Evitando o código quebrar, usei o try para retornar o erro para o usuário