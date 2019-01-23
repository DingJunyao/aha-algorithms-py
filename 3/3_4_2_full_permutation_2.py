"""
全排列2

求1、2、3、4的全排列
"""

k = [1, 2, 3, 4]
for a in k:
    for b in k:
        for c in k:
            for d in k:
                if a != b and a != c and a != d and b != c and b != d and c != d:
                    print("%s%s%s%s" % (a, b, c, d))
