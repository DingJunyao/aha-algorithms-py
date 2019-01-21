"""
枚举2
□□□ + □□□ = □□□，将1~9分别填入其中使等式成立，数字不重复，求所有的解法和解法个数（加数互相调换的两个解法算作一个）
"""
total = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    for f in range(1, 10):
                        for g in range(1, 10):
                            for h in range(1, 10):
                                for i in range(1, 10):
                                    if a != b and a != c and a != d and a != e and a != f and a != g and a != h and a != i and b != c and b != d and b != e and b != f and b != g and b != h and b != i and c != d and c != e and c != f and c != g and c != h and c != i and d != e and d != f and d != g and d != h and d != i and e != f and e != g and e != h and e != i and f != g and f != h and f != i and g != h and g != i and h != i and (a + d) * 100 + (b + e) * 10 + c + f == 100 * g + 10 * h + i:
                                        print("%s%s%s + %s%s%s = %s%s%s" %
                                              (a, b, c, d, e, f, g, h, i))
                                        total = total + 1
print("共有%s种解法" % (total // 2))

"""
本部分代码相当复杂，可以使用Pytohn自动生成，如if语句可用以下方法生成：

s = "abcdefghi"
q = []
for i,j in enumerate(s):
    for k in s[i+1:]:
        q.append(j+" != "+k)
q.append("(a + d) * 100 + (b + e) * 10 + c + f == 100 * g + 10 * h + i")
print("if " + " and ".join(q) + ":")

可以省一半多的输入。
"""
