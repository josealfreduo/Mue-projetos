moeda=float(input("Quanto dinheiro voçe tem na carteira R$: "))
dolar = moeda / 4.89
print("Com R${} voce pode comprar US${:.2f}".format(moeda, dolar))