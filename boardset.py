def printyPrint(board):
	top = '     |     |'
	divider = '------------------'
	print(top)
	print(' ',board[0][0],' | ',board[0][1],' | ',board[0][2])
	print(divider)
	print(' ',board[1][0],' | ',board[1][1],' | ',board[1][2])
	print(divider)
	print(' ',board[2][0],' | ',board[2][1],' | ',board[2][2])
	print(top)

if __name__=="__main__":
	board = [[1,2,3],[4,5,6],[7,8,9]]
	printyPrint(board)