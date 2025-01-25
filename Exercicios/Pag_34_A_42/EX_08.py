#%%
#Faça um programa que receba um número. Verifique se este número é primo ou não, e retorne o resultado:


def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isprime(number):
    numeros = []
    for i in range(2, number + 1):
        if prime(i):
            numeros.append(i)

    if number in numeros:
        print('O número', number, 'é primo')
    else:
        print('O número', number, 'não é primo')

numero = int(input('Insira o número: '))

isprime(numero)
# %%
