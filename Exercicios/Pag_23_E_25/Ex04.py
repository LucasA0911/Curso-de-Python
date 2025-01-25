# %%
#Faça um programa que verifique se a pessoa pertence à família “calvo”.

nome = input('Digite seu nome completo: ')

nome = nome.lower()

if 'Calvo' in nome:
    print('Você faz parte da familia Calvo')

else:
    print('Você não faz parte da familia Calvo')

#%%


while True:
    nome = input('Digite seu nome completo: ')

    nome = nome.lower()
    
    if 'Calvo' in nome:
        print('Você é da familia Calvo')
        break

    else:
        print('Você não faz parte da familia Calvo')
        continue