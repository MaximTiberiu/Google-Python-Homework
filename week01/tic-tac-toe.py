# Joc - X si 0 (2 players)
import time
from random import randint


# functie care afiseaza tabla curenta de joc
def print_board(tictactoe_board):
    print('\t-+-+-')
    for i in range(1, 10):
        if i in (1, 4, 7):
            print('\t', end='')
        if i % 3 != 0:
            print(tictactoe_board[i] + '|', end='')
        else:
            print(tictactoe_board[i])
            print('\t-+-+-')


# fucntie care face verificarile necesare pentru stabilirea unui castigator
def verify_winner(tictactoe_board):
    # verificare pe randuri
    for i in range(1, 10, 3):
        if tictactoe_board[i] == tictactoe_board[i + 1] == tictactoe_board[i + 2] != ' ':
            return True

    # verificare pe coloane
    for i in range(1, 4):
        if tictactoe_board[i] == tictactoe_board[i + 3] == tictactoe_board[i + 6] != ' ':
            return True

    # verificare pe diagonale
    if tictactoe_board[1] == tictactoe_board[5] == tictactoe_board[9] != ' ':
        return True
    elif tictactoe_board[3] == tictactoe_board[5] == tictactoe_board[7] != ' ':
        return True
    else:
        return False  # inca nu exista un castigtor


# functie care schimba jucatorul
def change_turn(turn):
    if turn == 'X':
        return '0'
    return 'X'


# fucntie care afiseaza tabla initiala
def print_init_board(tictactoe_board):
    print('\n*******************************************')
    print("Tabla initiala...")
    print_board(tictactoe_board)
    print('*******************************************')


# functie care afiseaza pozitiile de joc
def print_positions():
    print('*******************************************')
    print('''Acestea sunt pozitiile pe tabla de joc...
        \t-+-+-
        \t1|2|3
        \t-+-+-
        \t4|5|6
        \t-+-+-
        \t7|8|9
        \t-+-+-''')
    print('*******************************************')


# functie care afiseaza castigatorul
def print_winner(tictactoe_board, turn, player1, player2):
    print('\n\n*******************************************')
    print_board(tictactoe_board)
    print('*******************************************')
    print(f"Avem un castigator: {turn}!!! -- {player1 if turn == 'X' else player2}")
    print('*******************************************')


# functie care afiseaza cazul de egalitate
def print_tie(tictactoe_board):
    print('\n\n********************************************')
    print_board(tictactoe_board)
    print('*******************************************')
    print('Avem egalitate!!!')
    print('*******************************************')


# functia care porneste un joc de X si 0
def start_game():
    player1 = input("X - Numele tau este: ")
    player2 = input("0 - Numele tau este: ")

    # am folosit un dictionar in care cheia reprezinta pozitia elemetelor pe tabla de joc
    # initial, fiecare valoare este un space, pentru a simula faptul ca tabla de joc este goala
    # in momentul in care un player doreste sa completeze o casuta la o anumnita pozitie, se va actualiza tictactoeBoard
    tictactoe_board = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' ',
    }

    # afisarea tablei de joc goala
    print_init_board(tictactoe_board)
    time.sleep(3)

    # stabilirea playerului care va incepe jocul
    turn = 'X'  # in variabila turn stochez playerul care urmeaza sa actioneze pe tabla de joc
    first_turn = randint(0, 1)
    if first_turn == 1:
        # daca la generarea random, se returneaza 1, atunci playerul '0' va incepe jocul, altfel va ramane 'X'
        turn = '0'
        print(f'Playerul ** 0 ** ({player2}) incepe jocul!')
    else:
        print(f'Playerul ** X ** ({player1}) incepe jocul!')
    time.sleep(3)

    # afisarea pozitiilor pe tabla, pentru ca playerii sa stie unde sa faca actiunile
    print_positions()
    time.sleep(3)

    no_of_turns = 0  # numarul de mutari facute
    winner = False  # stabileste daca exista un castigator sau nu
    # incepe jocul efectiv
    while no_of_turns < 9:
        # afisam tabla de joc curenta si playerul care trebuie sa isi plaseze semnul
        print_board(tictactoe_board)
        print(f"Este randul playerului: {turn} / {player1 if turn == 'X' else player2}")

        location = int(input("Care este pozitie unde doresti sa asezi piesa? [1-9]: "))

        # verificam daca pozitia data ca argument este corecta
        if location not in range(1, 10):
            print('********************************************')
            print('*Introdu doar valori cuprinse intre 1 si 9!*')
            print('********************************************')
            time.sleep(3)
            continue  # ne intoarcem la inceputul instructiunii while (sarim peste verificari)

        # verificam daca pozitia este ocupata sau nu
        if tictactoe_board[location] == ' ':  # pozitia este libera, asezam aici mutarea playerului
            tictactoe_board[location] = turn
            no_of_turns += 1
        else:  # pozitia este ocupata, playerul trebuie sa aleaga o noua pozitie
            print('************************************')
            print("*Pozitia curenta este deja ocupata!*")
            print('************************************')
            time.sleep(3)
            continue  # ne intoarcem la inceputul instructiunii while (sarim peste verificari)

        # dupa 5 ture, exista posibilitatea sa avem un castigator, facem verificarile aferente
        if no_of_turns >= 5 and verify_winner(tictactoe_board):
            print_winner(tictactoe_board, turn, player1, player2)
            winner = True
            break

        # schimbam playerul
        turn = change_turn(turn)

    # daca se iese din while fara un castigator, rezulta egalitate
    if not winner:
        print_tie(tictactoe_board)

    time.sleep(3)
    # restart la joc, in caz ca se doreste
    if input('Doriti sa mai jucati? (0/1): ') == '1':
        start_game()
    else:
        print("Bye!")
        time.sleep(3)


start_game()
