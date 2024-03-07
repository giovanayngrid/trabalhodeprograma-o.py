area_metros_quadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
litros_tinta = area_metros_quadrados / 3
latas_tinta =(litros_tinta / 18)
preco_total = latas_tinta * 80
print(f"Quantidade de latas de tinta: {latas_tinta}")
print(f"Preço total: R${preco_total:.2f}")