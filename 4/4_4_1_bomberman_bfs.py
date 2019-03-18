"""
注：本算法未完成！

炸弹人

在炸弹人游戏中，炸弹可以放在空地上，爆炸方向是上下左右四个方向，只要在这些范围内的敌人均可以被消灭。墙壁可以抵挡爆炸的杀伤。
玩家在某个位置，使用广度优先搜索判断走到何处投放炸弹消灭敌人数最大。
先输入地图的行数，再输入地图，地图为矩形，#为墙壁，G为敌人，.为空地，最后输入玩家位置，输出结果。如以下示例：

输入：
13
#############
#GG.GGG#GGG.#
###.#G#G#G#G#
#.......#..G#
#G#.###.#G#G#
#GG.GGG.#.GG#
#G#.#G#.#.#.#
##G...G.....#
#G#.#G###.#G#
#...G#GGG.GG#
#G#.#G#G#.#G#
#GG.GGG#G.GG#
#############
3 3
输出：
将炸弹放在(7,11)处，最多可以消灭10个敌人

这里的坐标的格式是(行,列)，从0开始计数。
"""

game_map = []
row = int(input("输入行数: "))
print("输入地图，每输入完一行按回车键:")
for i in range(row):
    rmap = input()
    if game_map != []:
        if len(rmap) == len(game_map[0]):
            game_map.append(rmap)
        else:
            raise Exception
    else:
        game_map.append(rmap)
print("输入地图完成，正在计算...")
# code here
# print("将炸弹放在(%s,%s)处，最多可以消灭%s个敌人" % (p, q, max))
