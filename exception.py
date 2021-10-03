class SquareAlreadyMarked(Exception):
    def __str__(self):
        return "The Square is not empty, Select an empty square\n"
        pass

class SquareOutOfBoard(Exception):
    def __str__(self):
        return "The Square is not on the board, Select a square on the board\n"
        pass
