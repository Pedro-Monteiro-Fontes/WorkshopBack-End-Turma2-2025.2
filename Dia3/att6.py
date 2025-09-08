dados = {
    "nome": "Pedro ",
    "idade": 18,
    "cidade": "Campo Grande" 
}
try:
  chave = dados.get(input("Digite a chave que deseja acessar: "), "Dado inexistente")
  print(chave)
except KeyError:
  print("Essa chave não existe")

# Caso o usuário digitar uma chave não existente,

# KeyError