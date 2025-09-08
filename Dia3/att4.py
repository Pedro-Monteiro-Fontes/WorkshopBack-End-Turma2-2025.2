numeros = [10, 20, 30]
try: 
  indice = int(input("Digite um índice para acessar a lista: ")) 
  print(f"Posição da lista:{indice}")
except IndexError:
  print("Não tem esse valor na lista")
    
#IndexError: list index out of range 

# Evitar o código quebrar caso o usuário colocar um valor inválido