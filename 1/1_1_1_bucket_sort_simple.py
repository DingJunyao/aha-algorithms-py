"""
桶排序（简化）

示例：
输入：5 3 5 2 8
输出：8 5 5 3 2

"""


def bucket_sort_simple(in_list, front):
    """
    桶排序（简单）
        :param in_list: 待排序数组成的列表
        :param front: 排序方向，0为从小到大排序，1为从大到小排序
    """
    num_max = max(in_list)
    sort_num = [0 for _ in range(num_max + 1)]
    for i in in_list:
        sort_num[i] += 1
    out_list = []
    for a in range(num_max + 1):
        if front == 1:
            a = num_max - a
        j = sort_num[a]
        while j > 0:
            out_list.append(a)
            j -= 1
    return out_list


in_str = input("请输入要排序的正整数，用空格分隔: ")
print(' '.join(
    [str(sort_int) for sort_int in bucket_sort_simple(
        [int(o_in_str) for o_in_str in in_str.split(' ')], 1)
     ]))
