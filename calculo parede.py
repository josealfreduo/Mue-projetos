larg=float(input("Qual a largura da parede: "))
alt=float(input("Qual a altura da parede: "))
print("A dimenção da parede é {} X {}".format(larg,alt))
area = larg*alt
print("A área é de {}m²".format(area))
tin = area / 2
print("Para pintar voce vai precisar de {}L de tinta".format(tin))