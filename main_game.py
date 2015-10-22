from character_creation import *
from board_generator import *

def player_movement(board, player):
	user_input = ""
	while user_input not in ["W", "S", "E", "W", "P"]:
		user_input = input("Move your character using W, S, A, or D. W moves the character up. D moves the character to the right. And so on. Press P to quit.").upper()
		if user_input = 'P':
			player['quit'] = True
		elif user_input = 'W':
			if player['x'] > 0:
				board[player['x']][player['y']] = "*"
				player['x'] -= 1
				board[player['x']][player['y']] = "@"
			else:
				print('You have fallen into the abyss. Respawning...')
		elif user_input = 'S':
			if player['x'] < (len(board[0]) - 1):
				board[player['x']][player['y']] = "*"
				player['x'] += 1
				board[player['x']][player['y']] ="@"
			else:
				print('You have fallen into the abyss. Respawning...')
		elif user_input == "A":
			if player ['y'] > 0:
				board[player['x']][player['y']] = "*"
				player['y'] -= 1 
				board[player['x']][player['y']] = "@"
			else:
				print("You have fallen into the abyss. Respawning...")
		elif user_input == 'D':
			if player['y'] < (len(board[0]) - 1):
				board[player['x']][player['y']] = "*"
				player['y'] += 1
				board[player['x']][player['y']] = "@"
			else:
				print ("You have fallen into the abyss. Respawning...")

def main():
	player = create_character()
	board = create_board()
	player_location(board, player)
	show_board(board)

main()