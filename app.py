# importar o random 
import random

# criar array com as opções "pedra", "papel" e "tesoura"
opcoes = ["pedra", "papel", "tesoura"]
pontos = 0
partidas = 0

while True:
    random_choice = random.choice(opcoes)
    player_choice = input("Escolha pedra, papel ou tesoura: ")
    print("O computador escolheu: \n...\n" + random_choice.capitalize())
    print("Resultado: ")
    if player_choice == "pedra":
        partidas += 1

        if random_choice == "pedra":
            print("Empate")
        elif random_choice == "papel":
            print("Você perdeu")
            pontos -= 1
        else:
            print("Você ganhou")

    elif player_choice == "papel":
        if random_choice == "pedra":
            print("Você ganhou")
            pontos += 1
        elif random_choice == "papel":
            print("Empate")
        else:
            print("Você perdeu")

    elif player_choice == "tesoura":
        if random_choice == "pedra":
            print("Você perdeu")
            pontos -= 1
        elif random_choice == "papel":
            print("Você ganhou")
            pontos += 1
        else:
            print("Empate")
    else:
        print("Opção inválida")

    print("Pontuação: " + str(pontos), "Partidas: " + str(partidas))

    play_again = input("Deseja jogar novamente? (s/n): ")
    
    if play_again == "s":
        continue
    if play_again == "n":
        break
