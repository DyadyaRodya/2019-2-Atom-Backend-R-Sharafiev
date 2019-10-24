"""this is module with game class tic tac toe"""

class TicTacToe:
    """Class for game"""
    X = 'x'
    O = 'o'
    FREE = ' '
    SQUARES = 9
    DRAW = 'Draw'

    @staticmethod
    def draw_instuct():
        """draws instuctions for game"""
        print("""
To make a move enter number 1 to 9.
To see this instuction again enter 'i'.
        
          Board:

        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9
        """)

    def _ask_move(self, player):
        answer = None
        while True:
            answer = input('Player-'+player+', your move. Choose number 1-9:')
            if answer == 'i':
                self.draw_instuct()
                print(self)
            else:
                for i in answer:
                    if (not i.isdigit()) and (i != '-'):
                        return None
                answer = int(answer)
                return answer

    def __init__(self):
        self._board = [self.FREE for i in range(self.SQUARES)]

    def __repr__(self):
        return "\n\
        %s | %s | %s\n\
        ---------\n\
        %s | %s | %s\n\
        ---------\n\
        %s | %s | %s\n" % (self._board[0], self._board[1], self._board[2],\
self._board[3], self._board[4], self._board[5],\
self._board[6], self._board[7], self._board[8])

    def is_legal(self, move):
        """checks move for being legal"""
        return (move in range(1, 10)) and (self._board[move-1] == self.FREE)

    def find_winner(self):
        """looks for winner, checks for draw"""
        win_combinations = ((0, 1, 2), (0, 3, 6), (0, 4, 8),\
         (1, 4, 7), (2, 4, 6), (2, 5, 8), (3, 4, 5), (6, 7, 8))
        for combo in win_combinations:
            if self._board[combo[0]] == self._board[combo[1]] == \
self._board[combo[2]] != self.FREE:
                win = self._board[combo[0]]
                return win
            if self.FREE not in self._board:
                return self.DRAW
        return None

    def next_move(self, player):
        """asks for move, checks it and making it"""
        if not isinstance(player, str):
            raise TypeError("Wrong type of varaible player!")
        if player not in (self.X, self.O):
            raise ValueError('Player have to be "x" or "o"!')
        move = self._ask_move(player)
        while not self.is_legal(move):
            print('\n\nWrong move! Try to choose other move!\n')
            print(self)
            move = self._ask_move(player)
        print("Awesome move!")
        self._board[move-1] = player

    def next_side(self, side):
        """returns next player"""
        if not isinstance(side, str):
            raise TypeError("Wrong type of varaible side!")
        if side not in (self.X, self.O):
            raise ValueError('Side have to be "x" or "o"!')
        if side == self.X:
            return self.O
        return self.X

#call it from main

def game():
    """full game tic tac toe function, using class' methods"""
    print('\tWelcome to the game!')
    board = TicTacToe()
    board.draw_instuct()
    side = board.X
    print(board)
    while not board.find_winner():
        board.next_move(side)
        print(board)
        side = board.next_side(side)
    winner = board.find_winner()
    if winner == board.DRAW:
        print("The winner is not revealed...\n")
    else:
        print("And the winner is\n.\n..\n...\nThe player-"+winner+"!\nCongratulations!\n")
    print('Bye bye!')



if __name__ == '__main__':
    game()
