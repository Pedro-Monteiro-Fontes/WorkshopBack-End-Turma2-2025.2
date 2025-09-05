class Animais:
  def __init__(self, nome, idade, som):
    self.nome = nome
    self.idade = idade
    self.som = som
  def apresentar(self):
    return f"Eu sou {self.nome}, tenho {self.idade} anos .... {self.som}"
  
class Gatinho(Animais):
  def som(self):
    return "Miau Miau"
  def __init__(self, nome, idade, som):
    super().__init__( nome, idade, som)
  
class Cachorro(Animais):
  def som(self):
    return "AUUU Au"
  def __init__(self, nome, idade, som):
    super().__init__(nome, idade,som )

Cachorro_dados = Cachorro("Apollo", 5, "AUUUU Au") 
Gatinho_dados = Gatinho("Atriuz", 3, "MIAUU Miau")

print(Gatinho_dados.apresentar())
print(Cachorro_dados.apresentar())
