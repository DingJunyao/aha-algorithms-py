"""
将ISBN号去重，并使用冒泡排序从小到大排序

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
in_num = int(input("请输入书的个数: "))
sort_list = []
for i in range(in_num):
    sort_list.append(int(input("请输入书号: ")))
for i in range(len(sort_list) - 1):
    for j in range(len(sort_list) - 1 - i):
        if sort_list[j] > sort_list[j + 1]:
            sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
for k in range(len(sort_list)):
    if sort_list[k] != sort_list[k - 1]:
        print(sort_list[k])
