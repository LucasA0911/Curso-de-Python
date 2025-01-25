#%%
import random

def check_number():
      """ Verifica se o número colocado é um inteiro"""
      
      while True:
        try:
            return int(input('Insira um número de 1 a 15: '))

        except ValueError as err:
            return 'Digite um número, e não letras!' 

def check_interval(numero):
    """Verifica se o número colocado está entre 1 e 15"""
    
    return 1 <= numero <= 15
    
def valida():
    """Valida se num úmero é um inteiro, e se o numero digitado está dentro do intervalo """
    
    while True:

        numero = check_number()

        if type(numero) != int:
            print(numero)
            continue

        if check_interval(numero):
            return numero
        
        
numero_sorteado = random.randint(1,15)

for i in range(3):
    
    numero = valida()

    if numero == numero_sorteado:
        print('Acertou!')
        break

    elif numero > numero_sorteado:
        print('Errou! Tente um número menor.')
    else:
        print('Errou! Tente um número maior.')

# %%
