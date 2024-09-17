## 1️⃣ Desafio Classificador de nível de Herói

#**O Que deve ser utilizado**

#- Variáveis
#- Operadores
#- Laços de repetição
#- Estruturas de decisões

## Objetivo

#Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

#Se XP for menor do que 1.000 = Ferro
#Se XP for entre 1.000 e 1.999 = Bronze
#Se XP for entre 2.000 e 4.999 = Prata
#Se XP for entre 5.000 e 6.999 = Ouro
#Se XP for entre 7.000 e 7.999 = Platina
#Se XP for entre 8.000 e 8.999 = Ascendente
#Se XP for entre 9.000 e 9.999 = Imortal
#Se XP for maior ou igual a 10.000 = Radiante

## Saída

#Ao final deve se exibir uma mensagem:
#"O Herói de nome **{nome}** está no nível de **{nivel}**"

heroi = [
    ["Marcos", 15000],
]
#    ["Richard", 4385],
#    ["Alfred", 100000000]
while True:
    if (heroi[0][1]) < 1000:
        nivel_heroi = "Ferro"
    elif (heroi[0][1]) >= 1000 and (heroi[0][1]) < 2000:
        nivel_heroi = "Bronze"
    elif (heroi[0][1]) >= 2000 and (heroi[0][1]) < 5000:
        nivel_heroi = "Prata"
    elif (heroi[0][1]) >= 5000 and (heroi[0][1]) < 7000:
        nivel_heroi = "Ouro"
    elif (heroi[0][1]) >= 7000 and (heroi[0][1]) < 8000:
        nivel_heroi = "Platina"
    elif (heroi[0][1]) >= 8000 and (heroi[0][1]) < 9000:
        nivel_heroi = "Ascendente"
    elif (heroi[0][1]) >= 9000 and (heroi[0][1]) < 10000:
        nivel_heroi = "Imortal"
    else:
        nivel_heroi = "Radiante"
    break

verificar = str(input("Deseja verificar o nível de seu heroi? \nS para sim \nN para não \nS/N? "))
if verificar == "S" or "s":
 print(f"O herói de nome {heroi[0][0]} está no nível de {nivel_heroi}")
