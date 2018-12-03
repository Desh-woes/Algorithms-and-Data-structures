class PlayingCard:

    def __init__(self, suit, rank):
        self.suit_set = ('Spades', 'Diamonds', 'Hearts', 'Clubs')
        self.rank_set = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')

        if suit in self.suit_set:
            self.suit = suit
        else:
            raise ValueError

        if rank in self.rank_set:
            self.rank = rank
        else:
            raise ValueError

    def __str__(self):
        return 'Your card is a/an ' + self.rank + ' of ' + self.suit


card = PlayingCard('Spades', 'Jack')
print(card)