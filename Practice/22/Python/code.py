maze = [
    "####B######################",
    "# #           #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   # #   #   #",
    "# ############# # # # # # #",
    "# ###       # # # # # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]
posesh = []
def put(x, y, k = 0):
    if (x, y) in posesh:
        return
    posesh.append((x,y))
    if x >= len(maze[0]) or y >= len(maze) or x < 0 or y < 0:
        return
    if maze[x][y-1] == ' ':
        put(x, y - 1)
    if maze[x-1][y] == ' ':
        put(x - 1, y)
    if maze[x+1][y] == ' ':
        put(x + 1, y)
    if maze[x][y+1] == ' ':
        put(x, y + 1)
    if maze[x][y - 1] != ' ' and maze[x][y - 1] != '#':
        print(maze[x][y-1], end = ' ')
        schetchick()
        return put(x, y-1)
    if maze[x - 1][y] != ' ' and maze[x - 1][y] != '#':
        print(maze[x-1][y], end = ' ')
        schetchick()
        return
    if maze[x + 1][y] != ' ' and maze[x + 1][y] != '#':
        print(maze[x+1][y], end = ' ')
        schetchick()
        return
    if maze[x][y + 1] != ' ' and maze[x][y + 1] != '#':
        print(maze[x][y+1], end = ' ')
        schetchick()
        return
def schetchick(k=0):
    k += 1
    return k
k = schetchick()
if k == 0:
    print('Error')
x, y = map(int, input().split())
if maze[x][y] == '#':
    print('Error')
    exit(0)
put(x, y)