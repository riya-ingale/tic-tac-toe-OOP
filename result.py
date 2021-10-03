class Result:

    def is_tie(self, board):
        count = 0
        for i in range(1, 10):
            if board.squares[i] == " ":
                count += 1
        if count == 0:
            return 1
        else:
            return 0
