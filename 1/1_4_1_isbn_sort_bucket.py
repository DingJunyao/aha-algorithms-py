"""
将ISBN号去重，并使用桶排序从小到大排序

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

警告：在运行上面的示例时，请务必确保计算机拥有足够的内存（不知道要多少，反正8GB是不够的），以免死机。如果计算机内存不足，建议使用较小的数字进行测试。
"""


in_num = int(input("请输入书的个数: "))
orginal_list = []
for i in range(in_num):
    orginal_list.append(int(input("请输入书号: ")))
bucket = [0 for _ in range(max(orginal_list) + 1)]
for i in orginal_list:
    bucket[i] = bucket[i] + 1
for i in range(len(bucket)):
    if bucket[i] != 0:
        print(i)
