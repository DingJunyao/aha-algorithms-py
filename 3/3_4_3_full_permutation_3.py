"""
全排列3

输入n（n为1~9内的整数），输出1~n范围内的全排列结果
"""


def addl(in_list, num):
    out_list = []
    for i in in_list:
        for j in range(len(i) + 1):
            k = list(i)
            k.insert(j, str(num))
            out_list.append(k)
    return out_list


def fp(n):
    out_list = [['1']]
    if n != 1:
        for i in range(2, n + 1):
            out_list = addl(out_list, i)
    out_list = [int("".join(i)) for i in out_list]
    out_list.sort()
    return out_list


n = int(input("输入n: "))
o = fp(n)
for i in o:
    print(i)
