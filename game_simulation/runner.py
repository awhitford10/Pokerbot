import game

gt = game.TexasHoldem()

gt.set_players()

gt.shuffle()

gt.deal(gt.players)

gt.deck_to_community(3)


print(  f'_______________________________________________\n',
        'state after flop\n',
        f'\n\nDeck: {gt.deck}\n',
        f'Player:{[f"{gt.players[x].name},{gt.players[x].money},{gt.players[x].hand} " for x in gt.players]}\n',
        f'Community: {gt.community_cards}',
        f'Discard:{gt.discard}\n',
        f'_______________________________________________\n')

gt.end_round()
print(  f'_______________________________________________\n',
        'state after end round\n',
        f'\n\nDeck: {gt.deck}\n',
        f'Player:{[f"{gt.players[x].name},{gt.players[x].money},{gt.players[x].hand} " for x in gt.players]}\n',
        f'Community: {gt.community_cards}',
        f'Discard:{gt.discard}\n',
        f'_______________________________________________\n')

