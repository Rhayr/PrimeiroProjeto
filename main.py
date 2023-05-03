#teste3
import os
import time
import getpass
import netrc
from funcoes import limparTela, abertura, tempo, opcao, vencedor, perdedor, desenho

palavra = ""
acertos = 0
tentar = 5
erros = 0
acerto = False
letras = ""
letra = ""
letraFinal = ""
dica = 3

abertura()
tempo(2)
limparTela()

desafiante = (str(input("Nome do desafiante: ")))
competidor = (str(input("Nome do competidor: ")))

limparTela()

try:
    palavra = str(input("Escolha uma palavra: ")).upper()
    while palavra.isnumeric():
        print(" Palavra inválida. Por favor, tente novamente...")
        palavra = str(input("Escolha uma palavra: ")).upper()
except ValueError:
    print("Valor inválido.")

try: 
    dicaUm = str(input("Dica 1: "))
    while dicaUm.isnumeric():
        print(" Dica inválida. Por favor, tente novamente...")
        dicaUm = str(input("Dica 1: ")).upper()
except ValueError:
    print("Dica inválida.")
try:
    dicaDois = str(input("Dica 2: "))
    while dicaDois.isnumeric():
        print(" Dica inválida. Por favor, tente novamente...")
        dicaDois = str(input("Dica 2: ")).upper()
except ValueError:
    print("Dica inválida.")
try: 
    dicaTres = str(input("Dica 3: "))
    while dicaTres.isnumeric():
        print(" Dica inválida. Por favor, tente novamente...")
        dicaUm = str(input("Dica 3: ")).upper()
except ValueError:
    print("Dica inválida.")

limparTela()

opcao()

tam = len(palavra)
copiaPalavra = list()
for i in palavra:
    copiaPalavra.append(i.replace(i, "_")) 

while acertos < tam or tentar < 5:
    print("\nPalavra é: ", end='')
    for item in copiaPalavra:
        print(f"{item}", end=' ')
    print("\033[m")
    break

try:
  letra = str(input("Digite uma letra: ")).upper()[0]
  letras += letra
  while letra.isnumeric():
    print("Letra inválida. Tente de novo!")
    letra = str(input("Digite uma letra: ")).upper()[0]
    letras += letra
except ValueError():
        print("Valor Inválido.")

for i, value in enumerate(palavra):
        if value == letra:
            print(f"Letra [{letra}] encontrada com sucesso.")
            copiaPalavra[i] = letra
            acerto = True
            acertos += 1

if tentar == 0:
  perdedor()

if acertos == tam:
  vencedor()

deNovo = (int(input("Gostaria de jogar de novo? (0) Não (1) Sim")))
soma = (deNovo + 0)
if soma == 0:
  close()
if soma == 1:
  limparTela()

arquivo = open("historico.txt", "a")
arquivo.write(palavra + desafiante + competidor )
