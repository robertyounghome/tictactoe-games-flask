import random

class TicTacToe:
	def __init__(self, name="Player"):
		self.name = name
		self.board = [[''] * 3 for _ in range(3)]
		self.moves = [[(i,j) for i in range(3)] for j in range(3)]

	def print_board(self):
		for i in range(3):
			print(self.board[i])

	# Return Codes: 0-> Game continues 1-> X wins 2-> O wins 3-> Tie 
	def game_over(self):
		counter = 0
		for i in range(3):
			if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
				if self.board[i][0] == 'X':
					return 1
				elif self.board[i][0] == 'O':
					return 2
			elif self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
				if self.board[0][i] == 'X':
					return 1
				elif self.board[0][i] == 'O':
					return 2
			counter += self.board[i].count('')

		# Check diagonals	
		if (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]) or \
		   (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][2]):
			if self.board[1][1] == 'X':
				return 1
			elif self.board[1][1] == 'O':
				return 2
				
		if counter == 9:
			return 3
		return 0

	def check_board(self):
		a = ['', 'Player wins!', 'Computer wins', 'Tie Game']
		r = self.game_over()
		# Add keeping track of stats
		# Probably return either a blank, Player wins, Computer wins, or Tie Game
		return a[r]

	# Interacts with the application controller
	def player_move(self, i, j):
		self.board[i][j] = 'X'
		print(self.board)
		r = self.check_board()
		return {'value': 'X', 'result': r}

	def computer_move(self):
		k = random.randint(len(self.moves))
		i, j = self.moves[k]
		self.board[i][j] = 'O'
		del self.moves[k]
		self.check_board()

if __name__ == '__main__':
	game = TicTacToe()
	game.print_board()