#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

import exercice


class TestExercice(unittest.TestCase):
	def test_is_even_len(self):
		values = [
			"Spam & eggs",
			"'Tis but a scratch!",
			"This parrot is no more"
		]
		expected = [
			False,
			False,
			True
		]
		output = [exercice.is_even_len(v) for v in values]

		self.assertListEqual(
			output,
			expected,
			"Mauvaise identification de la parité de la longueur de la chaine."
		)

	def test_get_num_char(self):
		values = [
			("Who goes there?", "e"),
			("It is I, Arthur, son of Uther Pendragon", "a"),
			("King of the Brittons, defeater of the Saxons", "t")
		]
		expected = [v[0].count(v[1]) for v in values]
		output = [exercice.get_num_char(v[0], v[1]) for v in values]

		self.assertListEqual(
			output,
			expected,
			"Mauvais calcul du nombre d'occurences du caractère."
		)

	def test_get_first_part_of_name(self):
		values = [
			"Marie-Christine",
			"Louis-Philippe",
			"pierre-luc"
		]
		expected = [
			"Bonjour, Marie",
			"Bonjour, Louis",
			"Bonjour, Pierre"
		]

		output = [exercice.get_first_part_of_name(v) for v in values]
		self.assertListEqual(
			output,
			expected,
			"Mauvaise extraction du premier prénom."
		)

	def test_get_random_sentence(self):
		animals = ("anim1", "anim2", "anim3")
		adjectives = ("adj1", "adj2", "adj3", "adj4")
		fruits = ("fr1", "fr2")

		outputs = [exercice.get_random_sentence(animals, adjectives, fruits) for i in range(10)]
		is_random = False
		for output in outputs:
			if output != outputs[0]:
				is_random = True
		self.assertTrue(
			is_random,
			"Phrases pas aléatoires."
		)


if __name__ == '__main__':
	if not os.path.exists('logs'):
		os.mkdir('logs')
	with open('logs/tests_results.txt', 'w') as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	print(open('logs/tests_results.txt', 'r').read())
