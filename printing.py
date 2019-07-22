def changeBoard(plr,board,row,col,count):
	y = abs(row-3)
	x = col-1
	if board[y][x] != 0:
		print("Bitch, you tryna fool? Go again.")
		count-=1
	elif plr == 0:
		board[y][x] = 'x'
	elif plr == 1:
		board[y][x] = 'o'
	return count

def printyPrint(thing):
	for i in thing:
		print(i)

def checkZero(board):
	for i in board:
		for x in i:
			# print(x)
			if x == 0:
				return True
				break
	return False
	
if __name__=='__main__':
	board = [[0,0,0],[0,0,0],[0,0,0]]
	count = 0
	printyPrint(board)
	while checkZero(board):
		plr = count%2
		inprow = int(input('What row? '))
		inpcol = int(input('What column? '))
		changeBoard(board,plr,inprow,inpcol)
		printyPrint(board)
		count += 1