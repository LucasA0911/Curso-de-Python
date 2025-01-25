# %%

#Faça um programa que vende uma garrafa de água:
#Se o cliente escolher água mineral natural, será cobrado R$1,50
#Se o cliente escolher água mineral com gás, será cobrado R$2,50

escolha = input('Qual água você gostaria de pedir? [mineral/gas]')

if escolha == 'mineral':
    print('O valor da água é R$1,50')
elif escolha == 'gas':
    print('O valor é de R$2,50')
else:
    print('Escolha entre [mineral ou gas]')