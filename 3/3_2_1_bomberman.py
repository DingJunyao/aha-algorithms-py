"""
炸弹人

在炸弹人游戏中，炸弹可以放在空地上，爆炸方向是上下左右四个方向，只要在这些范围内的敌人均可以被消灭。墙壁可以抵挡爆炸的杀伤。
先输入地图的行数，再输入地图，地图为矩形，#为墙壁，G为敌人，.为空地。判断在何处投放炸弹消灭敌人数最大。如以下示例：

输入：
13
#############
#GG.GGG#GGG.#
###.#G#G#G#G#
#.......#..G#
#G#.###.#G#G#
#GG.GGG.#.GG#
#G#.#G#.#.###
##G...G.....#
#G#.#G###.#G#
#...G#GGG.GG#
#G#.#G#G#.#G#
#GG.GGG#G.GG#
#############
输出：
将炸弹放在(9,9)处，最多可以消灭8个敌人

这里的坐标的格式是(行,列)，从0开始计数。
"""

map = []
row = int(input("输入行数: "))
print("输入地图，每输入完一行按回车键:")
for i in range(row):
    rmap = input()
    if map != []:
        if len(rmap) == len(map[0]):
            map.append(rmap)
        else:
            raise Exception
    else:
        map.append(rmap)
print("输入地图完成，正在计算...")
max = 0
p = None
q = None
for i, rmap in enumerate(map):
    for j, element in enumerate(rmap):
        if element != '.':
            continue
        sum = 0
        x = i
        y = j
        while 0 <= x <= row - 1 and map[x][y] != '#':
            if map[x][y] == 'G':
                sum = sum + 1
            x = x - 1
        x = i
        y = j
        while 0 <= x <= row - 1 and map[x][y] != '#':
            if map[x][y] == 'G':
                sum = sum + 1
            x = x + 1
        x = i
        y = j
        while 0 <= y <= len(map[0]) and map[x][y] != '#':
            if map[x][y] == 'G':
                sum = sum + 1
            y = y - 1
        x = i
        y = j
        while 0 <= y <= len(map[0]) and map[x][y] != '#':
            if map[x][y] == 'G':
                sum = sum + 1
            y = y + 1
        if sum > max:
            max = sum
            p = i
            q = j
print("将炸弹放在(%s,%s)处，最多可以消灭%s个敌人" % (p, q, max))
