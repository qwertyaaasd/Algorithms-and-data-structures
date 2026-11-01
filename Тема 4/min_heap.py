class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def shift_up(self, i):
        while i // 2 > 0 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def shift_down(self, i):
        while i * 2 <= self.size:
            j = self.ind_min_child(i)
            if self.heap[j] < self.heap[i]:
                self.heap[j], self.heap[i] = self.heap[i], self.heap[j]
            i = j

    def ind_min_child(self, i):
        if 2 * i + 1 > self.size:
            return 2 * i
        if self.heap[2 * i]  > self.heap[2 * i + 1]:
            return 2 * i + 1
        return 2 * i

    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.shift_up(self.size)

    def extract(self):
        if self.size == 0:
            return None
        
        removed = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.shift_down(1)

        return removed

    def print_heap(self):
        print(self.heap)


n = int(input())
ls = list(map(int, input().split()))

heap = Heap()
for el in ls:
    heap.insert(el)

for _ in range(n):
    print(heap.extract(), end = ' ')
