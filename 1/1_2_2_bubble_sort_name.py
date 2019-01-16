"""
冒泡排序——排序名称对应数字

示例：
输入：
5
huhu 5
haha 3
xixi 5
hengheng 2
gaoshou 8
输出：
gaoshou huhu xixi haha hengheng
"""
import copy


def bubble_sort_name(in_list, pos, front):
    """
    带数字位置的冒泡排序
        :param in_list: 输入列表，列表的元素应为列表
        :param pos: 子列表中要排序的数的位置（从0开始）
        :param front: 排序方向，0为从小到大排序，1为从大到小排序
    """
    out_list = copy.deepcopy(in_list)
    for i in range(len(out_list) - 1):
        for j in range(0, len(out_list) - 1 - i):
            if front == 1:
                if out_list[j][pos] < out_list[j + 1][pos]:
                    out_list[j], out_list[j + 1] = out_list[j + 1], out_list[j]
            else:
                if out_list[j][pos] > out_list[j + 1][pos]:
                    out_list[j], out_list[j + 1] = out_list[j + 1], out_list[j]
    return out_list


in_num = int(input("请输入要排序的个数: "))

original_list = []
for i in range(in_num):
    in_struct_str = input("请输入名称和整数，用空格分隔: ")
    in_struct = in_struct_str.split(' ')
    in_struct[1] = int(in_struct[1])
    original_list.append(in_struct)
sort_list = bubble_sort_name(original_list, 1, 1)
for i in sort_list:
    i[1] = str(i[1])
print(" ".join([i[0] for i in sort_list]))
