"""
火柴棍等式

使用m（m≤24）根火柴棍拼出形如A+B=C的等式。要求如下：
- 如果A≠B，则A+B=C和B+A=C视为不同的等式（ABC均大于0）
- 所有的火柴棍都要用上
- 如果数字不是0，则最高位不能为0
- 加号和等号个需要两根火柴棍，计入m中
可以拼出多少种这样的等式呢？
"""
import math


def matches(in_num):
    """
    计算某个正整数所需火柴棍数量
        :param in_num: 正整数
    """
    x = in_num
    f = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    num = 0
    while x // 10 != 0:
        num = num + f[x % 10]
        x = x // 10
    num = num + f[x]
    return num


m = int(input("请输入火柴棍的数量（不大于24）: "))
total = 0
maxrg = math.ceil((m - 4) / 6)
max = 1
for maxa in range(maxrg, 0, -1):
    max = max + 10 ** (maxa - 1)
for a in range(0, max):
    if m < 11:
        break
    for b in range(0, max):
        c = a + b
        if 4 + matches(a) + matches(b) + matches(c) == m:
            print("%s + %s = %s" % (a, b, c))
            total = total + 1
print("共有%s种不同形式" % total)
