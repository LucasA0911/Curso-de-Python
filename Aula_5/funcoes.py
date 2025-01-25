#%%
"""
y = f(x) = x + 10
----------------
y = f(x) = x*x + 1
"""
def f(x):
    res = x + 10
    return res

y = f(10)
print(y)

#%%
def soma(a,b=0): #definindo um argumento opcional padrão "Default". Não pode definir o padrão no "a", pois o primeiro argumento é sempre obrigatório.
    return a + b
soma(10,10)
# %%

soma(a=10, b=10) # se o parametro for definido no primeiro argumento, todos os demais também precisaram ser definidos.

soma(10,b=10) # se o primeiro argumento for posicinal, os demais também serão, mesmo que seja definido com outro valor