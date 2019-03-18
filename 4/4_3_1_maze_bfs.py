"""
迷宫——广度优先搜索

输入一个迷宫的地图，其中0表示空地，1表示障碍。最后输入起点和终点的坐标，求最短步数。
使用广度优先搜索。坐标的格式是(行,列)，从1开始。

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

class note:
    def __init__(self, x=None, y=None, s=None):
        self.x = x
        self.y = y
        self.s = s

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
que = [note() for _ in range(len(maze_map[0]) * row)]
next_step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
flag = 0
head = 0
tail = 0
que[tail].x = sp[0]
que[tail].y = sp[1]
que[tail].s = 0
book[sp[0]][sp[1]] = 1
tail += 1
while flag == 0 and head < tail:
    for k in range(4):
        tx = que[head].x + next_step[k][0]
        ty = que[head].y + next_step[k][1]
        if 0 <= tx < row and 0 <= ty < len(maze_map[0]) and maze_map[tx][ty] == '0' and book[tx][ty] == 0:
            que[tail].x = tx
            que[tail].y = ty
            que[tail].s = que[head].s + 1
            book[tx][ty] = 1
            if tx == ep[0] and ty == ep[1]:
                flag = 1
                break
            tail += 1
    head += 1

print(que[tail].s)
