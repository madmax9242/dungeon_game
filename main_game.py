from character_creation import *
from board_generator import *
from treasure_generator import *

def main():
	player = create_character()
	board = create_board()
	player_location(board, player)
	show_board(board)

main()