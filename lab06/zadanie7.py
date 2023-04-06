import random

def deal_cards():
    suits = ['pik', 'kier', 'karo', 'trefl']
    values = ['As', 'Król', 'Dama', 'Walet', '10', '9', '8', '7', '6', '5', '4', '3', '2']

    deck = [f"{value} {suit}" for suit in suits for value in values]

    random.shuffle(deck)

    players = {}
    for i in range(4):
        player_cards = deck[i*5:(i+1)*5]
        players[f'Gracz {i+1}'] = player_cards

    for player, cards in players.items():
        print(f'{player}: {cards}')

deal_cards()