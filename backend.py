from enum import Enum

class Player(Enum):
    Blank = 0
    Human = -1
    AI = 1

class GameState(Enum):
    Ongoing = -1
    Draw = 0
    Over = 1

class TicTacToe():
    """Creates a TicTacToe game"""
    def __init__(self, first: Player = Player.Human):
        self.board = [[Player.Blank, Player.Blank, Player.Blank],
                      [Player.Blank, Player.Blank, Player.Blank],
                      [Player.Blank, Player.Blank, Player.Blank]]
        self.first = first
        self.turn = self.first
        self.state = GameState.Ongoing
        self.winner = Player.Blank

    def setBoard(self, state: list):
        if len(state) == 3 and [len(i) for i in state] == [3, 3, 3]:
            self.board = state
            self.showBoard()
            return self.board

    def move(self, x: int, y: int):
        """Modifies the board with the respective player's symbol. Returns true for valid move and false for invalid move."""
        # validate move
        if x <=2 and y <= 2 and self.board[x][y] == Player.Blank:
            self.board[x][y] = self.turn
            self.evaluate(self.turn)
            self.turn = Player(self.turn.value * -1) # -1 * -1 = 1 and 1 * -1 = -1 --> switches depending on input!
            self.showBoard()
            return True
        else: return False
    
    def evaluate(self, lastPlayer: Player):
        """Check if one player has already won"""
        # not pretty, but does the job:
        # Check horizontals
        if self.board[0][0] != Player.Blank and self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] or \
           self.board[1][0] != Player.Blank and self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] or \
           self.board[2][0] != Player.Blank and self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2]:
            self.state = GameState.Over
            self.winner = lastPlayer
            return self.state, self.winner
        # Check verticals
        if self.board[0][0] != Player.Blank and self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] or \
           self.board[0][1] != Player.Blank and self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] or \
           self.board[0][2] != Player.Blank and self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2]:
            self.state = GameState.Over
            self.winner = lastPlayer
            return self.state, self.winner
        # Check diagnoals
        if self.board[0][0] != Player.Blank and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] or \
           self.board[0][2] != Player.Blank and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            self.state = GameState.Over
            self.winner = lastPlayer
            return self.state, self.winner
        # Check for Draw
        blanks = sum([self.board[i].count(Player.Blank) for i in range(3)])
        if self.state != GameState.Over and blanks == 0: 
            self.state = GameState.Draw
            self.winner = Player.Blank
            return self.state, None

    def showBoard(self):
        for i in range(3):
            print("-"*13)
            for j in range(3):
                if self.board[i][j] == self.first: print("| X ", end="")
                elif self.board[i][j] != self.first and self.board[i][j] != Player.Blank: print("| O ", end="")
                else: print("|   ", end="")
            print("|")
        print("-"*13)


class AI:
    """Calculates the best move based on the Minimax recursive algorithm"""
    def __init__(self, t: TicTacToe):
        self.t = t
        self.score = 0
        self.board = t.board

    def copyState(self):
        newState = [[Player.Blank, Player.Blank, Player.Blank],
                    [Player.Blank, Player.Blank, Player.Blank],
                    [Player.Blank, Player.Blank, Player.Blank]]
        for i in range(3):
            for j in range(3):
                newState[i][j] = self.board[i][j]
        return newState

    def nextMove(self):
        """MiniMax Algorithm"""
        # get current state
        if t.state == GameState.Over and t.winner == Player.AI: return (Player.AI.value, 0)
        elif t.state == GameState.Over and t.winner == Player.Human: return (Player.Human.value, 0)
        elif t.state == GameState.Draw: return (Player.Blank, 0)

        # if game still ongoing, continue:
        moves = []
        emptyFields = []

        for i in range(3):
            for j in range(3):
                if t.board[i][j] == Player.Blank: emptyFields.append(i*3 + (j+1)) # appends fields labeled 1-9 if all are empty
        
        for f in emptyFields:
            move = {}
            move['index'] = f
            newState = self.copyState(self.board)
            t.setBoard(newState)
            #t.move(x, y)           


# START THE GAME
t = None  
def startGame():
    global t
    startingPlayer = input("Human or AI first (h/ai): ")
    if startingPlayer == 'h': 
        t = TicTacToe(Player.Human)
        print("You go first then!")
    elif startingPlayer == 'ai':
        t = TicTacToe(Player.AI)
        print("AI will start!")
    else: 
        print("Input not recognized.")
        startGame()

startGame()

ai = AI(t)
print(ai.nextMove())

# if t != None:
#     while t.state == GameState.Ongoing:
#         coord = input("Please give your next move as coordinates (x, y): ")
#         x, y = coord.split(',')
#         if t.move(int(x), int(y)): t.showBoard()
#         else: pass
#     if t.state == GameState.Over:
#         print("We have a winner! It's ", t.winner.value, "!")
#     elif t.state == GameState.Draw:
#         print("We have a Draw! It's nobody's game!")
