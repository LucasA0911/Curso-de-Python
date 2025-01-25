#%%
#Faça um programa que receba o nome e a idade de uma pessoa. 

name = input('Qual é o seu nome?')
age = int(input('Qual é a sua idade? '))

if age < 18:
    print(name, 'você não pode dirigir e nem beber')
elif age < 65:
    print(name, 'bebida liberada! Só não valde dirigir!')
else:
    print(name, 'tu é velho, melhor beber com cuidado!')
# %%
