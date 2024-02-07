print('=-'*20)
print("MERCADO DO ZEZIN")
print('=-'*20)
#perguntar o valor a ser pago
valor = float(input("Qual o valor a ser pago em R$: "))
#aplicar condição
print("""Escolha o metodo de pagamento
[1] AVISTA / dinheiro ou cheque
[2] AVISTA no cartão
[3] 2x no CARTÃO
[4] 3x ou mais no CARTÃO""")
resposta = str(input("Digite a opção desejada: "))
#se avista/cheque - 10% desc
if resposta == '1':
    ad = 10*valor/100
    a = valor - ad
    print("O valor é R$ {}".format(valor))
    print("Seu desconto com o pagamento a vista ou cheque é de  R${}".format(ad))
    print("A conta total é de {}".format(a))
#se avista no catao - 5% de esc
elif resposta == '2':
    ac = 5*valor/100
    b = valor - ac
    print("O valor da sua conta é R$: ".format(valor))
    print("O seu desconto com o pagamento a vista no cartão é de  R$ {}".format(ac))
    print("A conta total é de  R$ {}".format(b))
# em 2x no cartão - normal
elif resposta == '3':
    print("Você não obteve desconto")
    print("O valor da sua conta é de R$ {}".format(valor))
# 3x ou + 20% juros
elif resposta == '4':
    ab = 20*valor/100
    c = valor + ab
    print("O valor da sua conta é de R$ {}".format(valor))
    print("Com essa forma de pagamento aplica-se juros de 20%")
    print("O valor fica R$ {}".format(c))
    print("O juros é de R$ {}".format(ab))