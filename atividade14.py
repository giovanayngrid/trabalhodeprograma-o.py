peso = float(input("Digite o peso dos peixes (em kg): "))
excesso = peso - 50 if peso > 50 else 0
multa = excesso * 4
if peso <= 50:
    print("Parabéns! Você não excedeu o limite de peso de pesca.")
else:
    print(f"Você excedeu o limite de peso em {excesso:.2f} kg.")
    print(f"A multa a ser paga é de R${multa:.2f}.")