import os
import time



def abertura():
    print("Bem vindo ao Jogo da Forca!")

def limparTela():
    os.system('cls')

def tempo(tempo):
    time.sleep(tempo)

def opcao():
   print("Jogar (0) Dica (1)")
   a = input()
   return a

def localizar(texto,palavra):
        posicoes = []
        for i in range(0,len(palavra)):
            if texto[i] == palavra:
                posicoes.append(i)
        return posicoes


      
def vencedor(palavra):
  print("Mandou bem! Você conseguiu fugir da forca!")
  print("A palavra era {}".format(palavra))

def perdedor(palavra):
  print("Não foi dessa vez... você foi enforcado!")
  print("A palavra era {}".format(palavra))

def desenho(erros):
    if(erros == 0):
      print("Tudo tranquilo...")
    elif(erros == 1):
      print("O")
    elif(erros== 2):
      print("O")
      print("|")
    elif(erros== 3):
      print(" O ")
      print("-|-")
    elif(erros== 4):
      print(" O ")
      print("-|-")
      print(" | ")
    else:
      print(" O ")
      print("-|-")
      print(" | ")
      print("/ \ ")
      print("Oh não!")

            