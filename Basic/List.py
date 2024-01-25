# Media 

list = [10,9,8,10,9,8,5]

soma = 0
x = 0

size = len(list)

while x < size: 
    soma +=list[x]
    x += 1 

print(f"Soma = {soma/size:5.2f}")


while True:
    escolhido = int(input("Qual posicao vc quer imprimir? (0 para sair): "))
    if escolhido == 0:
        break
    print(f"Vc escolheu o {list[escolhido-1]}")