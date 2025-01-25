# %%

#Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista: laranja, cerveja, miojo, carvão, picanha.

item = input('Digite o item a ser verificado: ')

lista = ['Laranja', 'Cerveja', 'Miojo', 'Carvão', 'Picanha']

if item in lista:
    print('O item: ', item, ' está na lista.')
else:
    print('O item: ', item, ' não está na lista.')