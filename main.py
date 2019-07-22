import boardset, winner, printing

def play():
	board = [[0,0,0],[0,0,0],[0,0,0]]
	count = 0
	boardset.printyPrint(board)
	while winner.winner(board) == None and printing.checkZero(board) == True:
		plr = count%2
		row = int(input("What row? "))
		col = int(input("What column? "))
		count = printing.changeBoard(plr,board,row,col,count)
		boardset.printyPrint(board)
		count+=1
	if winner.winner(board)!=None:
		print('The winner is player %s!' %(plr+1))
	else:
		print("Cat's game")


if __name__ == '__main__':
	answer = 'yes'
	while answer == 'yes':
		play()
		answer = input('would you like to play again? ')