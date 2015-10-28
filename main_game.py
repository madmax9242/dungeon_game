from character_creation import *
from board_generator import *
from treasure_generator import *

import random
import os

def player_movement(board, player, treasure_list):
	user_input = ""
	while user_input not in ["W", "S", "A", "D", "P", "F"]:
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
		elif user_input == "F":
			print("So far you have found %s." % (", ".join(treasure_list)))
	return board, player

def combat(enemy, player):
	player_attack = random.randint(0, player['attack'])
	player_defense = random.randint(0, player['defense'])
	enemy_attack = random.randint(0, enemy['attack'])
	enemy_defense = random.randint(0, enemy['defense'])
	player_damage = player_attack - enemy_defense
	enemy_damage = enemy_attack - player_defense
	if player_damage > 0 and is_critical(player):
		enemy['health'] -= (player_damage * 2) 
		print("Critical Hit! %s hits for %s. The enemy's health is now %s" % (player['name'], (player_damage * 2), enemy['health']))
	elif player_damage > 0:
		enemy['health'] -= player_damage 
		print("%s hits for %s. The enemy's health is now %s" % (player['name'], player_damage, enemy['health']))
	else:
		print("%s misses" % (player['name']))
	if enemy_damage > 0 and e_crit == 1:
		player['health'] -= (enemy_damage * 2)
	elif enemy_damage > 0:
		player['health'] -= enemy_damage
		print("%s hits for %s. The player's health is now %s" % (enemy['name'], enemy_damage, player['health']))
	else:
		print("%s misses" % (enemy['name']))
	return player, enemy

def is_critical(player):
	chance = random.randint(1,101)
	if chance <= player['crit_chance']:
		return True
	else:
		return False

def enemy_crit(e_crit):
	enemy_ability = input("Do you want to give enemies the ability to get critical hits? Y/N   ")
	if enemy_ability.upper() == 'Y':
		e_crit = 1
		return True, e_crit
	else:
		return False

def main():
	e_crit = 0
	treasure_list = []
	player = create_character()
	enemy_crit(e_crit)
	board = create_board()
	player_location(board, player)
	treasure_name()
	treasure_creator()
	treasure_location(treasure, board)

	while True:
		if len(treasure_list) == 7:
			print("Congratulations. You have found all of the major treasures. Thanks for playing.")
			input()
			
			break
		else:
			os.system('clear')			
			show_board(board)
			board, player = player_movement(board, player, treasure_list)
			print("showing movement")
			if player['quit'] == True:
				break

			if check_treasure(treasure, player, treasure_list) == True:
				treasure_creator()
				treasure_location(treasure, board)

			else:
				encounter_chance = random.randint(1,6)
				if encounter_chance == 6:
					minor_treasure_creator()
					stat_adjuster(player, minor_treasure)
				elif encounter_chance == 1:
					enemy = player_gen(len(treasure_list), True)
					if e_crit == 1:
						enemy['crit_chance'] = 5
					print('You have encountered %s. It has %s health points. Prepare for battle' % (enemy['name'], enemy['health']))
					input()
					while enemy['health'] > 0 and player['health'] > 0:
						os.system('clear')
						combat(enemy, player)
						input()
						if enemy['health'] <= 0:
							print('You are victorious. Press Enter to continue your quest.')
							input()
					if player['health'] <= 0:
						print('Game Over. You died.')
						input()
						break

	

main()
