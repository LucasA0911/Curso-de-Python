# %%
from datetime import timedelta

sec = int(input('Digite os segundos: '))

minu = timedelta(seconds = sec, hours= 0, minutes= 0)


print(minu)

#%%

# resolução teo

segundos = int(input('digite os seguindos: '))

horas = segundos // (60*60) #horas inteiras

segundos = segundos % (60*60) # resto das horas

minutos = segundos // 60 #minutos inteiros

segundos = segundos % 60 #resto dos minutos

print(horas, minutos, segundos, sep = ':')