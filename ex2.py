temperatura = float(input("Informa temperatura atual: "))

if temperatura < 10:
    print("Esta muito frio")
elif 10 <= temperatura < 20:
    print("Esta modelada")
else: 
    print("Esta muito quente")