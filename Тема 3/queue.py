import sys

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        print('ok')

    def pop(self):
        if self.is_empty():
            return 'error'
        return self.items.pop(0)

    def top(self):
        if self.is_empty():
            return 'error'
        return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        print('ok')


commands = []
for line in sys.stdin:
    commands.append(line.split())

q = Queue()
for comm in commands:
    if comm[0] == 'push':
        q.push(int(comm[1]))
    elif comm[0] == 'pop':
        print(q.pop())
    elif comm[0] == 'front':
        print(q.top())
    elif comm[0] == 'size':
        print(q.size())
    elif comm[0] == 'clear':
        q.clear()
    elif comm[0] == 'exit':
        print('bye')
        break