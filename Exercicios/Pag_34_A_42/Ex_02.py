#%%
#Faça um programa que receba um número. Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:

#	O número x é impar
#ou
#	O número x é par

numero = int(input('Insira o número: '))

if numero % 2 == 0:
    print('O', numero, 'é par')
else:
    print('O', numero, 'é impar')
# %%
