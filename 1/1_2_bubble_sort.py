"""
冒泡排序

示例：
输入：5 3 5 2 8
输出：8 5 5 3 2
"""


def bubble_sort(in_list, front):
    out_list = list(in_list)
    for i in range(len(out_list) - 1):
        for j in range(0, len(out_list) - 1 - i):
            if front == 1:
                if out_list[j] < out_list[j + 1]:
                    out_list[j], out_list[j +
                                          1] = out_list[j + 1], out_list[j]
            else:
                if out_list[j] > out_list[j + 1]:
                    out_list[j], out_list[j +
                                          1] = out_list[j + 1], out_list[j]
    return out_list


in_str = input("请输入要排序的整数，用空格分隔: ")
print(' '.join(
    [str(sort_int) for sort_int in bubble_sort(
        [int(o_in_str) for o_in_str in in_str.split(' ')], 1)
     ]))
