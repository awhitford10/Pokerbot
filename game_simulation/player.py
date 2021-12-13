
class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money =0

    def __str__(self):
        return f'Player name:{self.name} \nPlayer Money:{self.money}\nPlayer hand:{self.hand}'

    def bet(self, amount):
        while True:
            if amount <= self.money:
                self.money -= amount
                return(amount)
            elif amount > self.money:
                print('Not enough money for bet.')

    def fold(self):
        discard = self.hand
        self.hand = []
        return(discard)


