#%%

dados = {'nome': 'Lucas',
         'Sobrenome': 'Alves',
         'Idade': 26,
         'Cachorros': [{'nome': 'Thor',
                        'genero':'M'},

                        {'nome': 'Layla',
                         'genero': 'F'},
                         
                         {'nome': 'Zoe',
                          'genero': 'F'},
                          
                          {'nome': 'Lola',
                           'genero': 'F'}
                        ]
        }

nome = dados['nome']
print(nome)

cachorra = dados['Cachorros'][2]['nome'] #Pegando o nome da Zoe
print(cachorra)
# %%
