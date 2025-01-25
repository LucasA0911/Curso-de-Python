# %%

#Faça um programa que receba uma quantidade indefinida de valores correspondentes a “saldo em conta”, mas quando o usuário apertar “enter” sem digitar valor algum, o programa para de receber valores, e exibe a soma te todos os valores digitados anteriormente.

lista = [0]
soma = 0
while True:
    valor = input('insira um valor: ')

    if valor == '':
        for i in lista:
            soma += i
        print(soma)
        break

    else:
        valor = int(valor)
        lista.append(valor)
        continue
# %%
