from collections import deque

player1 = deque(map(int, input().split()))
player2 = deque(map(int, input().split()))

cnt = 0
lim = 1e6
while cnt < lim:
	if (player1[0] == 0 and player2[0] == 9):
		player1.append(player1.popleft())
		player1.append(player2.popleft())
		
	elif (player1[0] == 9 and player2[0] == 0):
		player2.append(player1.popleft())
		player2.append(player2.popleft())
		
	elif (player1[0] > player2[0]):
		player1.append(player1.popleft())
		player1.append(player2.popleft())
		
	elif (player2[0] > player1[0]):
		player2.append(player1.popleft())
		player2.append(player2.popleft())
		
	cnt += 1
	if not player1:
		print('second', cnt)
		break
	elif not player2:
		print('first', cnt)
		break
	
if player1 and player2:
	print('botva')