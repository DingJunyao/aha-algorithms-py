"""
将ISBN号去重，并使用快速排序从小到大排序

输入：
10
9781234567890
9781241242123
9782141241223
9784689622528
9786904328539
9783462839468
9783849534054
9783426989053
9784032698743
9783462839468

输出：
9781234567890
9781241242123
9782141241223
9783426989053
9783462839468
9783849534054
9784032698743
9784689622528
9786904328539

"""


def quick_sort(left, right):
    if left > right:
        return
    base = left
    i = left
    j = right
    while j != i:
        while (sort_list[j] >= sort_list[base]) and (i < j):
            j = j - 1
        while (sort_list[i] <= sort_list[base]) and (i < j):
            i = i + 1
        if i < j:
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[base], sort_list[j] = sort_list[j], sort_list[base]
    quick_sort(left, j - 1)
    quick_sort(j + 1, right)


in_num = int(input("请输入书的个数: "))
sort_list = []
for i in range(in_num):
    sort_list.append(int(input("请输入书号: ")))
quick_sort(0, len(sort_list) - 1)
for k in range(len(sort_list)):
    if sort_list[k] != sort_list[k - 1]:
        print(sort_list[k])
