"""
快速排序

示例：
输入：6 1 2 7 9 3 4 5 10 8
输出：1 2 3 4 5 6 7 8 9 10
"""


def quick_sort(in_list, front):
    """
    快速排序
        :param in_list: 待排序数组成的列表
        :param front: 排序方向，0为从小到大排序，1为从大到小排序
    """
    def quick_sort_bt(left, right):
        if left > right:
            return
        base = left
        i = left
        j = right
        while j != i:
            if front == 1:
                while (out_list[j] <= out_list[base]) and (i < j):
                    j = j - 1
                while (out_list[i] >= out_list[base]) and (i < j):
                    i = i + 1
            else:
                while (out_list[j] >= out_list[base]) and (i < j):
                    j = j - 1
                while (out_list[i] <= out_list[base]) and (i < j):
                    i = i + 1
            if i < j:
                out_list[i], out_list[j] = out_list[j], out_list[i]
        out_list[base], out_list[j] = out_list[j], out_list[base]
        quick_sort_bt(left, j - 1)
        quick_sort_bt(j + 1, right)

    out_list = list(in_list)
    quick_sort_bt(0, len(out_list) - 1)
    return out_list


in_str = input("请输入要排序的整数，用空格分隔: ")
print(' '.join(
    [str(sort_int) for sort_int in quick_sort(
        [int(o_in_str) for o_in_str in in_str.split(' ')], 0)
     ]))
