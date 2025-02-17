#faça um programa que recebe o salario de um colaborador e o reajuste segundo o seguinte critério, baseado no salario atual 
# . Salários até R$ 1.280,00 (incluindo): aumento de 20% 
# . Salários entre R$1.280,oo até 1.700,00 : aumento de 15% 
# . Salários R$1.700,00 até 2.500,00 aumento 10% 
# . Salários R$2.500,00 em diante : aumento de 5% 

# Após aumento ser realizado ,informe na tela 
# . salário antes do reajuste; 
# percentuaal de aumento aplicado; 
# valor do aumento; 
# novo salário após o aumento.

salario = float(input("Salário do colaborador: R$ "))

if salario <= 1280:
    print("aumento de 20%")
    aumento = salario * 0.20
    salario_reajuste = (salario * 0.20) + salario
    print(f"O seu aumento é R${aumento}")
    print(f"Seu novo salario com reajuste é R${salario_reajuste:.2f}")
elif salario >= 1280 and salario <= 1700:
    print("aumento 15%")
    aumento = salario * 0.15
    salario_reajuste = (salario * 0.15) + salario
    print(f"O seu aumento é {aumento}")
    print(f"Seu novo salario com reajuste é R${salario_reajuste:.2f}")
elif salario >= 1700 and salario <= 2500:
    print("aumento de 10%")
    aumento = salario * 0.10
    salario_reajuste = (salario * 0.10 )+ salario
    print(f"O seu aumento é R${aumento}")
    print(f"o seu salário com reajuste é R$ {salario_reajuste:.2f}")
elif salario > 2500:
    print("aumento 5%")
    aumento = salario * 0.5
    salario_reajuste = (salario * 0.5) + salario
    print(f"O seu aumento é R$ {aumento}")
    print(f"O seu novo salario com reajuste é R$ {salario_reajuste}")
else:
    print("Nenhum dados informados!")

