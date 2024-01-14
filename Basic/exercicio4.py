# INPUT 

name = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
sexo = str(input("Digite seu sexo 'm' ou 'f': "))

if(idade>=18) and (sexo == 'm'):
    print(f"Bem vindo {name}! Vc pode se alistar!")
else:
    print("Nao pode se alistar")


