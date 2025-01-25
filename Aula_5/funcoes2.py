#%%
def soma (*num): # define que se pode passar quantos argumentos quiser no parâmetro
    total = 0
    
    for i in num:
        total +=i
    
    return total

soma(1,2,3,4,5,6,7,8,9,10)
# %%

def operacao(op, *num):#Criando várias operações matematicas em uma unica função
    total = 0
    
    if op == 'soma':
        for i in num:
            total += i

    elif op == 'mult':
        total = 1
        for i in num:
            total *= i

    return total

operacao('mult',1,2,3,4,5,6,7,8,9,10)
# %%

dados = ['Lucas', 'Alves'] 

nome, sobrenome = dados #unpack de listas só funciona se todos os valores dentro da lista estiverem declarados como variáveis
print(nome)
print(sobrenome)
# %%

dados = ['Lucas', 'Alves', 26,'zoe','thor'] 

nome, *_, cachorro = dados # O "*_" serve para armazenar o aquilo que eu não quero, pode colocar aonde eu quiser e só pode ter 1
print(nome)
print(cachorro)

#%%
a = 10
b = 20
print(a,b)

a,b = b,a # inverter os valores das váriaveis
print(a,b)
# %%
