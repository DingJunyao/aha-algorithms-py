"""
小猫钓鱼

将一副扑克牌平分为两份，每人拿一份。
每个人交替拿出自己手中的第一张牌放在桌上刚刚被打出的牌的上面（首次出牌就放在桌上）。
如果某人打出的牌与桌上已有的牌的数字相同，即可将两张相同的牌及其中间所有的牌全部取走，依次（越在上面的越先拿）放在自己手中的牌的末尾。
当任意一人先出完牌，游戏结束，对方获胜。

假如游戏开始时，A手里的牌依次为2 4 1 2 5 6，B的为3 1 3 5 6 4。牌面限定为1~9，A先手。判断谁获胜。

本代码使用对象进行实现，使用了2_1_2和2_2_1的相关代码。

这里面有一个问题：当一方出牌后，如果能够从桌上拿牌，但手上已经打完牌，这个时候是判对方赢还是拿牌？
从输出结果上看，原书上的处理方式似乎是：拿牌，游戏继续。
本代码也如此处理。如果是前者，则获胜结果相反。
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


class Stack:
    def __init__(self, num=100):
        """
        堆栈的初始化
            :param num=100: 可选，初始化的堆栈的可容纳元素数目，默认为100
        """
        self.data = [0 for _ in range(num)]
        self.top = 0

    def stin(self, in_data):
        """
        入栈，将数据加入堆栈顶，返回数据
            :param in_data: 入栈的数据
        """
        self.top = self.top + 1
        self.data[self.top - 1] = in_data
        return in_data

    def stout(self):
        """
        出栈，将堆栈顶的数据删除，返回对应的数据
        """
        self.top = self.top - 1
        return self.data[self.top]


# 初始化
table = Stack(10)
a = Queue(1000)
b = Queue(1000)
for i in [2, 4, 1, 2, 5, 6]:
    a.quin(i)
for i in [3, 1, 3, 5, 6, 4]:
    b.quin(i)
book = [0 for _ in range(10)]

while True:
    # A出牌
    ao = table.stin(a.quout())
    # A拿牌
    if book[ao] > 0:
        a.quin(table.stout())
        while True:
            ai = a.quin(table.stout())
            book[ai] = book[ai] - 1
            if ai == ao:
                break
    else:
        book[ao] = 1
    if a.head == a.tail:
        print("B赢")
        print("此时A手中的牌：%s" % a.data[a.head:a.tail])
        print("此时B手中的牌：%s" % b.data[b.head:b.tail])
        print("此时桌子上的牌：%s" % table.data[:table.top])
        break
    # B出牌
    bo = table.stin(b.quout())
    # B拿牌
    if book[bo] > 0:
        b.quin(table.stout())
        while True:
            bi = b.quin(table.stout())
            book[bi] = book[bi] - 1
            if bi == bo:
                break
    else:
        book[bo] = 1
    if b.head == b.tail:
        print("A赢")
        print("此时A手中的牌：%s" % a.data[a.head:a.tail])
        print("此时B手中的牌：%s" % b.data[b.head:b.tail])
        print("此时桌子上的牌：%s" % table.data[:table.top])
        break
