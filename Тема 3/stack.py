import sys

class Stack:
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
        return self.items.pop()

    def top(self):
        if self.is_empty():
            return 'error'
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        if self.is_empty():
            return 'empty'
        return '->'.join([str(el) for el in self.items])

    def clear(self):
        self.items = []
        print('ok')


commands = []
for line in sys.stdin:
    commands.append(line.split())

s = Stack()
for comm in commands:
    if comm[0] == 'push':
        s.push(int(comm[1]))
    elif comm[0] == 'pop':
        print(s.pop())
    elif comm[0] == 'back':
        print(s.top())
    elif comm[0] == 'size':
        print(s.size())
    elif comm[0] == 'clear':
        s.clear()
    elif comm[0] == 'exit':
        print('bye')
        break