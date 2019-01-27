"""
深度优先搜索2

□□□ + □□□ = □□□，将1~9分别填入其中使等式成立，数字不重复，求所有的解法和解法个数（加数互相调换的两个解法算作一个）
"""

total = 0
a = [None for _ in range(10)]
book = [0 for _ in range(10)]


def dfs(step):
    global total
    if step == 10:
        if 100 * (a[1] + a[4]) + 10 * (a[2] + a[5]) + a[3] + a[6] == 100 * a[7] + 10 * a[8] + a[9]:
            print("%s%s%s + %s%s%s = %s%s%s" % tuple(a[1:]))
            total += 1
    else:
        for i in range(1, 10):
            if book[i] == 0:
                a[step] = i
                book[i] = 1
                dfs(step + 1)
                book[i] = 0


dfs(1)
print("共有%s种解法" % (total // 2))
