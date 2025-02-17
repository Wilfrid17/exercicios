# faça um programa que calcule 10% de desconto de um produto comprando mais R$100 ou ter cupon de desconto: DESC10

valor_total = float(input("Digite o vslor da compra: R$"))
quantidade_itens = int(input("Digite quantidade da compra: "))
coupon_desconto = input("Digite o cupom de desconto (se houver): ").strip()

if valor_total >= 100 and quantidade_itens > 1:
    print("Parabens você ganhou 10% de desconto comprando mais de 2 podutos")
    desconto = valor_total * 0.10
    valor_final = valor_total - desconto
    print(f"O valor de desconto é: R$ {desconto}")
    print(f"O valor total apagar é: R${valor_final:.2f}")

elif coupon_desconto == "SIM":
    print("Parabens você ganhou 10% de desconto usando coupon de desconto")
    desconto = valor_total * 0.10
    valor_final = valor_total - desconto
    print(f"O valor de desconto é: R$ {desconto}")
    print(f"O valor total apagar é: R${valor_final:.2f}")
else:
    print(f"O valor apagar sem deconto é R${valor_total:.2f}")