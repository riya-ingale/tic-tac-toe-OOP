from exception import SquareAlreadyMarked, SquareOutOfBoard
class Board:
    def __init__(self):
        self.squares =[" "," "," "," "," "," "," "," "," "," "]
    def display(self):
        print()
        print(" {} | {} | {}".format(self.squares[1],self.squares[2],self.squares[3]))
        print("-----------")
        print(" {} | {} | {}".format(self.squares[4],self.squares[5],self.squares[6]))
        print("-----------")
        print(" {} | {} | {}".format(self.squares[7],self.squares[8],self.squares[9]))
    def update(self,player,square):
        self.squares[square] = player
    def clear(self):
        self.squares =[" "," "," "," "," "," "," "," "," "," "]

    def if_sqaure_empty(self,index):
        if self.squares[index] != " ":
            raise SquareAlreadyMarked
        else:
            return 1
            
    def if_square_onboard(self,index):
        if index<1 or index>9:
            raise SquareOutOfBoard
        else:
            return 1        
            
    

