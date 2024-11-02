"""
Tic-Tac-Toe

This program is a simple Tic-Tac-Toe game using classes and objects.
    
    
"""


# define Board class to building the Game Board:

class Board:
     # this constructor initiates the board with empty cells
    def __init__(self):
        self.c = [[" "," "," "],
                  [" "," "," "],
                  [" "," "," "]]
      
    # this method prints the board. Recall that class methods are functions
    def printBoard(self):
        # it first prints the BOARD_HEADER constant
        # BOARD_HEADER constant
        BOARD_HEADER = "-----------------\n|R\\C| 0 | 1 | 2 |\n-----------------"
        print(BOARD_HEADER)
        row_sep="-"*17

        # using a for-loop, it increments through the rows
        for i in range(3):
            print(f"| {i} |{' | '.join(self.c[i])} |")
            print(row_sep)
    
    def resetBoard(self):
        self.c = [[" " for _ in range(3)] for _ in range(3)]

    
# define Game class to implement the Game Logic:

class Game:

    # the constructor
    def __init__(self):
        self.board = Board()
        self.turn = 'X'

    # this method switches players 
    def switchPlayer(self):
        self.turn='O' if self.turn=='X' else 'X'
    
    # this method validates the user's entry
    def validateEntry(self, row, col):
        if 0<=row<3 and 0<=col<3:
            if self.board.c[row][col]==" ":
                return True 
            else:
                print("That cell is already taken.\nPlease make another selection.")
                return False
        else:
            print("Invalid input. Please enter numbers between 0 and 2 for row and column.")
            return False

    # this method checks if the board is full
    def checkFull(self):
        return all(cell!=" " for row in self.board.c for cell in row)

    # this method checks for a winner
    def checkWin(self):
        for row in self.board.c:
            if all(s==self.turn for s in row):
                return True 
        for col in range(3):
            if all(self.board.c[row][col]==self.turn for row in range(3)):
                return True 
        if all(self.board.c[i][i]==self.turn for i in range(3)) or all(self.board.c[i][2-i]==self.turn for i in range(3)):
            return True 
        return False
    # this method checks if the game has met an end condition by calling checkFull() and checkWin()
    # hint: you can call a class method using self.method_name() within another class method, e.g., self.checkFull()
    def checkEnd(self):
        if self.checkWin():
            print(f"\n{self.turn} is the winner!")
            return True
        elif self.checkFull():
            print(f"Draw! Nobody wins!!")
            return True 
        return False 
    
    # this method runs the tic-tac-toe game
     # hint: you can call a class method using self.method_name() within another class method
    def playGame(self):
        game_end=False
        print("New Game: X goes first.")
        while not game_end:
            self.board.printBoard()
            valid_move = False
            while not valid_move:
                try:
                    print(f"\n{self.turn}'s turn: ")
                    row,col=map(int,input(f"Where do you want your {self.turn} placed?\nPlease enter row number and column number separated by a comma\n").split(","))
                    print(f"You have entered row #{row}\n          and column #{col}")
                    valid_move=self.validateEntry(row,col)
                except ValueError:
                    print("Invalid entry.\n Row & Column numbers must be either 0, 1, or 2")
            print("Thank you for your selection.")
            self.board.c[row][col]=self.turn 
            game_end=self.checkEnd()
            if game_end==True:
                self.board.printBoard()
            
            if not game_end:
                self.switchPlayer()
        
# main function
def main():
    # first initializes a variable to repeat the game
    replay='y'
    game=Game()
    # using while-loop that runs until the user says no for another game
    while replay[0].lower()=='y':
        game.board.resetBoard()
        game.turn='X'
        game.playGame()
        replay = input("\nAnother game? Enter yes for replay no to stop. ").strip().lower()
    # goodbye message 
    print("Thank you for playing!")
    
# call to main() function
if __name__ == "__main__":
    main()
