# Joc - X si 0 (2 players)
import time
from random import randint


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


def start_game():
    # am folosit un dictionar in care cheai reprezinta pozitia elemetelor pe tabla de joc
    # initial, fiecare valoare este un space, pentru a simula faptul ca tabla de joc este goala
    # in momentul in care un player doreste sa completeze o casuta la o anumnita pozitie, se va actualiza tictactoeBoard
    tictactoe_board = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' ',
    }

    # afisarea tablei de joc goala
    print('\n*******************************************')
    print("Tabla initiala...")
    print_board(tictactoe_board)
    print('*******************************************')
    time.sleep(2)

    # stabilirea playerului care va incepe jocul
    turn = 'X'  # in variabila turn stochez playerul care urmeaza sa actioneze pe tabla de joc
    first_turn = randint(0, 1)
    if first_turn == 1:
        # daca la generarea random, se returneaza 1, atunci playerul '0' va incepe jocul, altfel va ramane 'X'
        turn = '0'
        print('Playerul ** 0 ** incepe jocul!')
    else:
        print('Playerul ** X ** incepe jocul!')
    time.sleep(2)

    # afisarea pozitiilor pe tabla, pentru ca playerii sa stie unde sa faca actiunile
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
    time.sleep(2)

    no_of_turns = 0  # numarul de mutari facute
    winner = False  # stabileste daca exista un castigator sau nu
    # incepe jocul efectiv
    while no_of_turns < 9:
        # afisam tabla de joc curenta si playerul care trebuie sa isi plaseze semnul
        print_board(tictactoe_board)
        print("Este randul playerului: " + turn)

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
            print('\n\n*******************************************')
            print_board(tictactoe_board)
            print('*******************************************')
            print('Avem un castigator: ' + turn + '!!!')
            print('*******************************************')
            winner = True
            break

        # schimbam playerul
        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'

    # daca se iese din while fara un castigator, rezulta egalitate
    if not winner:
        print('\n\n********************************************')
        print_board(tictactoe_board)
        print('*******************************************')
        print('Avem egalitate!!!')
        print('*******************************************')


start_game()
