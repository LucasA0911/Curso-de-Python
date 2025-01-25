# %%

#Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

frase = input('Digite a frase: ')
quantidade = frase.count('a')
print(quantidade)

# %%

frase = input('Digite a frase: ')

count = 0
for i in frase:

    if i != 'a':
        continue
    elif i == 'a':
        count += 1
    print(count)