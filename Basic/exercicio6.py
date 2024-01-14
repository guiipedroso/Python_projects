
dia = int(input("Dia(s): "))
hora = int(input("Hora(s): "))
minuto = int(input("Minuto(s): "))
segundo = int(input("Segundo(s): "))

total = (dia * 24 * 3600) + (hora * 3600 ) + (minuto * 60) + (segundo)

print(f"Total em segundos: {total}")