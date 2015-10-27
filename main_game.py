from character_creation import *
from board_generator import *
from treasure_generator import *

def player_movement(board, player):
	user_input = ""
	while user_input not in ["W", "S", "A", "D", "P"]:
		user_input = input("Move your character using W, S, A, or D. W moves the character up. D moves the character to the right. And so on. Press P to quit.").upper()
		if user_input == 'P':
			player['quit'] = True
		elif user_input == 'W':
			if player['x'] > 0:
				board[player['x']][player['y']] = "*"
				player['x'] -= 1
				board[player['x']][player['y']] = "@"
			else:
				print('You have fallen into the abyss. Respawning...')
		elif user_input == 'S':
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
	return board, player 

def combat(enemy, player):
	player_attack = random.randint(0, player['attack'])
	player_defense = random.randint(0, player['defense'])
	enemy_attack = random.randint(0, enemy['attack'])
	enemy_defense = random.randint(0, enemy['defense'])
	player_damage = player_attack - enemy_defense
	enemy_damage = enemy_attack - player_defense
	if player_damage > 0:
		enemy['health'] -= player_damage
		print("%s hits for %s. The enemy's health is now %s" % (player['name'], player_damage, enemy['health']))
	else:
		print("%s misses" % (player['name']))
	if enemy_damage > 0:
		print("%s hits for %s. The player's health is now %s" % (enemy['name'], enemy_damage, player['name']))
	else:
		print("%s misses" % (enemy['name']))
	return player, enemy 

def main():
	player = create_character()
	board = create_board()
	player_location(board, player)
	show_board(board)
	for i in range(6):
		player_movement(board, player)
		show_board(board)

main()
