km=float(input("Quantos Km foi rodado com o carro?: "))
dia=int(input("Por quantos dias voçe ficou com o carro?: "))
dist = km * 0.15
diaria = dia * 60
print("O custo total da diaria foi {}R$\nO custo da quilometragem foi: {}R$".format(diaria,dist))
total = dist + diaria
print("O total foi: {}R$".format(total))