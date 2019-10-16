

class TicTacToe:
    _x = 'x'
    _o = 'o'
    _free = ' '
    _squares = 9
    _draw = 'Draw'

    def draw(self):
        return self._draw

    def x(self):
        return self._x

    def o(self):
        return self._o

    def draw_instuct(self):
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
        while answer not in range(1, self._squares+1):
            answer = input('Player-'+player+', your move. Choose number 1-9:')
            if answer == 'i':
                self.draw_instuct()
                print(self)
            else:
                answer = int(answer)
        return answer

    def __init__(self):
        self._board = [self._free for i in range(self._squares)]

    def __repr__(self):
        return "\n\
        %s | %s | %s\n\
        ---------\n\
        %s | %s | %s\n\
        ---------\n\
        %s | %s | %s\n" % (self._board[0], self._board[1], self._board[2],\
self._board[3], self._board[4], self._board[5],\
self._board[6], self._board[7], self._board[8])

    def isLegal(self, move):
        return (move in range(1, 10)) and (self._board[move-1] == self._free)

    def find_winner(self):
        winCombinations = ((0, 1, 2), (0, 3, 6), (0, 4, 8),\
         (1, 4, 7), (2, 4, 6), (2, 5, 8), (3, 4, 5), (6, 7, 8))
        for combo in winCombinations:
            if self._board[combo[0]] == self._board[combo[1]] == \
self._board[combo[2]] != self._free:
                win = self._board[combo[0]]
                return win
            if self._free not in self._board:
                return self._draw
        return None

    def next_move(self, player):
        if not isinstance(player, str):
            raise TypeError("Wrong type of varaible player!")
        elif player not in (self._x, self._o):
            raise ValueError('Player have to be "x" or "o"!')
        move = self._ask_move(player)
        while not self.isLegal(move):
            print('\n\nWrong move! Try to choose other move!\n')
            print(self)
            move = self._ask_move(player)
        print("Awesome move!")
        self._board[move-1] = player

    def next_side(self, side):
        if not isinstance(side, str):
            raise TypeError("Wrong type of varaible side!")
        elif side not in (self._x, self._o):
            raise ValueError('Side have to be "x" or "o"!')
        if side == self._x:
            return self._o
        else: 
            return self._x

#call it from main

def game():
    print('\tWelcome to the game!')
    board = TicTacToe()
    board.draw_instuct()
    side = board.x()
    print(board)
    while not board.find_winner():
        board.next_move(side)
        print(board)
        side = board.next_side(side)
    winner = board.find_winner()
    if winner == board.draw():
        print("The winner is not revealed...\n")
    else:
        print("And the winner is\n.\n..\n...\nThe player-"+winner+"!\nCongratulations!\n")
    print('Bye bye!')



if __name__ == '__main__':
    game()