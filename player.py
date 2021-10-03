class Player:
    def __init__(self,shape):
        self.shape = shape

    def is_winner(self,board):
        if board.squares[1] == self.shape and board.squares[2] == self.shape and board.squares[3] == self.shape:
            return 1
        elif board.squares[4] == self.shape and board.squares[5] == self.shape and board.squares[6] == self.shape:
            return 1
        elif board.squares[7] == self.shape and board.squares[8] == self.shape and board.squares[9] == self.shape:
            return 1
        elif board.squares[1] == self.shape and board.squares[4] == self.shape and board.squares[7] == self.shape:
            return 1
        elif board.squares[2] == self.shape and board.squares[5] == self.shape and board.squares[8] == self.shape:
            return 1
        elif board.squares[3] == self.shape and board.squares[6] == self.shape and board.squares[9] == self.shape:
            return 1
        elif board.squares[1] == self.shape and board.squares[5] == self.shape and board.squares[9] == self.shape:
            return 1
        elif board.squares[3] == self.shape and board.squares[5] == self.shape and board.squares[7] == self.shape:
            return 1
        else:
            return 0



        
