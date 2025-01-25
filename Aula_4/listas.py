#%%
#append

notas = []
nota = 7.75

notas.append(nota) #Adiciona um elemento no final da lista
print(notas)

#%%
#extend

notas.extend([5.75, 6.24]) #Permite que adicione mais de um valor em uma lista. Caso ele seja utilizado para adicionar elementos que não sejam uma lista, ele vai adicionar cada iteravel do elemento. EX: 'Lucas' = 'L','u','c','a','s'
print(notas)

#%%
#Concatenação

notas = notas + [10, 9.25] #Concatenação de listas
print(notas)

# %%
