field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

print("Добро пожаловать! Вы запустили игру в крестики-нолики, где вам предстоит заполнить символами х и 0 поле 3-столбца-на-3-строки. Вот оно:")

def print_field(field):
    strings = []
    for row in field:
        strings.append('  : '.join(row))
    print('\n............\n'.join(strings))

print_field(field)

print("Первый ход делает х, затем ходы чередуются до тех пор, пока в одной линии не появятся три одинаковых символа.")
print("Ничейный исход также возможен.")

def get_move(field):
    while True:
        x = int(input('Введите строку: '))
        y = int(input('Введите столбец: '))
        if x in range(1,4) and y in range(1,4):
            x, y = int(x) - 1, int(y) - 1
            if field[x][y] != ' ':
                print("Клетка занята")
                continue
        else:
            print('Вы ошиблись! Введите число от 1 до 3.')
            continue
        return x, y

def check_winner(field):
    #строки
    if field[0][0] == field[0][1] == field[0][2] != ' ':
        return True
    if field[1][0] == field[1][1] == field[1][2] != ' ':
        return True
    if field[2][0] == field[2][1] == field[2][2] != ' ':
        return True
    #столбцы
    if field[0][0] == field[1][0] == field[2][0] != ' ':
        return True
    if field[0][1] == field[1][1] == field[2][1] != ' ':
        return True
    if field[0][2] == field[1][2] == field[2][2] != ' ':
        return True
    # диагонали
    if field[0][0] == field[1][1] == field[2][2] != ' ':
        return True
    if field[0][2] == field[1][1] == field[2][0] != ' ':
        return True
    else:
        return False

def play():
    field = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    player_1 = 'x'
    player_2 = '0'
    counter = 0

    while True:
        print_field(field)

        x, y = get_move(field)
        if counter % 2 == 0:
            field[x][y] = player_1
        else:
            field[x][y] = player_2

        if check_winner(field):
            if counter % 2 == 0:
                print('Победил игрок Х')
            else:
                print('Победил игрок 0')
            print_field(field)
            break

        if counter == 8:
            print('Ничья')
            break

        counter += 1

play()




