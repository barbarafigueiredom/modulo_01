import os

os.system('clear')

print("Pense em um número de 1 a 10...")
input("Quando estiver pronto, aperte Enter.")

os.system('clear')
print("Estou lendo sua mente...")
input()

print("Seu número é... 7!")
resposta = input("Acertei? 😄 (s/n:) ")

numero = 7

while True:
    if resposta.lower() == "s":
        print("Ebaaaa!! 😀 Acertei!")
        break
    else: 
        if resposta.lower () == "n":
            print("Poxa... não foi dessa vez!😢")
        break