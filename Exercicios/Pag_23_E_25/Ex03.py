# %%

#Faça o programa de uma sorveteria, onde o usuário pode escolher:
#Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#Sabor do sorvete: morango, creme, chocolate
#Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago

# Meu codigo
escolhaTipo = input('Escolha o tipo: [Casquinha, Cascão, Cestinha]: ')
escolhaSabor = input('Escolha o sabor: [Morango, Creme, Chocolate]: ')
escolhaCobertura = input('Escolha a cobertura: [Caramelo, Morango, Chocolate, Sem cobertura]: ')

if escolhaTipo == 'Casquinha' and escolhaSabor in ['Morango','Creme','Chocolate'] and escolhaCobertura in ['Caramelo', 'Morango', 'Chocolate']:
    print('O total é de: R$2,50')

elif escolhaTipo == 'Casquinha' and escolhaSabor in ['Morango','Creme','Chocolate'] and escolhaCobertura == 'Sem cobertura':
    print('O total é de: R$1,00 ')

elif escolhaTipo == 'Cascão' and escolhaSabor in ['Morango','Creme','Chocolate'] and escolhaCobertura in ['Caramelo', 'Morango', 'Chocolate']:
    print('O total é de: R$4,00')

elif escolhaTipo == 'Cascão' and escolhaSabor in ['Morango','Creme','Chocolate'] and escolhaCobertura == 'Sem cobertura':
    print('O total é de: R$2,50')

elif escolhaTipo == 'Cestinha' and escolhaSabor in ['Morango','Creme','Chocolate'] and escolhaCobertura in ['Caramelo', 'Morango', 'Chocolate']:
    print('O total é de: R$5,50')

elif escolhaTipo == 'Cestinha' and escolhaSabor in ['Morango','Creme','Chocolate'] and escolhaCobertura == 'Sem cobertura':
    print('O total é de: R$4,00')
else:
    print('Escolha um tipo, sabor e cobertura')

# %%

#Codigo Téo
escolhaTipo = input('Escolha o tipo: [Casquinha, Cascão, Cestinha]: ')
escolhaSabor = input('Escolha o sabor: [Morango, Creme, Chocolate]: ')
escolhaCobertura = input('Escolha a cobertura: [Caramelo, Morango, Chocolate, Sem cobertura]: ')

valor = 0

## Tipo
if escolhaTipo == 'Casquinha':
    valor = valor + 1.00

elif escolhaTipo == 'Cascão':
    valor += 2.50 ## somando o valor de 0 + 2,50

elif escolhaTipo == 'Cestinha':
    valor += 4.00

else:
    print('Escolha um tipo entre os disponiveis')



## Cobertura
if escolhaCobertura == 'Caramelo':
    valor += 1.50

elif escolhaCobertura == 'Morango':
    valor += 1.50

elif escolhaCobertura == 'Chocolate':
    valor += 1.50

elif escolhaCobertura == '':
    pass ## passa

else:
    print('Escolha uma cobertura entre os sabores disponiveis, ou não escolha nenhuma')

print('Seu sorvete', escolhaTipo, 'de', escolhaSabor, 'coberto de', escolhaCobertura, 'custará R$', valor,'.')