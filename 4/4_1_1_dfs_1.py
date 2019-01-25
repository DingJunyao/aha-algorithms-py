"""
深度优先搜索1

输入n（n为1~9内的整数），输出1~n范围内的全排列结果
"""

n = int(input("请输入n: "))
a = [None for _ in range(n + 1)]
book = [0 for _ in range(n + 1)]

def dfs(step):
    # 判断边界
    if step == n + 1:
        print(''.join([str(ai) for ai in a[1:]]))
        return
    # 尝试每一种可能
    for i in range(1, n + 1):
        if book[i] == 0:
            a[step] = i
            book[i] = 1
            # 继续下一步
            dfs(step + 1)
            book[i] = 0

dfs(1)
