# making a mini game 2048
import random

def start_game(grid):
	for i in range(4):
		grid.append([0]*4)
	add_2(grid)
	add_2(grid)

	print("Instructions To play the game:-\n")
	print("enter 'w' to move up")
	print("enter 'a' to move left")
	print("enter 's' to move down")
	print("enter 'd' to move right")
	return grid

def find_empty(grid):
	for i in range(4):
		for j in range(4):
			if grid[i][j] == 0:
				return i,j
	return None,None

def add_2(grid):
	changed = False
	if all(all(cell != 0 for cell in row) for row in grid):
		return
	i = random.randint(0,3)
	j = random.randint(0,3)
	x=0
	while x<40:
		if grid[i][j] == 0:
			grid[i][j] = 2
			changed = True
			break
		x+=1

	#if empty cell is not found in random
	if not changed:
		i,j=find_empty(grid) 
		if i is not None and j is not None:
			grid[i][j]=2
	
	
def check_win(grid):
	for i in range(4):
		for j in range(4):
			if grid[i][j] == 2048:
				
				return "Won"
	
	for i in range(4):
		for j in range(4):
			if grid[i][j] == 0:
				
				return "Continue"

	for i in range(3):
		for j in range(3):
			if grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i+1][j]:
				
				return "Continue"
				
	for j in range(3):
		if grid[3][j] == grid[3][j+1]:
			
			return "Continue"
		
	for i in range(3):
		if grid[i][3] == grid[i+1][3]:
			
			return "Continue"
			
	return "Lost"

def compress_left(grid): #only works for moving element left
	changed = False
	temp_grid = []
	for i in range(4):
		temp_grid.append([0]*4)
		
	for i in range(4):
		z=0
		for j in range(4):
			if grid[i][j] != 0:	
				temp_grid[i][z] = grid[i][j]
				z+=1
				if z != j:
					changed = True
	grid = temp_grid
	return grid,changed
	
def merge_left(grid): #only works for left
	changed = False
	for i in range(4):
		for j in range(3):
			if grid[i][j] == grid[i][j+1] and grid[i][j]!=0:
				grid[i][j] = grid[i][j]*2
				grid[i][j+1] = 0
				changed = True
	return grid,changed
	
def reverse_grid(grid):
	temp_grid = []
	for i in range(4):
		temp_grid.append([0]*4)
		
	for i in range(4):
		for j in range(4):
			temp_grid[i][j] = grid[i][-j-1] #imp
	return temp_grid

def transpose_grid(grid):
	temp_grid = []
	for i in range(4):
		temp_grid.append([0]*4)
		
	for i in range(4):
		for j in range(4):
			temp_grid[i][j] = grid[j][i]
	return temp_grid

def move_left(grid):
	temp_grid,x=compress_left(grid)
	temp_grid,y=merge_left(temp_grid)
	if x or y:
		temp_grid,moved=compress_left(temp_grid)
	return temp_grid

def move_right(grid):
	temp_grid=reverse_grid(grid)
	temp_grid=move_left(temp_grid)
	temp_grid=reverse_grid(temp_grid)
	return temp_grid

def move_up(grid):
	temp_grid=transpose_grid(grid)
	temp_grid=move_left(temp_grid)
	temp_grid=transpose_grid(temp_grid)
	return temp_grid

def move_down(grid):
	temp_grid=transpose_grid(grid)
	temp_grid=move_right(temp_grid)
	temp_grid=transpose_grid(temp_grid)
	return temp_grid


#main code

if __name__ == "__main__":
	main_grid=[]
	print("enering he loop")
	start_game(main_grid)
	game_status = check_win(main_grid)

	while game_status == "Continue":
	
		print(main_grid[0])
		print(main_grid[1])
		print(main_grid[2])
		print(main_grid[3])
		print(game_status)
	
		player_move=input("enter your move : ").lower()
	
		if player_move == "w":
			main_grid=move_up(main_grid)
		elif player_move == "a":
			main_grid=move_left(main_grid)
		elif player_move == "s":
			main_grid=move_down(main_grid)
		elif player_move == "d":
			main_grid=move_right(main_grid)
		else:
			print("Invalid move")
			continue
		add_2(main_grid)
		game_status=check_win(main_grid)

	if game_status == "Won":
		print(main_grid[0])
		print(main_grid[1])
		print(main_grid[2])
		print(main_grid[3])
		print(game_status)
		
	elif game_status == "Lost":
		print(main_grid[0])
		print(main_grid[1])
		print(main_grid[2])
		print(main_grid[3])
		print(game_status)
		


	
	
	






		

	
	
	

		
	
	
		

			

		
	
	
	
	
	



	
	
	
	




			
	
	
	



