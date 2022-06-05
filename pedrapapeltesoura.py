from lib2to3.pgen2.token import EQUAL
from operator import truediv
import random

vitoria_usuario = 0
vitoria_pc = 0
empate = 0
opcoes = ["Pedra","Papel", "Tesoura"]
opcoes[0]


while True:
    escolha_usuario = input("Escolha entre Pedra/Papel/Tesoura ou digite S para sair: ").lower()
    if escolha_usuario == "s":
        break
    
    if escolha_usuario in opcoes:
        continue
    
    random_number = random.randint(0,2)
    # pedra: 0, papel: 1, tesoura:2
    
    escolha_pc = opcoes[random_number]
    print("o computador escolheu:", escolha_pc + ". ")

        
    if escolha_usuario == "pedra" and escolha_pc == "Tesoura":   
        print("Você ganhou!!")
        vitoria_usuario +=1
    
    elif escolha_usuario == "papel" and escolha_pc == "Pedra":   
        print("Você ganhou!!")
        vitoria_usuario +=1
        
    
    elif escolha_usuario == "tesoura" and escolha_pc == "Papel":   
        print("Você ganhou!!")
        vitoria_usuario +=1
    # não é necessario checar as escolhas do computador, uma vez que se nenhuma das tres condições é verdadeira é impossivel o usuário ter ganhado.
    
    else:
        print("Você perdeu :(")
        vitoria_pc +=1
        
    print("Suas vitórias:", vitoria_usuario)
    print("Vitórias do computador:", vitoria_pc) 
    print("obrigada por jogar :) volte sempre!")