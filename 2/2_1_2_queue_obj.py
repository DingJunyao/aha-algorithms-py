"""
队列——对象

相对于C语言的结构体类型，在Python中，本例以对象实现。Python中可以使用内置库queue来实现队列类型，本例未使用。
本例仅供学习参考，不要用于正式环境。实际使用需要考虑更多的因素。
"""


class Queue:

    def __init__(self, num=100):
        """
        队列的初始化
            :param num=100: 可选，初始化的队列的可容纳元素数目，默认为100
        """
        self.data = [0 for _ in range(num)]
        self.head = 0
        self.tail = 0

    def quin(self, in_data):
        """
        入队，将数据加入队列末尾，返回数据
            :param in_data: 入队的数据
        """
        self.tail = self.tail + 1
        self.data[self.tail - 1] = in_data
        return in_data

    def quout(self):
        """
        出队，将队列开头的数据删除，返回对应的数据
        """
        self.head = self.head + 1
        return self.data[self.head - 1]


qu = Queue()
for _ in range(10):
    qu.quin(input("请输入要入队的信息: "))
while (qu.head < qu.tail):
    print(qu.quout())
