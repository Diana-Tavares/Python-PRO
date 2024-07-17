from random import randint
from time import sleep
import random


def pedra_papel_tesoura():
    jogada = input("Escolha entre Pedra, Papel ou Tesoura: ").lower()
    jogada2 = randint(0, 2)
    lista = ["pedra", "papel", "tesoura"]
    print(lista[jogada2])

    if jogada == lista[jogada2]:
        print("Empate.")
    elif jogada == "papel" and lista[jogada2] == "pedra":
        print("Ganhou o utilizador.")
    elif jogada == "pedra" and lista[jogada2] == "tesoura":
        print("Ganhou o utilizador.")
    elif jogada == "tesoura" and lista[jogada2] == "papel":
        print("Ganhou o utilizador.")
    else:
        print("Ganhou o computador.")


def jogo_adivinha():
    num = randint(0, 5)
    num2 = int(input("Qual é o número? "))

    while num != num2:
        if num2 > num:
            print("Tente um número mais baixo.")
        elif num2 < num:
            print("Tente um número mais alto.")

        num2 = int(input("Qual é o número? "))

    print("Você acertou!")


def jogo_luta():
    vidaA = 10
    vidaB = 10

    while True:
        socoA = randint(1, 5)
        socoB = randint(1, 5)

        vidaA -= socoB
        vidaB -= socoA

        sleep(1)
        print("O lutador A deu um soco de forca", socoA, "e a vida do lutador B foi para", max(0, vidaB), ".")
        sleep(1)
        print("O lutador B deu um soco de forca", socoB, "e a vida do lutador A foi para", max(0, vidaA), ".")
        sleep(1)

        if vidaA <= 0 or vidaB <= 0:
            break

    if vidaA <= 0 and vidaB <= 0:
        print("Os lutadores empataram.")
    elif vidaA <= 0:
        print("O lutador B ganhou.")
    else:
        print("O lutador A ganhou.")


def jackpot():
    pontos = 0
    lista_perguntas = ["Qual o feminino de leao?",
                       "Qual o nome de um conjunto de lobos?",
                       "Qual o feminino de atores?",
                       "De que cor e o ceu?"]

    lista_respostas = ["Leoa", "Alcateia", "Atriz", "Azul"]

    lista_escolhas = []

    while len(lista_escolhas) < len(lista_perguntas):
        escolha = randint(0, 3)

        if escolha not in lista_escolhas:
            lista_escolhas.append(escolha)
            resposta1 = input(lista_perguntas[escolha])

            if resposta1.title() == lista_respostas[escolha]:
                pontos += 2500
                print("Está com", pontos, "pontos.")
            else:
                print("Resposta errada!")

        else:
            print("Pergunta já foi feita. Vou sortear outro número.")

    if pontos == 10000:
        print("Parabéns! Você alcançou o prêmio máximo de 10 mil euros.")
    else:
        print("Que pena! Você errou e perdeu tudo!")


def jogo_moeda():
    escolha = input("Cara ou Coroa?")

    resultado = random.choice(["cara", "coroa"])

    print(f"Você escolheu {escolha} e o resultado foi {resultado}.")

    if escolha == resultado:
        print("Parabéns! Você acertou!")
    else:
        print("Que pena! Você errou!")


def jogo_de_dados():
    dado_jogador = random.randint(1, 6)
    dado_computador = random.randint(1, 6)

    print(f"Você lançou o dado e obteve: {dado_jogador}")
    print(f"O computador lançou o dado e obteve: {dado_computador}")

    if dado_jogador > dado_computador:
        print("Parabéns! Você ganhou!")
    elif dado_jogador < dado_computador:
        print("Que pena! Você perdeu.")
    else:
        print("Empate!")


while True:
    try:
        print()
        sleep(2)
        print("MENU")
        sleep(1)
        print("1: Pedra, Papel, Tesoura")
        sleep(1)
        print("2: Jogo de Adivinha")
        sleep(1)
        print("3: Jogo de Luta")
        sleep(1)
        print("4: Jackpot")
        sleep(1)
        print("5: Jogo da Moeda")
        sleep(1)
        print("6: Jogo de Dados")
        sleep(1)
        print("0: Sair")
        sleep(1)
        
    except:
        print("Algum erro ocorreu")

    escolha = int(input(f'Que jogo deseja jogar?'))

    if escolha == 0:
        break

    elif escolha in (1, 2, 3, 4, 5, 6):
        print("O jogo vai começar...")

        if escolha == 1:
            pedra_papel_tesoura()

        elif escolha == 2:
            jogo_adivinha()

        elif escolha == 3:
            jogo_luta()

        elif escolha == 4:
            jackpot()

        elif escolha == 5:
            jogo_moeda()

        elif escolha == 6:
            jogo_de_dados()

    else:
        print("Opção inválida.")
