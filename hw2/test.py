import unittest
from tic_tac_toe import TicTacToe
#-----------------------------tests-------------------------

class TestTicTacToeItems(unittest.TestCase):
    def test_next_side(self):
        test_board = TicTacToe()
        self.assertEqual(test_board.next_side('x'), 'o')
        self.assertEqual(test_board.next_side('o'), 'x')
        with self.assertRaises(TypeError):
            test_board.next_side(1223)
        with self.assertRaises(ValueError):
            test_board.next_side('xo')

    def test_find_winner(self):
        test_board = TicTacToe()
        self.assertEqual(test_board.find_winner(), None)
        test_board._board[0] = 'x'; test_board._board[1] = 'x'; test_board._board[2] = 'x' 
        self.assertEqual(test_board.find_winner(), 'x')
        test_board._board[0] = 'o'; test_board._board[1] = 'o'; test_board._board[2] = 'o' 
        self.assertEqual(test_board.find_winner(), 'o')
        test_board._board[0] = 'o'; test_board._board[5] = 'o'; test_board._board[7] = 'o'; test_board._board[8] = 'o'
        test_board._board[1] = 'x'; test_board._board[2] = 'x'; test_board._board[3] = 'x'; test_board._board[4] = 'x'; test_board._board[6] = 'x'
        self.assertEqual(test_board.find_winner(), 'Draw')

    def test_is_legal(self):
        test_board = TicTacToe()
        self.assertTrue(test_board.is_legal(1))
        self.assertFalse(test_board.is_legal(-10))
        test_board._board[0] = 'x'
        self.assertFalse(test_board.is_legal(1))




if __name__ == '__main__':
    unittest.main()
