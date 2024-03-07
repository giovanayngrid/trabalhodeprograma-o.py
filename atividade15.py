valor_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))
salario_bruto = valor_hora * horas_trabalhadas
inss = salario_bruto * 0.08
irpf = salario_bruto * 0.11
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - inss - irpf - sindicato
print(f"Salário bruto: R${salario_bruto:.2f}")
print(f"INSS: R${inss:.2f}")
print(f"IRPF: R${irpf:.2f}")
print(f"Sindicato: R${sindicato:.2f}")
print(f"Salário líquido: R${salario_liquido:.2f}")