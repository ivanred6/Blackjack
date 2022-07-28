'''
A simple blackjack game
'''
from card_style import make_card
from card_engine import *


def start_hand(hand, deck):
    drew = deck.draw_cards(2)
    hand.add_cards(drew)
    return hand


def draw(deck):
    pass

# Play
def play():
    # Creates deck for game
    deck = Deck("Blackjack")

    # Creates player and dealer hands
    player = Hand(deck.draw_cards(2))
    dealer = Hand()

    player.add_cards(deck.draw_cards(2))
    dealer.add_cards(deck.draw_cards(2))
    player.add_cards(deck.draw_cards(2))
    dealer.add_cards(deck.draw_cards(2))
    print(player)
    print(dealer)

    player.show_info()
    dealer.show_info()

    print(deck.get_len_deck())
    

    


if __name__ == "__main__":
    play()
