# algoritmo que escolhe um nome aleatório no TXT para encontrar um redator e orador para a reunião

import random

# abrindo o arquivo
with open('Nomes.txt', 'r') as f:
    # lendo o arquivo
    nomes = f.readlines()

# Removendo o '\n' de cada nome
nomes = [nome.strip() for nome in nomes]


# Pessoas fora da lista

# caso tenha faltantes 
faltantes = input('Digite o nome dos faltantes: (com um espaço entre eles "Maria José Alice") ')
faltantes = faltantes.split()

# Pessoas escolhidas anteriormente
with open('Last_reunion.txt', 'r') as f:
    Nomes_anteriores = f.readlines()

# Removendo o '\n' de cada nome
Nomes_anteriores = [nome.strip() for nome in Nomes_anteriores]

# juntando os faltantes e os nomes anteriores
Escaparam = faltantes + Nomes_anteriores

# Removendo os faltantes e os nomes anteriores da lista de nomes
for escapou in Escaparam:
    if escapou in nomes:
        nomes.remove(escapou)


# escolhendo dois nomes aleatório que estão presentes na reunião
orador = random.choice(nomes)
nomes.remove(orador) # não escolher o orador novamente

redator = random.choice(nomes)

# guarda os nomes do orador e redator para que em uma próxima reunião não sejam escolhidos novamente
with open('Last_reunion.txt', 'w') as f:
    pass    # deleta conteúdo antigo do arquivo
    f.write(f'{orador}\n{redator}')
    

# exibindo os nomes escolhidos
print("\nO orador da reunião será: " + orador)
print("\nO redator da reunião será: " + redator)