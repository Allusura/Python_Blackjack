#Author: Allusura
#A simple blackjack game I created in my free time after 11 days of study.

import random
import art
import os

def calculate_score(pscore, dscore):

  if pscore == dscore:
    return "Draw 🙃"
  elif dscore == 0:
    return "Lose, opponent has Blackjack 😱"
  elif pscore == 0:
    return "Win with a Blackjack 😎"
  elif pscore > 21:
    return "You went over. You lose 😭"
  elif dscore > 21:
    return "Opponent went over. You win 😁"
  elif pscore > dscore:
    return "You win 😃"
  else:
    return "You lose 😤"

def blackjack():
  os.system('clear')
  print(art.logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  players_hand = []
  dealers_hand = [] 
  players_hand.append(random.choice(cards))
  players_hand.append(random.choice(cards))
  dealers_hand.append(random.choice(cards))
  dealers_hand.append(random.choice(cards))

  player_score = players_hand[0] + players_hand[1]
  dealers_score = dealers_hand[0] + dealers_hand[1]

  print (f"\n\nYour cards: {players_hand}, current score: {player_score}")
  print(f"Computer's first card: {dealers_hand[0]}\n")

  choice = input("Type 'y' to get another card, type 'n' to pass: \n\n")
  if choice == 'y':
    players_hand.append(random.choice(cards))
    player_score = player_score + players_hand[2]
    print(f"\nYour cards: {players_hand}, current score: {player_score}")
  elif choice == 'n':
    pass  
  else:
    print(f"{choice} is an invalid input.")

  print(f"\nComputer's final hand: {dealers_hand}, final score: {dealers_score}\n")

  print(calculate_score(player_score, dealers_score))
  print()

  if input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    blackjack()
  else:
    os.system('clear')
    print("Thanks for playing!\nGoodbye!")

blackjack()
