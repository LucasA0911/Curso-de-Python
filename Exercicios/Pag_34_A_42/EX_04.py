#%%
#Faça um programa que receba 4 notas de um aluno. Retorne a média dessas notas, a menor e a maior nota:

notas = []
for i in range(4):
    nota = int(input('Insira a nota: '))
    notas.append(nota)

media = sum(notas)/4
print('A média das notas é: ', media, '.',)
maior = max(notas)
print('A maior nota é: ', maior, '.',)
menor = min(notas)
print('A menor nota é: ', menor, '.',)
# %%
