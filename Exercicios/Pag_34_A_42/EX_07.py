#%%
#Escreva um programa que crie um dicionário com nomes de frutas como chaves e seus respectivos preços como valores. Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

fruta = input('Qual fruta você deseja saber o valor? ')
frutas = {  'Maçã': 1.50,
            'Banana': 2.75,
            'Uva': 1.90,
            'Pera': 1.25,
            'Laranja': 0.65,
            'Limão': 1.25,
            'Goiaba': 2.15,
            'Abacaxi': 3.20,
            'Jaca': 5.80
        }

if fruta in frutas:
    valor = frutas[fruta]
    print('O valor da',fruta, 'é: R$', valor)
else:
    keys = frutas.keys()
    print('No momento não possuimos esta fruta em estoque, escolha entre uma dessas frutas: ',list(keys))
# %%
