print('=-'*20)
print("SISTEMA DE DESCONTO DO ZEZIN")
print('=-'*20)

# Perguntar o valor a ser pago
valor = float(input("Qual o valor a ser pago em R$: "))

# Aplicar condição
print("""Escolha o método de pagamento
[1] À VISTA / + 31 DIAS
[2] À VISTA / - 31 DIAS
[3] PARCELADO EM 2X
[4] PARCELADO EM 3X""")
resposta = input("Digite a opção desejada: ")

# Se avista + 30 dias
if resposta == '1':
    ad = 30 * valor / 100
    a = valor - ad
    print("O valor é R$ {}".format(valor))
    print("Seu desconto com o pagamento à vista de R$ {}".format(ad))
    print("A conta total é de {}".format(a))

# Se avista - 30 dias
elif resposta == '2':
    ac = 20 * valor / 100
    b = valor - ac
    print("O valor da sua conta é R$: {}".format(valor))
    print("O seu desconto com o pagamento à vista é de R$ {}".format(ac))
    print("O total do débito é de R$ {}".format(b))

# Em 2x + entrada
elif resposta == '3':
    porcentagem_entrada = float(input("Qual a porcentagem de entrada (0-100): "))
    entrada = valor * (porcentagem_entrada / 100)
    print("O valor da sua conta é de R$ {}".format(valor))
    print("O valor da entrada é de R$ {}".format(entrada))
    o = valor - entrada
    f = o / 2
    print("O valor é 2x de R$ {}".format(f))

# 3x + entrada
elif resposta == '4':
    porcentagem_entrada = float(input("Qual a porcentagem de entrada (0-100): "))
    entrada = valor * (porcentagem_entrada / 100)
    print("O valor da sua conta é de R$ {}".format(valor))
    print("O valor da entrada é de R$ {}".format(entrada))
    l = valor - entrada
    f = l / 3
    print("O valor fica 3x de R$ {}".format(f))
