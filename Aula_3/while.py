#%%
count = 1
while count <= 10:
    print('ola')
    count += 1

#%%

#break

while True:
    senha = input('Digite a senha: ')

    if senha == 'lucas':
        break
    else:
        print('senha incorreta')

print('Bem vindo!')

#%%

# continue

while True:
    senha = input('Digite a senha: ')

    if senha == 'lucas':
        break
    elif senha == 'luquinhas':
        print('quase')
        continue

    print('senha incorreta')

print('Bem vindo!')

#%%

count = 1

while count <= 15:
    if count % 2 == 0:
        print(count)

    count +=1