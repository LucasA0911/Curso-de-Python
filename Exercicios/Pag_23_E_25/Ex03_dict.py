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

valor = 0
sorvetes = {'Casquinha': 1.00,
            'Cascão': 2.50,
            'Cestinha':4.00}

valor += sorvetes[escolhaTipo]

sabor = {'Morango': 0,
         'Creme': 0,
         'Chocolate': 0}

valor += sabor[escolhaSabor]

cobertura = {'Caramelo': 1.50,
             'Morango': 1.50,
             'Chocolate':1.50,
             'Sem cobertura': 0}

valor +=cobertura[escolhaCobertura]


print(f'Seu sorvete', escolhaTipo, 'de', escolhaSabor, 'com', escolhaCobertura, 'ficou', valor,'R$')
print('Escolha um tipo, sabor e cobertura')


# %%
