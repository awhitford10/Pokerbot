import random

class TexasHoldem():

    def __init__(self):
        self.deck = [
            'AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH',
            'AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS',
            'AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD',
            'AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC',]
        self.discard = []
        self.player_hands = {'community':[]}
        self.player_money = {'pot':0}
        self.starting_money = 1000


    def set_players(self):
        #input player names, set initial pot to 1000
        count = 1
        while len(self.player_hands) < 6:
            player = input(f'\nInput player {1} name.\nType "n" to continue with set players \nThere can be 2 to 5 players.\n')
            if player == 'n':
                break
            elif player not in self.player_hands:
                self.player_hands[player] = []
                self.player_money[player] = self.starting_money
                count += 1
            else:
                print(f'\nThere seems to be an error with that name. Either it is already in use or something went wrong.')
            
        if len(self.player_hands) < 2:
            print('There must be between 2 and 5 players.')
            self.player_hands = []
            self.set_players()



    def shuffle(self):
        #add discard to deck and shuffle deck
        self.deck += self.discard
        random.shuffle(self.deck)

    def deal(self, player_hands):
        #initial hand dealt to players, players hands saved in dictionary by player number
        for card in range(2):
            for player in player_hands:
                player_hands[player].append(self.deck.pop())
    
    def flop(self):
        for x in range(3):
            self.player_hands['community'].append(self.deck.pop())

    def discard(self):
        pass

    def bet():
        pass
            

