"""
模拟链表

输入数据，使用模拟链表存储，追加数据，输出输入和追加的数据。使用对象实现。
"""


class SimulatedLinkedList:
    def __init__(self):
        """
        模拟链表初始化
        """
        self.data = []
        self.right = []

    def initData(self, in_data):
        """
        在模拟链表中加入数据
            :param in_data: 数据，以列表形式添加
        """
        for i, d in enumerate(in_data):
            self.data.append(d)
            if i == len(in_data) - 1:
                self.right.append(None)
            else:
                self.right.append(i + 1)

    def iterate(self):
        """
        遍历数据，输出列表
        """
        sll = []
        for i in range(len(self.data)):
            if i == 0:
                sll.append(self.data[i])
                j = 0
            else:
                j = self.right[j]
                if j is None:
                    break
                sll.append(self.data[j])
        return sll

    def ins(self, data):
        """
        在模拟链表中插入数据。如果链表和数据内容为整数，且已经按从小到大的顺序排列，数据会按顺序放到合适位置
            :param data: 数据
        """
        lp = 0
        lp_before = 0
        self.data.append(data)
        while self.data[lp] < data:
            lp_before = lp
            if self.right[lp] is not None:
                lp = self.right[lp]
            else:
                break
        if lp == 0 and lp_before == 0:
            self.data[0], self.data[-1] = self.data[-1], self.data[0]
            self.right.append(self.right[0])
            self.right[0] = len(self.data) - 1
        else:
            self.right[lp_before] = len(self.data) - 1
            self.right.append(lp)


sll = SimulatedLinkedList()
sll.initData([int(i) for i in input("请输入从小到大已排好序的整数，以空格分隔: ").split(' ')])

sll.ins(int(input("请输入要添加的数，该数会按顺序放到合适位置: ")))
print(' '.join([str(i) for i in sll.iterate()]))
 