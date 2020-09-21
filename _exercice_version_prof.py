#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	return len(string) % 2 == 0


def get_num_char(string, char):
	num_char = 0
	for c in string:
		num_char += 1 if c == char else 0
	return num_char


def get_first_part_of_name(name):
	# Extraire le premier prénom
	first_part = name.split("-")[0]
	# Metre en majuscule la première lettre
	capitalized = first_part[0].upper() + first_part[1:].lower()
	# Faire 'Bonjour, <leNom>'
	return "Bonjour, " + capitalized


def get_random_sentence(animals, adjectives, fruits):
	basic_sentence = "Aujourd’hui, j’ai vu un %s s’emparer d’un panier %s plein de %s."

	# Approche avec répétition de code
	#animal_word = animals[random.randrange(0, len(animals))]
	#adject_word = adjectives[random.randrange(0, len(adjectives))]
	#fruits_word = fruits[random.randrange(0, len(fruits))]

	# Approche sans répétition
	words = []
	for word_set in (animals, adjectives, fruits):
		words += [word_set[random.randrange(0, len(word_set))]]

	# Approche bin cool sur une ligne
	#words = [word_set[random.randrange(0, len(word_set))] for word_set in (animals, adjectives, fruits)]

	return basic_sentence % tuple(words)


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
