import unittest

from gof import get_neighbors_of, ru1


# class GameOfLifeTest(unittest.TestCase):
# def test_get_neighbors_of_cell_should_return_one(self):
#     cell = (0, 3)
#     result = get_neighbors_of(cell)
#     self.assertEqual(result, 1)

# def test_less_than_2_neighbors(self):
#     result = ru1((0, 3), {(0, 3)})
#     self.assertTrue(result)

# def test_more_than_2_neighbors(self):
#     result = ru1((1, 1), {(1, 1), (0, 1), (0, 2)})
#     self.assertFalse(result)

class GetNeighborsTest(unittest.TestCase):
    def test_zero_neighbors(self):
        result = get_neighbors_of((1, 1), {(1, 1)})
        self.assertEqual(result, 0)

    def test_one_neighbors(self):
        result = get_neighbors_of((1, 1), {(0, 1), (1, 1)})
        self.assertEqual(result, 1)

    def test_two_neighbors(self):
        result = get_neighbors_of((1, 1), {(0, 1), (1, 1), (2, 1)})
        self.assertEqual(result, 2)

    def test__neighbors(self):
        result = get_neighbors_of((1, 1), {(0, 1), (1, 1)})
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
