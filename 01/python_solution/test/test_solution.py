from solution import main
from unittest import TestCase


class TestSolution(TestCase):

    def test_input(self):
        part_1, part_2, _time = main(infile="input")
        assert part_1 == None
        assert part_2 == None
