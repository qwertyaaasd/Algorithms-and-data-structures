import sys
from functools import cmp_to_key

def compare(x, y):
    if int(x+y) >= int(y+x):
        return -1
    else:
        return 1


lst = sys.stdin.read().split()
lst = sorted(lst, key=cmp_to_key(compare))
print(''.join(lst))