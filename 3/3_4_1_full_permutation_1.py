"""
全排列1

求1、2、3的全排列
"""

k = [1, 2, 3]
for a in k:
    for b in k:
        for c in k:
            if a != b and a != c and b != c:
                print("%s%s%s" % (a, b, c))
