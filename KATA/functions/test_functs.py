from unittest import TestCase

from functions.functs import unique_in_order, count_bits


class Test(TestCase):

    def test_count_bits(self):
        self.assertEqual(count_bits(1234), 5)

    def test_unique_in_order(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'),
                         ['A', 'B', 'C', 'D', 'A', 'B'])
