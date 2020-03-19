import random


def xod_comp():
    k = random.randint(0,8)
    if (ms[k] != 'x') and (ms[k] != 'o'):
        ms[k] = 'o'
        print("комп ходит по координате : " + str(k+1))
    else:
        xod_comp()


def gener_mat():
    print( ms[0] + " | " + ms[1] + " | " + ms[2] )
    print( "__|" + "___|" + "__")
    print( ms[3] + " | " + ms[4] + " | " + ms[5] )
    print( "__|" + "___|" + "__")
    print( ms[6] + " | " + ms[7] + " | " + ms[8] )
    print( "  |" + "   |")
    print("\n")


def xod_player():
    i = int(input("введи клетку (от 1 до 9): "))
    if (ms[i-1] != 'x') and (ms[i-1] != 'o'):
        print("\n")
        ms[i-1] = 'x'
    else:
        print("\n")
        print("эта клетка уже занята!")
        xod_player()


def proverka_na_vyigrish():

    #ms = [ 'x', 'x', 'x' ,'o' ,'o' ,'o', 'x' , 'x' , 'x']
    if (ms[0] == 'x') and (ms[1] == 'x') and (ms[2] == 'x'):
        print("выиграл пользователь")
        print("Игра окончена ")
        exit()
    elif (ms[0] == 'x') and (ms[3] == 'x') and(ms[6]== 'x'):
        print("выиграл пользователь")
        print("Игра окончена ")
        exit()
    elif (ms[1] == 'x') and (ms[4] == 'x') and(ms[7]== 'x'):
        print("выиграл пользователь")
        print("Игра окончена ")
        exit()
    elif (ms[2] == 'x') and (ms[5] == 'x') and(ms[8]== 'x'):
        print("выиграл пользователь")
        print("Игра окончена ")
        exit()
    elif (ms[3] == 'x') and (ms[4] == 'x') and (ms[5] == 'x'):
        print("выиграл пользователь")
        print("Игра окончена ")
        exit()
    elif (ms[6] == 'x') and (ms[7] == 'x') and (ms[8] == 'x'):
        print("выиграл пользователь")
        print("Игра окончена ")
        exit()
    elif (ms[0] == 'x') and (ms[4] == 'x') and (ms[8] == 'x'):
        print("выиграл пользователь")
        print("Игра окончена ")
        exit()
    elif (ms[2] == 'x') and (ms[4] == 'x') and (ms[6] == 'x'):
        print("выиграл пользователь")
        print("Игра окончена ")
        exit()


    elif (ms[0] == 'o') and (ms[1] == 'o') and (ms[2] == 'o'):
        print("выиграл комп")
        print("Игра окончена ")
        exit()

    elif (ms[0] == 'o') and (ms[3] == 'o') and(ms[6]== 'o'):
        print("выиграл комп")
        print("Игра окончена ")
        exit()

    elif (ms[1] == 'o') and (ms[4] == 'o') and(ms[7]== 'o'):
        print("выиграл комп")
        print("Игра окончена ")
        exit()

    elif (ms[2] == 'o') and (ms[5] == 'o') and(ms[8]== 'o'):
        print("выиграл комп")
        print("Игра окончена ")
        exit()

    elif (ms[3] == 'o') and (ms[4] == 'o') and (ms[5] == 'o'):
        print("выиграл комп")
        print("Игра окончена ")
        exit()

    elif (ms[6] == 'o') and (ms[7] == 'o') and (ms[8] == 'o'):
        print("выиграл комп")
        print("Игра окончена ")
        exit()

    elif (ms[0] == 'o') and (ms[4] == 'o') and (ms[8] == 'o'):
        print("выиграл комп")
        print("Игра окончена ")
        exit()

    elif (ms[2] == 'o') and (ms[4] == 'o') and (ms[6] == 'o'):
        print("выиграл комп")
        print("Игра окончена ")
        exit()


ms = [ ' ', ' ', ' ' ,' ' ,' ' ,' ', ' ' , ' ' , ' ']

def main():
    while True:
        xod_player()
        gener_mat()
        proverka_na_vyigrish()
        xod_comp()
        gener_mat()
        proverka_na_vyigrish()


if __name__ == "__main__":
    main()

