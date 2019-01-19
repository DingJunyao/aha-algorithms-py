"""
堆栈与回文字符串判定

本例用对象实现，仅供学习参考，不要用于正式环境。

回文字符串是指正读反读均相同的字符序列。

示例：
输入：12321
输出：是回文字符串
输入：12345
输出：不是回文字符串
"""


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


st = Stack()
a = input("请输入字符串: ")
mid = len(a) // 2
for i in range(mid):
    st.stin(a[i])
if len(a) % 2 == 0:
    next = mid
else:
    next = mid + 1
while st.top > 0:
    if a[next] != st.stout():
        st.top = st.top + 1
        break
    next = next + 1
if st.top == 0:
    print("是回文字符串")
else:
    print("不是回文字符串")
