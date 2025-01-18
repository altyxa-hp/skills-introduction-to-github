class TicToeToe:
	field = [ ["*", '*', '*'],
			  ["*", '*', '*'],
			  ["*", '*', '*']
			]

	def meke_move(self, player, row, col):
		if self.field[row][col] == "x" or self.field[row][col] == 'o':
			return 'занято'
		else:
			self.field[row][col] = player
			

	def check_winner(self):
		winner_combi = []

		for i in self.field:
			winner_combi.append(i)

		row = 0
		column = 0 
		time_arr = []

		while column <= len(self.field) - 1:
			row = 0

			while row <= len(self.field[0]) - 1:
				time_arr.append(self.field[row][column])
				row += 1
			column += 1

			winner_combi.append(time_arr)
			time_arr = []


		row = 0
		column = 0
		time_arr = []

		while row <= len(self.field) - 1:
			time_arr.append(self.field[row][column])
			row, column = row + 1, column + 1

		winner_combi.append(time_arr)

		row = len(self.field) - 1
		column = 0
		time_arr = []
		while column <= len(self.field) - 1:
			time_arr.append(self.field[row][column])
			row, column = row - 1, column + 1

		winner_combi.append(time_arr)

		for i in winner_combi:
			if i.count('x') == 3:
				print("Игрок х выиграл")
				return False

			elif i.count('o') == 3:
				print("Игрок о выиграл")
				return False

		return True

	def check_draw(self):
		res = 0
		for i in self.field:
			if not '*' in i:
				res += 1

			if res == 3:
				print("Ничья")
				return False
		return True




	def display_board(self):
		for i in self.field:
			for j in i:
				print(j, end=" ")
			print()


game = TicToeToe()

print("Игра в крестики нолики!")

player = True

while  game.check_winner() and game.check_draw():
	if player:
		print("Ходит х")

	else:
		print("Ходит о")
	x, y = input("Ввидите кординаты (столбец и строка):").split()

	if player:
		if type(game.meke_move('x', int(x), int(y))) == str:
			print("Это поля занято")
			player = not player

		else:
			game.meke_move('x', int(x), int(y))

	else:
		if type(game.meke_move('o', int(x), int(y))) == str:
			print("Это поля занято")
			player = not player

		else:
			game.meke_move('o', int(x), int(y))

	player = not player 

	game.display_board()

