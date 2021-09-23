#Declaring the problem
grid = [[3, 0, 5, 4, 0, 2, 0, 6, 0],
		[4, 9, 0, 7, 6, 0, 1, 0, 8],
		[6, 0, 0, 1, 0, 3, 2, 4, 5],
		[0, 0, 3, 9, 0, 0, 5, 8, 0],
		[9, 6, 0, 0, 5, 8, 7, 0, 3],
		[0, 8, 1, 3, 0, 4, 0, 9, 2],
		[0, 5, 0, 6, 0, 1, 4, 0, 0],
		[2, 0, 0, 5, 4, 9, 0, 7, 0],
		[1, 4, 9, 0, 0, 7, 3, 0, 6]]

#Checking whether the entered value is valid or not
def validation(grid, row, col, num):
	#Checking through each column
	for x in range(9):
		if grid[row][x] == num:
			return False

	#Checking through each row
	for x in range(9):
		if grid[x][col] == num:
			return False

	#Checking through each 3x3 boxes
	cornerRow = row - row % 3
	cornerCol = col - col % 3
	for x in range(3):
		for y in range(3):
			if grid[cornerRow + x][cornerCol + y] == num:
				return False

	return True

#Solving the Sudoku puzzle
def solve(grid, row, col):
	if col == 9:
		if row == 8:
			return True
		row += 1
		col = 0

	if grid[row][col] > 0:
		return solve(grid, row, col+1)

	for number in range(1,10):
		if validation(grid, row, col, number):
			grid[row][col] = number

			if solve(grid, row, col+1):
				return True

		grid[row][col] = 0

	return False

#Printing out the unsolved Sudoku puzzle
def unsolved(grid):
	print("Problem: ")
	for i in range(9):
		for j in range(9):
			print(grid[i][j], end = " ")
		print(" ")
	print("\n\n")

unsolved(grid)
print("Solution: ")

#Printing out the Solved Sudoku
if solve(grid,0,0):
	for i in range(9):
		for j in range(9):
			print(grid[i][j], end = " ")
		print("")
else:
	print("No Solution Found")