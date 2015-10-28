""" Functions for creating the player and enemy characters """
import random
import os

def name_gen():
	prefixList = ["Bra", "Ma", "Rob", "Ken", "To", "Jo", "Bar", "Mic", "Har", "Quin", "Ad", "An", "Art", "Cyn", "Ty", "Aar", "Tom", "Han", "Lu", "Jam", "Gro", "Gala", "Cod", "Sym", "Just", "Sky", "Sim", "Tom"]
	suffixList = ["don", "ert", "ry", "ah", "her", "hew", "and", "thy", "ash", "by", "lar", "show", "lee", "cy", "ster", "ron", "walker", "solo", "gana", "dam", "tain", "had", "helm", "dan", "long", "tom"]
	title = ["the Barbarian", "the Brave", "the Cowardly", "the Small", "the Magician", "the Silver Fox", "the Just", "the Merciless", "the Not-So-Brave as Everyone Else", "the Chaste", "the Wicked", "the Smuggler", "the Bounty Hunter", "the Super Saiyen", "the Avenger", "the Ranger", "the Warlock", "the Pessimistic", "the Shadow of Death", "the Shade", "the Goblin King", "the Lord of Shadow", "the Undying"]
	randPref = random.randint(0,len(prefixList)-1)
	randSuff = random.randint(0,len(suffixList)-1)
	randTitle = random.randint(0,len(title)-1) 
	firstHalf = prefixList[randPref]
	secondHalf = suffixList[randSuff]
	officialTitle = title[randTitle]
	return firstHalf + secondHalf + " " + officialTitle

def history_gen():
	"""Provides the character's background history"""
	familyHistory = ["You were raised by a family of wolves until you were discovered by a group of nuns at the age of 12.", "You were a simple turtle before being exposed to radioactive sludge, which gave you sentient thought, increased size/strength, and crazy karate skills.", "You are a demi-god that was born when Zeus hooked up with a seagull.", "You were grown in a genetics lab.", "You were \"born\" when your \"parents\" summoned you from the pits of Hell.", "You are on your 5th cycle of reincarnation. Your past 4 forms have been a beetle, a cat, a cow, and a horse."]
	pastJob = ["You were the tallest midget in a carnival.", "You were a soldier in a future war that was sent back in time to protect a woman that was critical to humanity's survival.", "You are a police officer in the Time Enforcement Commission.", "You are a Judge in Mega-City One.", "You were a major in the special forces before becoming a taxi driver. After your cab got destroyed, you and 2 monks assist a super-human in saving the universe.", "Your poor spatial ability led to you designing a Death Star that was cube shaped, which was promply followed by a copyright infringement lawsuit filed by the Borg.", "You were a construction worker until you tried a program called Rekall which reminded you that you're a freedom fighter.", "You tried copying Walter White's recipe, but you created flourescent orange pop rocks instead.", "You were a moderately famous musician.  Your music was used to fight a martian invasion because it made their heads explode.", "You used to be a Sith Master but mass murder was never really your thing, so you left to look for more planetary-friendly professions.", "You are actually a Russian who fights the forces of evil behind the scenes of everyday life.", "You put money to a starter-up business with a colleague, Peter Weyland. You are still waiting to see if you'll receive any profit."]
	funFact = ["You built little robots that you nicknamed, \"Cylons\", which you suspect will never amount to anything beyond household chores.","You found a creepy book made of human flesh inked in blood.  You have a bad feeling about it, but your girlfriend thinks you should read it.", "You completed the Kessel Run in under 12 parsecs.", "You successfully bred swallows that can carry coconuts by themselves.", "Your best friend from childhood was a short, peculiar fellow that didn't talk much but loved Reese's Pieces.  He always wanted to call home.", "You always keep a towel handy at all times, just in case.", "You raised the Killer Rabbit, but due to a faulty locking mechanism on its cage, you unleashed it upon the world.", "You figured out a way to clone dinosaurs, but used frog DNA to keep them all males so they can't reproduce...so everything should be fine.", "You keep waking up in the same room with a sense of deja-vu and the same memories of going to the shore. Strangely, it always seems to be night-time.", "During a stint in a prison where any form of lighting is non-existent, you got a \"surgical shine job\" done on your eyes so you could see in the dark.", "You own a lightsaber, and have only accidentally severed two family members\' arms.", "During a particularly dark time in your life, you would put on a bunny costume, travel across dimensions, and mess with depressed teenagers.", "You are a replicant with only 2 years of life left.", "You were recently exposed to a lethal dose of radiation, so you attached an exosuit to your nervous system.", "Contrary to popular belief, Walt Disney is actually cryogenically frozen in your basement.", "You genetically engineered a racoon that could talk, but then it escaped."]
	history1 = familyHistory[random.randint(0,len(familyHistory)-1)]#Combined two steps from the previous function
	history2 = pastJob[random.randint(0,len(pastJob)-1)]
	history3 = funFact[random.randint(0,len(funFact)-1)]
	return history1 + ("\n") + ("\n") + history2 + ("\n") + ("\n") + history3 + ("\n") + ("\n")

def modifier(m):
	total = 0
	for i in range(m):
		character_stat = random.randint(1,6)
		total += character_stat
	return total

def player_gen(mod, enemyFlag = False):
	player = {}
	player['name'] = name_gen()
	player['history'] = history_gen()
	# Player's position on game board
	player['x'] = 0
	player['y'] = 0
	player['attack'] = (random.randint(3,18) + modifier(mod))
	player['defense'] = (random.randint(3,18) + modifier(mod))
	player['health'] = (random.randint(5,30) + modifier(mod))
	player['crit_chance'] = 0
	player['quit'] = False
	return player 

def create_character():
	"""The main function for this Player Generation program"""
	userInput = ""
	while True:
		player = player_gen(5)# Putting the 5 in here sets both the mod and n variables as 5
		print (player['name'])
		print ("\n")
		print (player['history'])
		print ("Attack: " +  str(player['attack']))
		print ("Defense: " + str(player['defense']))
		print ("Health: " + str(player['health']))
		print ("\n")
		userInput = input("Do you like this character?  Press Enter to generate a new character.  Type \"Y\" to accept your character. Ready to continue?: ")
		os.system('clear')
		if userInput == "Y" or userInput == "y":
		    break
		#print("________________________")
		print("\n")

	return player


