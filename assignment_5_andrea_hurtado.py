"""
Assignment 5
"""

import random
import time

#Function to add up value of drawn cards
def cards_total(*drawn_cards):
    total = 0
    for number in drawn_cards:
        total += number
    return total

#Dealer's turn function, comes into effect after user stands or gets 21
def dealers_turn(user_cards, dealer_cards):
    print(f'\nThe dealer reveals the hidden card of {dealer_cards[-1]} and has a total of {cards_total(*dealer_cards)}.\n')
    time.sleep(1.5)

    #loop for dealer's card sum
    while cards_total(*dealer_cards) <= 16:
        dealer_cards.append(random.randint(1, 10))
        print(f'Hit! The dealer draws {dealer_cards[-1]}. The dealer\'s total is {cards_total(*dealer_cards)}.\n')
        time.sleep(1.5)

    #card sum outputs
    if cards_total(*dealer_cards) > 21:
        print('The dealer busts. You win!\n')
        time.sleep(1.5)

    elif cards_total(*dealer_cards) in range(17, 22):
        print('The dealer stands.\n')
        time.sleep(1.5)

        print(f'Your total is {cards_total(*user_cards)} and the dealer\'s total is {cards_total(*dealer_cards)}.\n')
        time.sleep(1.5)

        if cards_total(*user_cards) == cards_total(*dealer_cards) or cards_total(*user_cards) < cards_total(*dealer_cards):
            print('The dealer wins!\n')
            time.sleep(1.5)

        else:
            print('You win!\n')
            time.sleep(1.5)

#Blackjack program start
print("Welcome to Blackjack.")

#Loop to invite user to start a blackjack game
while True:
    print(f'{"":-^50}\n')

    #Empty lists to add drawn cards
    user_drawn_cards = []
    dealer_drawn_cards = []

    game_starter = input("Do you wish to start a new game? (y/n): ").lower()

    #verifies user's input follows requirement
    while len(game_starter) == 0 or game_starter not in ["y", "n"]:
        game_starter = input("Invalid input. Do you wish to start a new game? (y/n): ").lower()

    if game_starter == "n":
        print("\nOkay! Have a great day.")
        quit()

    for i in range(2): #obtains first two cards for user and dealer
        user_drawn_cards.append(random.randint(1, 10))
        dealer_drawn_cards.append(random.randint(1, 10))

    print(f'\nYou draw a {user_drawn_cards[0]} and a {user_drawn_cards[1]}. Your total is {cards_total(*user_drawn_cards)}.')
    time.sleep(1.5)

    print(f'The dealer draws a {dealer_drawn_cards[0]} and a hidden card.\n')
    time.sleep(1.5)

    user_decision = input('Hit or stand? (h/s): ').lower()

    #verifies user's input follows requirement
    while len(user_decision) == 0 or user_decision not in ["h", "s"]:
        user_decision = input('Invalid input. Hit or stand? (h/s): ').lower()

    #loop for hit/stand decisions and cards sum outpus
    while user_decision == 'h':
        user_drawn_cards.append(random.randint(1, 10))

        if cards_total(*user_drawn_cards) > 21:
            print(f'\nUh oh! You draw a {user_drawn_cards[-1]}. Your total is {cards_total(*user_drawn_cards)}. You lost the game.')
            break

        if cards_total(*user_drawn_cards) == 21:
            print(f'\nYou draw a {user_drawn_cards[-1]}. Your total is {cards_total(*user_drawn_cards)}. You stand.')
            dealers_turn(user_drawn_cards, dealer_drawn_cards)
            break

        user_decision = input(f'\nHit! You draw a {user_drawn_cards[-1]}. Your total is {cards_total(*user_drawn_cards)}. Hit or stand? (h/s): ')

        while len(user_decision) == 0 or user_decision not in ["h", "s"]:
            user_decision = input('Invalid input. Hit or stand? (h/s): ').lower()

    if user_decision == 's':
        print('\nYou stand.')
        dealers_turn(user_drawn_cards, dealer_drawn_cards)
