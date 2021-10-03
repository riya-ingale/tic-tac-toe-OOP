import board as b
import player as p
import result as r
from exception import SquareAlreadyMarked, SquareOutOfBoard

print("\nTIC-TAC-TOE\nGame Initiated..\n")
board = b.Board()
X = p.Player("X")
O = p.Player("O")
result = r.Result()

while(True):
    board.display()
    print("\n'X' plays")
    
    while True:
        x_sqaure = int(input("Select the square (1 to 9) - "))
        try:
            board.if_square_onboard(x_sqaure)
            board.if_sqaure_empty(x_sqaure)
            break
        except SquareAlreadyMarked as sam:
            print("SqaureAlreadyMarked : ",sam)
            continue
        except SquareOutOfBoard as sob:
            print("SqaureOutOfBoard : ",sob) 
            continue 

    board.update("X", x_sqaure)
    if X.is_winner(board):
        board.display()
        print("\nX WON!")
        answer = input("Do you want to play again? (Y/N) - ").lower()
        if answer == "y":
            board.clear()
            continue
        else:
            break
    if result.is_tie(board):
        board.display()
        print("\nThe Game is tied, No one Won")
        answer = input("Do you want to play again? (Y/N) - ").lower()
        if answer == "y":
            board.clear()
            continue
        else:
            break
    board.display()
    print("\n'O' plays")
    while True:
        o_sqaure = int(input("Select the square (1 to 9) - "))
        try:
            board.if_square_onboard(o_sqaure)
            board.if_sqaure_empty(o_sqaure)
            break
        except SquareAlreadyMarked as sam:
            print("SqaureAlreadyMarked : ",sam)
            continue
        except SquareOutOfBoard as sob:
            print("SqaureOutOfBoard : ",sob) 
            continue
    board.update("O", o_sqaure)
    if O.is_winner(board):
        board.display()
        print("\nO WON!")
        answer = input("Do you want to play again? (Y/N) - ").lower()
        if answer == "y":
            board.clear()
            continue
        else:
            break
    if result.is_tie(board):
        board.display()
        print("\nThe Game is tied, No one Won")
        answer = input("Do you want to play again? (Y/N) - ").lower()
        if answer == "y":
            board.clear()
            continue
        else:
            break
