#!/usr/bin/env python3

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)


def spades_high(card):
	# print(card)
	rank_value = FrenchDeck.ranks.index(card.rank)
	
	# print('rank_value: %d'%rank_value)
	a = rank_value * len(suit_values) + suit_values[card.suit]
	print(a)
	return rank_value * len(suit_values) + suit_values[card.suit]


class FrenchDeck:
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()
	
	def __init__(self):
		self.cards = [Card(rank, suit) for suit in self.suits
		                               for rank in self.ranks]
	
	def __len__(self):
		return len(self.cards)
	
	def __getitem__(self, item):
		return self.cards[item]


if __name__ == '__main__':
	
	# Part 1
	
	# beer_card = Card(rank = '7', suit = 'diamonds')
	# print(beer_card)
	deck = FrenchDeck()
	# print(deck.ranks)
	# print(len(deck))
	# print(deck[-1])
	#
	# from random import choice
	#
	# deck_choice = choice(deck)
	# print(deck_choice)
	#
	# print(deck[:4])
	#
	# for card in deck:
	#     print(card)
	#
	# in_ = Card('7','Q')  in deck
	# print(in_)
	#
	for card in sorted(deck, key = spades_high):
		print(card)
