from random import randint

# RPS Game - Give the user some weapon options

player = ["rock", "paper", "scissors"] 



player_lives = 5
ai_lives = 5

total_lives = 5

print("===========*/ RPS GAME /*===========")
print("Computer lives:", ai_lives, "/", total_lives)
print("Player Live:", player_lives, "/", total_lives)
print("====================================")



# computer is our Ai opponent - let it make a choice
computer = player[randint (0, 2)]

#give the user some weapon options
player = input("Pick Rock, Paper or Scissors: ")

# validate that the input worked
print("player chose: " + player) 
print("Ai chose: " + computer) 

# check to see who won or if it's a tie
if (computer == player):
	print("tie")
	#reset the game loop and have the user choose again

elif (computer == "rock"):
	if (player == "scissors"):
		print("you lose!")
		player_lives = player_lives - 1
	else:
		print("you won!")
		#take a life away from the Ai
		ai_lives = ai_lives - 1

elif (computer == "paper"):
	if (player == "rock"):
		print("you lose!")
		player_lives = player_lives - 1
	else:
		print("you won!")
		#take a life away from the Ai
		ai_lives = ai_lives - 1

elif (computer == "scissors"):
	if (player == "paper"):
		print("you lose!")
		player_lives = player_lives - 1
	else:
		print("you won!")
		#take a life away from the Ai
		ai_lives = ai_lives - 1

print("player lives:", player_lives)
print("ai lives:", ai_lives)











		
