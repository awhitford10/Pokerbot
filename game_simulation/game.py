import random
import player

class TexasHoldem():

    def __init__(self):
        self.deck = [
            'AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH',
            'AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS',
            'AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD',
            'AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC',]
        self.discard = []
        self.players = {}
        self.community_cards = []
        self.pot = 0
        self.starting_money = 1000


    def set_players(self):
        # ask for user input and create instances of player classes based off names, give each player $1000
        count = 1
        while len(self.players) < 6:
            name = input(f'\nInput player {count} name.\nType "n" to continue with set players \nThere can be 2 to 5 players.\n')
            if name == 'n':
                break
            elif name not in self.players:
                self.players[f'player{count}'] = (player.Player(name))
                self.players[f'player{count}'].money = self.starting_money
                print(self.players[f'player{count}'])
                count += 1
            else:
                print(f'\nThere seems to be an error with that name. Either it is already in use or something went wrong.')
            
        if len(self.players) < 2:
            print('There must be between 2 and 5 players.')
            self.player_hands = []
            self.set_players()



    def shuffle(self):
        #add discard to deck and shuffle deck
        self.deck += self.discard
        random.shuffle(self.deck)

    def deal(self, players):
        #initial hand dealt to players, players hands saved in dictionary by player number
        for x in range(2):
            for player in players:
                players[player].hand.append(self.deck.pop())
    
    def flop(self):
        # sends three cards from the deck to the community cards
        for x in range(3):
            self.community_cards.append(self.deck.pop())

    def end_round(self):
        #Put all players hands in discard and put all cards on table in discard
        self.discard += self.community_cards
        self.community_cards = []
        for player in self.players:
            self.discard += self.players[player].hand
            self.players[player].hand = []        

