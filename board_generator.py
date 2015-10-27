import random
from character_creation import *

print("Welcome to Monty Python's Artifact Hunt. You will be asked to determine what size board you wish to play on. Then a random character will be generated for you.  If you wish to keep that character, press Y and start the game. If you would like another character, press Enter. Once you're placed on the board, you will wander around looking for treasure.  If you can find 7 treasures, you win. Press Enter to begin your search, and good luck!")
input()
userHeight = int(input("How tall should the board be?"))
userWidth = int(input("How wide should the board be?"))
print('\n')

def create_board():
	board = []
	tempList = []
	for i in range(userWidth):
		tempList.append('*')
	for i in range(userHeight):
		board.append(list(tempList))
	return board

def show_board(board):
	for i in range(0,(userHeight)):
		print("|".join(board[i]))

def player_location(board, player):
	player['x'] = random.randint(0, (len(board[0])) - 1)
	player['y'] = random.randint(0, (len(board)) - 1)
	board[player['y']][player['x']] = "@"
	return board, player