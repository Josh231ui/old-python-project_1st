from random import choice


choices = ['rock', 'paper', 'scissor', 'lizard', 'spock']
game_on = True

print("Rock-Paper-Scissor-Lizard-Spock\n")

print("\t[Rock] [Paper] [Scissor] [Lizard] [Spock]")
print("The bot have chosen an option: Your Turn....")
while game_on:
	bot_choice = choice(choices)

	print("\t[Rock] [Paper] [Scissor] [Lizard] [Spock]")
	player_choice = input("")
	if player_choice == "q" or player_choice == "quit":
		game_on = False
	else:
		if player_choice.lower() in choices:
			print(f"Reveal: The player bot choosed {bot_choice}")
			if player_choice.lower() == "rock":
				if player_choice.lower() == bot_choice:
					print("Draw")
				elif bot_choice == "scissor" or bot_choice == "lizard":
					print("You Win")
				else:
					print("You lose")

			elif player_choice.lower() == "paper":
				if player_choice.lower() == bot_choice:
					print("Draw")
				elif bot_choice == "rock" or bot_choice == "spock":
					print("You Win")
				else:
					print("You lose")
				

			elif player_choice.lower() == "scissor":
				if player_choice.lower() == bot_choice:
					print("Draw")
				elif bot_choice == "paper" or bot_choice == "lizard":
					print("You Win")
				else:
					print("You lose")
				

			elif player_choice.lower() == "lizard":
				if player_choice.lower() == bot_choice:
					print("Draw")
				elif bot_choice == "paper" or bot_choice == "spock":
					print("You Win")
				else:
					print("You lose")
				

			elif player_choice.lower() == "spock":
				if player_choice.lower() == bot_choice:
					print("Draw")
				elif bot_choice == "rock" or bot_choice == "scissor":
					print("You Win")
				else:
					print("You lose")

		else:
			print(f"{player_choice} doesn't exist in the game\n")
			continue
print("\nThank You for Playing\n")
