"""
枚举3
□□□ + □□□ = □□□，将1~9分别填入其中使等式成立，数字不重复，求所有的解法和解法个数（加数互相调换的两个解法算作一个）
使用另一种方法
"""

total = 0
a = [0 for _ in range(9)]
for a[0] in range(1, 10):
    for a[1] in range(1, 10):
        for a[2] in range(1, 10):
            for a[3] in range(1, 10):
                for a[4] in range(1, 10):
                    for a[5] in range(1, 10):
                        for a[6] in range(1, 10):
                            for a[7] in range(1, 10):
                                for a[8] in range(1, 10):
                                    book = [0 for _ in range(9)]
                                    for ai in a:
                                        book[ai - 1] = 1
                                    if sum(book) == 9 and (a[0] + a[3]) * 100 + (a[1] + a[4]) * 10 + a[2] + a[5] == 100 * a[6] + 10 * a[7] + a[8]:
                                        total = total + 1
                                        print("%s%s%s + %s%s%s = %s%s%s" % tuple(a))
print("共有%s种解法" % (total // 2))
