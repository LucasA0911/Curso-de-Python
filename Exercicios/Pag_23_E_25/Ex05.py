# %%
#Faça um programa que verifique se a pessoa pertence à família “calvo” ou "silva".

nome = input('Digite seu nome Completo: ')
nome = nome.lower()
if 'calvo' in nome or 'silva' in nome:
    print('Você faz parte da familia Calvo, ou da familia silva')

else:
    print('Você não faz parte da familia Calvo, e nem da familia silva')

#%%

while True:
    nome = input('Digite seu nome Completo: ')

    nome = nome.lower()

    if 'calvo' in nome and 'silva' in nome:
        print('Você é da familia calvo e da familia silva')
        break
    
    elif 'calvo' in nome:
        print('Você é da familia calvo')
        break

    elif 'silva' in nome:
        print('Você é da familia silva')
        break
    
    else:
        print('Você não faz parte de nenhuma das familias')
        continue