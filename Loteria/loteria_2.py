#%%
numero_sorteado = 5

for i in range(3):
    
    while True:
        try:
            numero = int(input('Insira um número de 1 a 15'))
            break

        except ValueError as err:
            print('Digite um número, e não letras!')

    if numero == numero_sorteado:
        print('acertou!')
        break

    elif numero > numero_sorteado:
        print('Errou! Tente um número menor.')
    else:
        print('Errou! Tente um número maior.')
# %%
