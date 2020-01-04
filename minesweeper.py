# minesweeper program
# three levels Basic, Intermediate, Advanced
import random, itertools
BLANK = '0'
BOMB = '*'

class Minesweeper:
	def __init__(self, name="Player"):
		self.name = name
		self.complexity = [(8,10),(16,40),(24,99)]
		self.level = 1
		self.reset()

	def reset(self):
		self.board_size = self.complexity[self.level][0]
		print(self.board_size)
		self.board = [[BLANK for _ in range(self.board_size)] for _ in range(self.board_size)]
		self.show_board = [[BLANK for _ in range(self.board_size)] for _ in range(self.board_size)]
		self.moves = []
		self.bombs = []
		self.start = True
		for i in range(self.board_size):
			for j in range(self.board_size):
				self.moves.append((i,j))

	def makeMove(self, i, j):
		updates = {}
		updates[(i,j)] = self.board[i][j]
		print(updates)
		if self.board[i][j] == BOMB:
			return updates
		self.moves.remove((i,j))
		if self.board[i][j] == BLANK:
			updates = self.finish_updates(updates)
		return updates

	def makeFirstMove(self, i, j):
		updates={}
		for i1, j1 in itertools.product([0,1,-1],[0,1,-1]):
			i2 = i1 + i
			j2 = j1 + j
			if i2 >= 0 and j2 >= 0 and i2 < self.board_size and j2 < self.board_size:
				self.moves.remove((i2,j2))
				updates[(i2,j2)] = BLANK
		self.place_bombs()
		self.place_numbers()
		updates = self.finish_updates(updates)
		return updates

	def finish_updates(self, updates):
		bfs = []
		for i, j in updates.keys():
			updates[(i,j)] = self.board[i][j]
			if self.board[i][j] == BLANK:
				bfs.append((i,j))
		while len(bfs):
			i,j = bfs.pop()
			for i1, j1 in itertools.product([0,1,-1],[0,1,-1]):
				i2 = i1 + i
				j2 = j1 + j
				if i2 >= 0 and j2 >= 0 and i2 < self.board_size and j2 < self.board_size:
					if (i2,j2) in self.moves:
						self.moves.remove((i2,j2))
						self.show_board[i2][j2] = self.board[i2][j2]
						updates[(i2,j2)] = self.board[i2][j2]
						if self.board[i2][j2] == BLANK:
							bfs.append((i2,j2))
		return updates

	def setName(self, name):
		self.name = name

	def print_board(self):
		for i in range(self.board_size):
			for j in range(self.board_size):
				print(self.board[i][j], end = "")
			print()

	def place_bombs(self):
		number_of_bombs = self.complexity[self.level][1]
		while number_of_bombs:
			x = random.randint(0,len(self.moves) - 1)
			i, j = self.moves[x]
			del self.moves[x]
			self.bombs.append((i,j))
			self.board[i][j] = BOMB
			number_of_bombs-=1

	def place_numbers(self):
		for i in range(self.board_size):
			for j in range(self.board_size):
				if self.board[i][j] != BOMB:
					for i1, j1 in itertools.product([0,1,-1],[0,1,-1]):
						i2 = i1 + i
						j2 = j1 + j
						if i2 >= 0 and j2 >= 0 and i2 < self.board_size and j2 < self.board_size:
							self.board[i][j] = str(int(self.board[i][j]) + (self.board[i2][j2] == BOMB))

	# Interacts with the application controller
	# Makes a move for the player
	def player_move(self, i, j):
		if self.start:
			updates = self.makeFirstMove(i, j)
			self.start = False
		else:
			updates = self.makeMove(i, j)
		r = ""
		if (i,j) in self.bombs:
			r = f"{self.name} loses!"
		if len(self.moves) == 0:
			r = f"{self.name} wins!"
		return {'updates': updates, 'result': r}

	# def bfs_find_blanks(self, i, j):
	# 	bfs = [(i,j)]
	# 	while len(bfs):
	# 		i,j = bfs.pop(0)
	# 		for i1, i2 in [(1,0)]

if __name__ == '__main__':
	game = Minesweeper()
	game.print_board()
	game.makeFirstMove(5,3)
	game.print_board()
