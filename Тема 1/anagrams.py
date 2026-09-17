def anagram(word):
    lst = [0] * 255
    for let in word:
        lst[ord(let)] += 1

    return lst


a = input()
b = input()

if anagram(a) == anagram(b):
    print('YES')
else:
    print('NO')