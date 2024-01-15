# km percorridos e dias

print("Bem vindo a Aluga Autos!")

dias = int(input("Dias alugados: "))
kmh = float(input("Km percorridos: "))

valor = (dias * 24 * 60) + (kmh * 0.15)

print(f"Total a pagar: R$ {valor} ")