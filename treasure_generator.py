import random 
from board_generator import *

treasure = {}
treasure_list = {}
minor_treasure_list = {}

def treasure_name():
	treasure_list = ["The Holy Hand Grenade of Antioch","A SHRUBBERY!","Camelot. It is a silly place.", "A Farm Animal Catapult", "An Insult Spewing Frenchman", "A Large Wooden Rabbit", "The Staff of Tim", "Brave Sir Robin's Minstrels"]
	treasure['name'] = treasure_list[random.randint(0, (len(treasure_list) - 1))]
	return treasure, treasure_list

def treasure_creator():
	treasure = {}
	treasure['name'] = treasure_name()
	treasure['x'] = 0
	treasure['y'] = 0
	return treasure

def check_treasure(treasure, player, treasure_list):
	found_treasure = False
	if treasure['x'] == player['x'] and treasure['y'] == player['y']:
		print("You have found " + (treasure['name']) + ". Press Enter to continue the journey.")
		input()
		found_treasure = True 
		return found_treasure

def minor_treasure_creator():
	minor_treasure_list = ["a Beer. You gain 5 health", "a Really Sharp Stick. You gain 4 attack", "a Pointy Hat. You gain 3 defense"]
	minor_treasure['name'] = minor_treasure_list[random.randint(0, len(minor_treasure_list) - 1)] 
	return minor_treasure

def stat_adjuster(player, minor_treasure):
	if minor_treasure['name'] == "a Beer. You gain 5 health":
		player['health'] += 5
	elif minor_treasure['name'] == 'a Really Pointy Stick. You gain 3 attack':
		player['attack'] += 3
	elif minor_treasure['name'] == "a Pointy Hat. You gain 3 defense":
		player['defense'] += 3
	return player

