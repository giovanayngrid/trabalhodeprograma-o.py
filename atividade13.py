def calcular_peso_ideal(altura, sexo):
  if sexo == 1:
    return 62.1 * altura - 44.7
  elif sexo == 2:
    return 72.7 * altura - 58
  else:
    return None

altura = float(input("Qual sua altura? "))
sexo = int(input("Qual seu sexo? (Feminino digite 1/Masculino digite 2) "))

peso_ideal = calcular_peso_ideal(altura, sexo)

if peso_ideal is not None:
  print("O seu peso ideal de acordo com sua altura de {}cm e sexo {} é de {}kg".format(altura, "feminino" if sexo == 1 else "masculino", peso_ideal))
else:
  print("Sexo inválido.")