import sys

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push_front(self, item):
        self.items = [item] + self.items
        print('ok')

    def push_back(self, item):
        self.items.append(item)
        print('ok')

    def pop_front(self):
        if self.is_empty():
            return 'error'
        return self.items.pop(0)

    def pop_back(self):
        if self.is_empty():
            return 'error'
        return self.items.pop()

    def front(self):
        if self.is_empty():
            return 'error'
        return self.items[0]

    def back(self):
        if self.is_empty():
            return 'error'
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        print('ok')


commands = []
for line in sys.stdin:
    commands.append(line.split())

d = Deque()
for comm in commands:
    if comm[0] == 'push_back':
        d.push_back(int(comm[1]))
    elif comm[0] == 'push_front':
        d.push_front(int(comm[1]))
    elif comm[0] == 'pop_back':
        print(d.pop_back())
    elif comm[0] == 'pop_front':
        print(d.pop_front())
    elif comm[0] == 'front':
        print(d.front())
    elif comm[0] == 'back':
        print(d.back())
    elif comm[0] == 'size':
        print(d.size())
    elif comm[0] == 'clear':
        d.clear()
    elif comm[0] == 'exit':
        print('bye')
        break