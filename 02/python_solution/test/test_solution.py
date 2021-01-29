from solution import main
from unittest import TestCase


class TestSolution(TestCase):

    def test_1(self):
        part_1, part_2, _time = main(infile="test_1")
        assert part_1 == 58
        assert part_2 == 34

    def test_2(self):
        part_1, part_2, _time = main(infile="test_2")
        assert part_1 == 43
        assert part_2 == 14
