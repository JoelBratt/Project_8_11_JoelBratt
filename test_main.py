"""
test_main.py
Joel Bratt
Automated unit tests to verufy the logic of the Board class.
7/9/2026
"""
import unittest
from classes import Board, CPU

class testlogic(unittest.TestCase):
    """test the game logic"""

    def setUp(self):
        """runs before each test to set up a fresh board"""

        self.board = Board()
        self.cpu = CPU("CPU", "X")

    def test_open_spots_initial(self):
        """Makes sure new board has 9 slots"""

        open_spots = self.board.get_open_spots()
        self.assertEqual(len(open_spots), 9)

    def test_horizontal_win(self):
        """Test that the board correctly identifies a horizontal win"""

        self.board.spots[0] = "X"
        self.board.spots[1] = "X"
        self.board.spots[2] = "X"

    def test_cpu_random_choice(self):
        """Test that the CPU picks a valid spot from the list."""
        available = [1, 5, 9]
        pick = self.cpu.pick_spot(available)

        self.assertIn(pick, available)

if __name__ == '__main__':
    unittest.main()