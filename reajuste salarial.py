salario=float(input("Qual o seu salario atual R$: "))
nvsalario = salario*15/100
atual = salario + nvsalario
print("Seu salario é R$:{} ".format(salario))
print("Com o ajuste de 15% seu sálario passa a ser R$: {:.2f}".format(atual))
print("O ajuste foi um acrecimo de R$: {:.2f}".format(nvsalario))