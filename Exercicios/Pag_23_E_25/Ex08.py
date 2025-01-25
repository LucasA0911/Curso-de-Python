# %%

#Faça um programa que receba 4 alturas, armazene em uma lista e depois mostre a soma dessas alturas.

lista = [0]
valores = []
conta = 0
for x in range(4):
    altura = int(input('Digite o valor da altura: '))
    valores.append(altura)
    lista.append(altura)
    conta = lista[-2] + lista[-1]
    lista.clear()
    lista.append(conta)
print('A soma das alturas é:', valores, 'é:',lista[0])