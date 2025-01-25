# %%

#Faça um programa que vende uma garrafa de água:
#Se o cliente escolher água mineral natural, será cobrado R$1,50
#Se o cliente escolher água mineral com gás, será cobrado R$2,50
#Altere o programa anterior para considerar a quantidade de água

escolha = input('Qual água você gostaria de pedir? [mineral/gas]')
quantidade = int(input('Quantas águas você quer?'))

if escolha == 'mineral' and quantidade >= 1:
    total = 1.50*quantidade
    print('O valor da água é: ', total)
elif escolha == 'gas' and quantidade >= 1:
    total = 2.50*quantidade
    print('O valor é de ', total)
else:
    print('Escolha entre [mineral ou gas], e 1 ou mais águas')