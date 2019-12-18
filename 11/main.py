import Common.computer as comp

DIRS = {
    'UP': {'x': 0, 'y': -1},
    'RIGHT': {'x': 1, 'y': 0},
    'DOWN': {'x': 0, 'y': 1},
    'LEFT': {'x': -1, 'y': 0}
}

TURN = {
    'UP': {0: 'LEFT', 1: 'RIGHT'},
    'RIGHT': {0: 'UP', 1: 'DOWN'},
    'DOWN': {0: 'RIGHT', 1: 'LEFT'},
    'LEFT': {0: 'DOWN', 1: 'UP'}
}

COLORS = {0: '.', '.': 0, 1: '#', '#': 1}

pos = 0, 0
dir = 'UP'


def move(pos, dir):
    x = pos[0] + DIRS[dir]['x']
    y = pos[1] + DIRS[dir]['y']
    return x, y


def get_color_under(pos, path):
    try:
        return COLORS[path[pos]]
    except KeyError:
        return COLORS['.']


def show_map(path):
    tmp = [[" "] * 500 for _ in range(20)]
    for i in zip(path.keys(), path.values()):
        try:
            tmp[i[0][1]][i[0][0]] = i[1]
        except:
            tmp[i[0][1]][i[0][0]] = '.'
    [print(" ".join(x)) for x in tmp]


path = {}

input_path = '.\input.txt'
# computer = comp.Computer(input_path)
# while True:
#     computer.input(get_color_under(pos, path))
#     output = computer.calculate(painting=True, debug=False)
#     if output is None:
#         break
#     color, turn = output
#     path[pos] = COLORS[color]
#     dir = TURN[dir][turn]
#     pos = move(pos, dir)
# print(len(path))
# 2392

path[(0, 0)] = '#'
computer = comp.Computer(input_path)
while True:
    computer.input(get_color_under(pos, path))
    output = computer.calculate(painting=True, debug=False)
    if output is None:
        break
    color, turn = output
    path[pos] = COLORS[color]
    dir = TURN[dir][turn]
    pos = move(pos, dir)
print(len(path))
show_map(path)
# EGBHLEUE
