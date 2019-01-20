"""
链表

输入数据，使用链表存储，追加数据，输出输入和追加的数据。

Python中没有指针，因此链表的结构也不一样。本代码使用对象实现链表及其节点。
"""


class Node:
    def __init__(self, data=None, next_node=0):
        """
        节点初始化
            :param data=None: 数据，默认为None
            :param next_node=0: 下一个节点，默认为0
        """
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        """
        链表初始化
        """
        self.head = None

    def initData(self, in_data):
        """
        在链表中加入数据
            :param in_data: 数据，以列表形式添加
        """
        self.head = Node(in_data[0])
        p = self.head
        for i in in_data[1:]:
            an = Node(i)
            p.next = an
            p = p.next

    def iterate(self):
        """
        遍历数据，输出列表
        """
        ll = []
        lp = self.head
        while lp != 0:
            ll.append(lp.data)
            lp = lp.next
        return ll

    def ins(self, data):
        """
        在链表中插入数据。如果链表和数据内容为整数，且已经按从小到大的顺序排列，数据会按顺序放到合适位置
            :param data: 数据
        """
        lp = self.head
        while lp.next != 0 and lp.next.data < data:
            lp = lp.next
        an = Node(data)
        if lp is self.head and lp.next.data > data:
            an.next = lp
            self.head = an
        else:
            an.next = lp.next
            lp.next = an


ll = LinkedList()
ll.initData([int(i) for i in input("请输入从小到大已排好序的整数，以空格分隔: ").split(' ')])
ll.ins(int(input("请输入要添加的数，该数会按顺序放到合适位置: ")))
print(' '.join([str(i) for i in ll.iterate()]))
