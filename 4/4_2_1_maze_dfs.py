"""
迷宫——深度优先搜索

输入一个迷宫的地图，其中0表示空地，1表示障碍。最后输入起点和终点的坐标，求最短步数。
使用深度优先搜索。坐标的格式是(行,列)，从1开始。

示例：
输入：
5
0010
0000
0010
0100
0001
1 1
4 3
输出：
7
"""


maze_map = []
row = int(input("请输入地图的行数: "))
print("接下来输入每一行的地图: ")
for i in range(row):
    rmap = input()
    if maze_map != []:
        if len(rmap) == len(maze_map[0]):
            maze_map.append(rmap)
        else:
            raise Exception
    else:
        maze_map.append(rmap)
sp = [int(i) - 1 for i in input("请输入起点坐标（从1开始，以空格分隔）: ").split(' ')]
ep = [int(i) - 1 for i in input("请输入终点坐标（从1开始，以空格分隔）: ").split(' ')]
min_step = None
book = [[0 for _ in range(len(maze_map[0]))] for _ in range(row)]


def dfs(x, y, step):
    global row, min_step
    next_step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    if x == ep[0] and y == ep[1]:
        if min_step == None or step < min_step:
            min_step = step
    else:
        for k in range(4):
            tx = x + next_step[k][0]
            ty = y + next_step[k][1]
            if 0 <= tx < row and 0 <= ty < len(maze_map[0]) and maze_map[tx][ty] == "0" and book[tx][ty] == 0:
                book[tx][ty] = 1
                dfs(tx, ty, step + 1)
                book[tx][ty] = 0


book[sp[0]][sp[1]] = 1
dfs(sp[0], sp[1], 0)
print(min_step)
