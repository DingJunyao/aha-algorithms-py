"""
队列——基础练习
给定一串数字：631758924，将（对于最初的数字，如果有新增按新增的顺序）第一个数删除，同时将第二个数移至最后，再删除第三个数并把第四个数放到最后……直到只剩下一个数，把该数删除。将删除的数字按顺序给出一个新数。
"""

queue = [0 for _ in range(101)]
queue[0:9] = [6, 3, 1, 7, 5, 8, 9, 2, 4]
head = 0
tail = 9
out = ''
while tail > head :
    # 删除
    out = out + str(queue[head])
    head = head + 1
    # 移位
    queue[tail] = queue[head]
    head = head + 1
    tail = tail + 1
print(out)
