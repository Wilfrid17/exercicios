nota = float(input("Digite o valor da nota: "))
falta = 20

if nota >= 70 and falta <= 20:
    print("Voce foi aprovado")
elif nota < 70 and falta < 20:
    print("Você foi repovado por nota")
elif nota > 70 and falta > 20:
    print("Você foi reprovado por falta")
elif nota < 70 and falta > 20:
    print("Você foi reprovado por nota e por falta")