import sys
import heapq as h


ls = []
h.heapify(ls)

input_data = sys.stdin.readlines()

for line in input_data:
    command = line.split()
    if command[0] == 'CLEAR':
        ls = []
    elif command[0] == 'ADD':
        h.heappush(ls, -1 * int(command[1]))
    elif command[0] == 'EXTRACT':
        if ls == []:
            print('CANNOT')
        else:
            print(-1 * h.heappop(ls))
