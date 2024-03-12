LITROS_POR_METRO_QUADRADO = 1 / 6
LATA_LITROS = 18
LATA_PRECO = 80
GALAO_LITROS = 3.6
GALAO_PRECO = 25
area_metros_quadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
litros_tinta = area_metros_quadrados * LITROS_POR_METRO_QUADRADO * 1.1
latas_necessarias =(litros_tinta / LATA_LITROS)
preco_total_latas = latas_necessarias * LATA_PRECO
galoes_necessarios =(litros_tinta / GALAO_LITROS)
preco_total_galoes = galoes_necessarios * GALAO_PRECO
litros_em_galoes =(litros_tinta / GALAO_LITROS) * GALAO_LITROS
galoes_necessarios = litros_em_galoes / GALAO_LITROS
litros_em_latas = litros_tinta - litros_em_galoes
latas_necessarias =(litros_em_latas / LATA_LITROS)
preco_total_misturado = galoes_necessarios * GALAO_PRECO + latas_necessarias * LATA_PRECO
print("Situação 1: Comprar apenas latas de 18 litros")
print(f"Quantidade de latas: {latas_necessarias}")
print(f"Preço total: R${preco_total_latas:.2f}")
print("Situação 2: Comprar apenas galões de 3,6 litros")
print(f"Quantidade de galões: {galoes_necessarios}")
print(f"Preço total: R${preco_total_galoes:.2f}")
print("Situação 3: Misturar latas e galões")
print(f"Quantidade de galões: {galoes_necessarios}")
print(f"Quantidade de latas: {latas_necessarias}")
print(f"Preço total: R${preco_total_misturado:.2f}")
