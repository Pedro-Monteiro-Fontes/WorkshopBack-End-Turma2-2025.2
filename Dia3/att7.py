def validar_idade(idade):
    if idade < 0 or idade > 120:
       return ("Idade Inválida")
    else:
        return(f"Idade válida: {idade} !")

idade = int(input("Digite sua idade: "))
print(validar_idade(idade))
