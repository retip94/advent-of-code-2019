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


# def show_map(path):
#     grid = []
#     min_x = min(list(map(lambda x: x[0], path.keys())))
#     max_x = max(list(map(lambda x: x[0], path.keys())))
#     min_y = min(list(map(lambda x: x[1], path.keys())))
#     max_y = max(list(map(lambda x: x[1], path.keys())))
#     width = abs(min_x) + max_x + 1 if min_x < 0 else max_x - min_x
#     height = abs(min_y) + max_y + 1 if min_y < 0 else max_y - min_y
#     for i in range(0, height):
#         row = []
#         for j in range(0, width):
#             pos = j, i
#             color = COLORS[get_color_under(pos, path)]
#             row.append(color)
#         print(row)
#         grid.append(row)

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

path = {}
path[(0,0)]='#'
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
