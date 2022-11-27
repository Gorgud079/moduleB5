def Hi():
    print('-'*30)
    print()
    print('Вы включили игру крестики-нолики')
    print()
    print('-'*30)
    print('Вводить нужно 2 цифры')
    print('(по х и у оси соответственно),')
    print('через пробел')
    print('Х - номер строки, У - номер столбца')
    print('-'*30)

def table():
    # Игровая площадка
    print()
    print('    | 0 | 1 | 2 | ')
    print('  --+---+---+---+--')
    for i, level in enumerate(pole):
        level_y = f"  {i} | {' | '.join(level)} | {i}"
        print(level_y)
        # print(f"  {i} | {' | '.join(level)} | {i}")
        print("  --+---+---+---+--")
    print('    | 0 | 1 | 2 | ')
    print()

pole = [[' ', ' ', ' '] for i in range(3)]
# print(pole)
def step():
    while True:
        answer = input('Ваш ход: ').split()
        if len(answer) != 2:
            print("Введите 2 цифры")
            continue
        x, y = answer
        x, y = int(x), int(y)
        if 2<x or x<0 or 0>y or y>2:
            print('Введите цифры от 0 до 2 включительно')
            continue
        if pole[x][y] !=' ':
            print('Выберите другую клетку')
            continue
        return x, y
def win():
    # Победные варианты
    variant = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
               ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
               ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
               ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cod in variant:
        symbols = []
        for c in cod:
            symbols.append(pole[c[0]][c[1]])
        if symbols == ['X', 'X', 'X']:
            print('X - WIN')
            return True
        if symbols == ['O', 'O', 'O']:
            print('O - WIN')
            return True
        return False

Hi()
count = 0
while True:
    count += 1
    table()
    if count % 2 == 1:
        print('ХОД КРЕСТИКА')
    else:
        print('ХОД НОЛИКА')
    x, y = step()
    if count %2 == 1:
        pole[x][y]='X'
    else:
        pole[x][y]='O'
    if win():
        break
    if count == 9:
        print('ничья')
        break

