from Common.computer import Computer
from functools import reduce

TILES = {
    0: ' ',
    1: '#',
    2: 'x',
    3: '_',
    4: 'o'
}


def split_list(list, n):
    for i in range(0, len(list), n):
        yield list[i:i + n]


def show_screen(tiles):
    max_x = 0
    max_y = 0
    for tile in tiles.items():
        if tile[0][0] > max_x:
            max_x = tile[0][0]
        if tile[0][1] > max_y:
            max_y = tile[0][1]
    screen_list = []
    for i in range(0, max_y + 1):
        row = []
        for j in range(0, max_x + 1):
            tile = tiles.get((j, i), ' ')
            row.append(tile)
        screen_list.append(row)

    for i, row in enumerate(screen_list):
        screen_list[i] = ''.join(row)
    return '\n'.join(screen_list)


input_path = './input.txt'


computer = Computer(input_path)
output = computer.calculate()[1]
instructions = split_list(output, 3)
tiles = dict()
for instr in instructions:
    tiles[(instr[0], instr[1])] = TILES[instr[2]]

part_one = len(list(filter(lambda tile: tile[1] == 'x', tiles.items())))
print('answer for part1 is: ', part_one)
# 284
print(show_screen(tiles))

computer.i = 0
computer.set(0, 2)
# computer.input()
score = 0
ball_x,paddle_x=0,0
while True:
    output = computer.calculate(arcade=True)
    if output is None:
        break
    if output == 'input':
        print(show_screen(tiles))
        move = 1 if ball_x > paddle_x else 0 if ball_x == paddle_x else -1
        computer.input(move)
        continue
    if output[0] == -1 and output[1] == 0:
        score = output[2]
    else:
        tiles[(output[0], output[1])] = TILES[output[2]]
        if TILES[output[2]] == 'o':
            ball_x, ball_y = output[:2]
        elif TILES[output[2]] == '_':
            paddle_x = output[0]
print('game is finished with SCORE:', score)
