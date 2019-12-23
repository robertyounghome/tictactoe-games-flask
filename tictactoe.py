import random

class TicTacToe:
	def __init__(self, name="Player"):
		self.name = name
		self.reset()

	def reset(self):
		self.board = [[''] * 3 for _ in range(3)]
		self.moves = []
		for i in range(3):
			for j in range(3):
				self.moves.append((i,j))

	def setName(self, name):
		self.name = name

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
		   (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]):
			if self.board[1][1] == 'X':
				return 1
			elif self.board[1][1] == 'O':
				return 2
				
		if counter == 0:
			return 3
		return 0

	def check_board(self):
		a = ['', f"{self.name} wins!", 'Computer wins', 'Tie Game']
		r = self.game_over()
		# Add keeping track of stats
		# Probably return stats as well
		return a[r]

	def computer_win_or_block(self, value):
		i=j=-1
		for x in range(3):
			if self.board[x].count(value) > 1:
				if '' in self.board[x]:
					j = self.board[x].index('')
					return x, j
			if self.board[0][x] == value and self.board[1][x] == value and self.board[2][x] == '':
				return 2, x
			if self.board[0][x] == value and self.board[2][x] == value and self.board[1][x] == '':
				return 1, x
			if self.board[1][x] == value and self.board[2][x] == value and self.board[0][x] == '':
				return 0, x
		# main diagonal
		if self.board[0][0] == value and self.board[1][1] == value and self.board[2][2] == '':
			return 2, 2
		if self.board[0][0] == value and self.board[2][2] == value and self.board[1][1] == '':
			return 1, 1
		if self.board[1][1] == value and self.board[2][2] == value and self.board[0][0] == '':
			return 0, 0
		# other diagonal
		if self.board[2][0] == value and self.board[1][1] == value and self.board[0][2] == '':
			return 0, 2
		if self.board[2][0] == value and self.board[0][2] == value and self.board[1][1] == '':
			return 1, 1
		if self.board[1][1] == value and self.board[0][2] == value and self.board[2][0] == '':
			return 2, 0
		return i, j


	def get_computer_move(self):
		i, j = self.computer_win_or_block('O')
		print(i,j)
		if (i, j) == (-1,-1):
			i, j = self.computer_win_or_block('X')
		if (i,j) == (-1,-1):
			k = random.randint(0,len(self.moves) - 1)
			i, j = self.moves[k]
		self.board[i][j] = 'O'
		self.moves.remove((i,j))
		return i, j

	# Interacts with the application controller
	# Makes a move for the player
	def player_move(self, i, j):
		self.board[i][j] = 'X'
		print(i,j)
		self.moves.remove((i,j))
		print(self.moves)
		r = self.check_board()
		return {'value': 'X', 'result': r}

	# Interacts with the application controller
	# Makes a move for the computer
	def computer_move(self):
		print('really inside')
		i, j = self.get_computer_move()
		r = self.check_board()
		caller = f"button{i}{j}"
		return {'caller': caller, 'value': 'O', 'result': r}

if __name__ == '__main__':
	game = TicTacToe()
	game.print_board()