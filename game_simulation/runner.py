import game

gt = game.TexasHoldem()

gt.set_players()

gt.shuffle()

gt.deal(gt.player_hands)

gt.flop()

print(f'\n\nDeck: {gt.deck}\nHands:{gt.player_hands}\nDiscard:{gt.discard}\nMoney:{gt.player_money}')

