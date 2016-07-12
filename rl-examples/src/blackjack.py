#coding=utf8

import math
import random

def randomCard():
    card = random.randint(1, 13)
    if card > 10:
        card = 10
    return card

def useable_ace(hand):
    val, ace = hand
    return ((ace) and ((val + 10) <= 21))

def totalValue(hand):
    val, ace = hand
    if (useable_ace(hand)):
        return (val + 10)
    else:
        return val

def add_card(hand, card):
    val, ace = hand
    if (card == 1):
        ace = True
    return (val + card, ace)

def eval_dealer(dealer_hand):
    while (totalValue(dealer_hand) < 17):
        dealer_hand = add_card(dealer_hand, randomCard())
    return dealer_hand


# state: (player total, useable ace), (dealer total, useable ace), game status; 
# e.g. ((15, True), (9, False), 1)
# stay or hit => dec == 0 or 1
def play(state, dec):
    player_hand = state[0]
    dealer_hand = state[1]
    if dec == 0: # action = stay
        dealer_hand = eval_dealer(dealer_hand)
        player_tot = totalValue(player_hand)
        dealer_tot = totalValue(dealer_hand)

        status = 1
        if (dealer_tot > 21):
            status = 2  # player wins
        elif (dealer_tot == player_tot):
            status = 3 # draw
        elif (dealer_tot < player_tot):
            status = 2 # player wins
        elif (dealer_tot > player_tot):
            status = 4  # player loses
    
    elif dec == 1:  # action = hit
        # if hit, add new card to player's hand
        player_hand = add_card(player_hand, randomCard())
        d_hand = eval_dealer(dealer_hand)
        player_tot = totalValue(player_hand)
        status = 1
        if (player_tot == 21):
            if (totalValue(d_hand) == 21):
                status = 3 # draw
            else:
                status = 2 # player wins
        elif (player_tot > 21):
            status = 4 # player loses
        elif (player_tot < 21):
            status = 1  # game still in progress
    
    state = (player_hand, dealer_hand, status)
    return state

def initGame():
    status = 1  # 1=in progress; 2=player wins; 3=draw; 4=dealer wins
    player_hand = add_card((0, False), randomCard())
    player_hand = add_card(player_hand, randomCard())
    dealer_hand = add_card((0, False), randomCard())
    # evaluate if player wins from first hand
    if totalValue(player_hand) == 21:
        if totalValue(dealer_hand) != 21:
            status = 2 # player wins after first deal
        else:
            status = 3 # draw

    state = (player_hand, dealer_hand, status)
    return state

if __name__ == '__main__':
    state = initGame()
    print "init state: ", state
    state = play(state, 1)
    print state
