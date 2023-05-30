'''
A simple blackjack game
'''
import time, os, csv
import collections
from card_style import make_card
from card_engine import *

def value(hand):
    value = 0
    cards = hand.get_hand()
    if len(cards[0].get_rank()) > 2 and cards[0].get_rank() != 'Ace':
        value += 10
    elif cards[0].get_rank() == 'Ace':
        value += 11
    else:
        value += int(cards[0].get_rank())
    return value

def ranks(hand):
    ranks = []
    for card in hand.get_hand():
        ranks.append(card.get_rank())
    return ranks

def duplicate(ranks):
    if len(ranks) != len(set(ranks)):
        return True
    else:
        return False

def m_aces(counter):
    dupes = []
    for key in counter.keys():
        if counter[key] > 1:
            dupes.append(key)
    if 'Ace' in dupes:
        return True
    else:
        return False

def calc_value(hand):
    value = 0
    for card in hand.get_hand():
        if len(card.get_rank()) > 2 and card.get_rank() != 'Ace':
            value += 10
        elif card.get_rank() == 'Ace':
            value += 1
        else:
            value += int(card.get_rank())
    return value
 
def total_value(hand):
    value = 0
    for card in hand.get_hand():
        if len(card.get_rank()) > 2 and card.get_rank() != 'Ace':
            value += 10
        elif card.get_rank() == 'Ace':
            value += 11
        else:
            value += int(card.get_rank())

        if value > 21:
            if duplicate(ranks(hand)):
                counter = collections.Counter(ranks(hand))
                # print(f"hello I am here{counter}")
                if m_aces(counter):
                    print("here")
                    value = calc_value(hand)
                    value += 10
                    if value > 21:
                        return calc_value(hand)
                else:
                    return calc_value(hand)
            else:
                return calc_value(hand)
    return value
            
def player_start(hand, deck):
    '''
    drew = []
    a = Card('Clubs', '5')
    b = Card('Diamonds', '3')
    drew.append(a)
    drew.append(b)
    '''
    drew = deck.draw_cards(2)
    hand.add_cards(drew)
    print('Player hand:', total_value(hand))
    hand.show_info()

def dealer_start(hand, deck):
    drew = deck.draw_cards(2)
    hand.add_cards(drew)
    print('\nDealer hand:', value(hand))
    hand.show_info(1)

def dealer_open(hand):
    print('\nDealer hand:', total_value(hand))
    hand.show_info()

def p_hit(hand, deck):
    '''
    draw = []
    a = Card('Hearts', '5')
    b = Card('Spades', '3')
    c = Card('Diamonds', 'Ace')
    draw.append(a)
    draw.append(b)
    draw.append(c)
    '''
    draw = deck.draw_card()
    hand.add_card(draw)
    print('\nPlayer hand:', total_value(hand))
    hand.show_info()

def d_hit(hand, deck):
    draw = deck.draw_card()
    hand.add_card(draw)
    print('\nDealer hand:', total_value(hand))
    hand.show_info()

# Initialise the data file
def setup_data(filename):
    if not filename.endswith('.csv'):
        filename += '.csv'
    
    if os.path.isfile(filename):
        return os.path.abspath(filename)
    else:
        with open(filename, 'w', newline='') as file:
            # Write header if needed
            writer = csv.writer(file)
            # writer.writerow(['Header1', 'Header2', 'Header3'])
        return os.path.abspath(filename)
    return os.path.abspath(filename)

# Add hand to data file
def record_hand(filename, row_data):
    filepath = setup_data(filename)
    
    with open(filepath, 'a', newLine='') as file:
        writer = csv.writer(file)
        writer.writerow(row_data)


# Play
def play():
    absolute_filepath = setup_data('saveddata.csv')
    currentscore = [0, 0, 0] # Win, Loss, Draw
    print("Welcome to BlackJack!")
    print("---------------------")
    while True:
        # Creates deck for game
        deck = Deck("Blackjack")

        # Creates player and dealer hands
        player = Hand()
        dealer = Hand()

        dealer_start(dealer, deck)
        player_start(player, deck)
    
        while True:
            if total_value(player) == 21:
                dealer_open(dealer)
                if total_value(dealer) != 21:
                    print("Blackjack! Player wins!\n")
                    currentscore[0] += 1
                    break
                else:
                    print("Tie!\n")
                    break
            choice = input("\nH to hit, S to stand, Q to quit\n")
            if choice.lower() == 'h':
                p_hit(player, deck)
                if total_value(player) == 21:
                    dealer_open(dealer)
                    if total_value(dealer) == 21:
                        print("Tie!\n")
                        currentscore[2] += 1
                        break
                    else:
                        print("Blackjack! Player wins!\n")
                        currentscore[0] += 1
                        break
                elif total_value(player) > 21:
                    print("Player bust! Dealer wins!\n")
                    currentscore[1] += 1
                    break

            if choice.lower() == 's':
                if total_value(dealer) < 17:
                    while total_value(dealer) < 17:
                        d_hit(dealer, deck)
                        time.sleep(1.5)
                    if total_value(dealer) == total_value(player):
                        print("Tie!\n")
                        currentscore[2] += 1
                        break 
                    if total_value(dealer) == 21:
                        print("Dealer wins!\n")
                        currentscore[1] += 1
                        break    
                    if total_value(dealer) > 21:
                        print("Dealer bust! Player wins!\n")
                        currentscore[0] += 1
                        break    
                    if total_value(dealer) > total_value(player):
                        print("Dealer wins!\n")
                        currentscore[1] += 1
                        break    
                    else:
                        print("Player wins!\n")
                        currentscore[0] += 1
                        break
                else:
                    dealer_open(dealer)
                    if total_value(dealer) == total_value(player):
                        print("Tie!\n")
                        currentscore[2] += 1
                        break
                    if total_value(dealer) == 21:
                        print("Dealer wins!\n")
                        currentscore[1] += 1
                        break
                    if total_value(dealer) > 21:
                        print("Dealer bust! Player wins!\n")
                        currentscore[0] += 1
                        break
                    if total_value(dealer) > total_value(player):
                        print("Dealer wins!\n")
                        currentscore[1] += 1
                        break
                    else:
                        print("Player wins!\n")
                        currentscore[0] += 1
                        break

            if choice.lower() == 'q':
                print("Thanks for playing, goodbye!\n")
                print("You have won: " + str(currentscore[0]) + " hands")
                print("You have lost: " + str(currentscore[1]) + " hands")
                print("You have drawn: " + str(currentscore[2]) + " hands")
                
                quit()
            continue
        print("----------- Next Round -----------")
        time.sleep(2)
        continue


if __name__ == "__main__":
    play()
