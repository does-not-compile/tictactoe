"""
Backened for TicTacToe
Author: Sebastian Nagel (github: does-not-compile)
"""

#   _____________   _____________   _____________
#   |XXX|XXX|XXX|   |   |XXX|   |   |XXX|XXX|XXX|
#   -------------   -------------   -------------
#   |   |XXX|   |   |   |XXX|   |   |XXX|   |   |
#   -------------   -------------   -------------
#   |   |XXX|   |   |   |XXX|   |   |XXX|XXX|XXX|
#   -------------   -------------   -------------
#
#   _____________   _____________   _____________
#   |XXX|XXX|XXX|   |XXX|XXX|XXX|   |XXX|XXX|XXX|
#   -------------   -------------   -------------
#   |   |XXX|   |   |XXX|XXX|XXX|   |XXX|   |   |
#   -------------   -------------   -------------
#   |   |XXX|   |   |XXX|   |XXX|   |XXX|XXX|XXX|
#   -------------   -------------   -------------
#
#   _____________   _____________   _____________
#   |XXX|XXX|XXX|   |XXX|XXX|XXX|   |XXX|XXX|XXX|
#   -------------   -------------   -------------
#   |   |XXX|   |   |XXX|   |XXX|   |XXX|XXX|   |
#   -------------   -------------   -------------
#   |   |XXX|   |   |XXX|XXX|XXX|   |XXX|XXX|XXX|
#   -------------   -------------   -------------
#

from enum import Enum
from math import *

class Player(Enum):
    AI = 1
    Human = -1
    Blank = 0


class GameState(Enum):
    Ongoing = -1
    Draw = 0
    Over = 1


class TicTacToe():

    def __init__(self, symbolAI: str = 'X', symbolHuman: str = 'O', firstPlayer: Player = Player.AI):

        self.symbolAI = symbolAI
        self.symbolHuman = symbolHuman
        self.currentPlayer = firstPlayer
        self.symbolMap =  {Player.AI: symbolAI, Player.Human: symbolHuman, Player.Blank: '_'}

        self.board = [[Player.Blank, Player.Blank, Player.Blank],
                      [Player.Blank, Player.Blank, Player.Blank],
                      [Player.Blank, Player.Blank, Player.Blank]]

    def showBoard(self):
        """Pretty print of the board.

        Args:
            b (list, optional): Current board.
        """

        b: list = self.board

        for i in range(3):
            print("-"*13)
            for j in range(3):
                if b[i][j] == Player.AI: print(f"| {self.symbolAI} ", end="")
                elif b[i][j] == Player.Human: print(f"| {self.symbolHuman} ", end="")
                else: print("|   ", end="")
            print("|")
        print("-"*13)


    def checkWinner(self):
        """Checks the board for game ending combinations (horizontal, vertical, diagonal).
           Returns (GameState.Ongoing, Player.Blank) if no endstate has been reached (i.e. no win or draw). 
           Depends on classes GameState and Player.

        Args:
            board (list, optional): A list containing the current board status

        Returns:
            GameState, Player: None, None if no endpoint. Winner is None if GameState is Draw.
        """

        b: list = self.board

        # check horizontals
        for i in range(3):
            if b[i][0] != Player.Blank and b[i][0] == b[i][1] and b[i][1] == b[i][2]:
                return GameState.Over, b[i][0]
        # Check verticals
        for i in range(3):
            if b[0][i] != Player.Blank and b[0][i] == b[1][i] and b[1][i] == b[2][i]:
                return GameState.Over, b[0][i]
        # Check diagonals
        if b[0][0] != Player.Blank and b[0][0] == b[1][1] and b[1][1] == b[2][2] or \
           b[0][2] != Player.Blank and b[0][2] == b[1][1] and b[1][1] == b[2][0]:
            return GameState.Over, b[1][1]
        # Check for draw after all else
        blanks = sum([b[i].count(Player.Blank) for i in range(3)])
        if blanks == 0: 
            return GameState.Draw, Player.Blank
        
        # if nothing, return Ongoing,  Blank
        return GameState.Ongoing, Player.Blank


    def _minimax(self, board: list, depth: int, isMaximizing: bool):

        result, winner = self.checkWinner()
        if result != GameState.Ongoing:
            return winner.value
        
        # AI turn
        if isMaximizing:
            highscore = -inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == Player.Blank:
                        board[i][j] = Player.AI
                        score = self._minimax(board, depth+1, False)
                        board[i][j] = Player.Blank
                        if score > highscore:
                            highscore = score
            
            return highscore
        
        # Human turn
        else:
            highscore = inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == Player.Blank:
                        board[i][j] = Player.Human
                        score = self._minimax(board, depth+1, True)
                        board[i][j] = Player.Blank
                        if score < highscore:
                            highscore = score
            
            return highscore


    def bestMove(self):
        # AI turn
        highscore = -inf
        move = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == Player.Blank:
                    self.board[i][j] = Player.AI
                    score = self._minimax(self.board, 0, False)
                    if score > highscore:
                        highscore = score
                        move = [i, j]
                    self.board[i][j] = Player.Blank
        if not move == []:
            self.board[move[0]][move[1]] = Player.AI
            

    def playerMove(self, row: int, col: int):
        # result, winner = self.checkWinner()
        # if result == None and winner == None:
            
        if self.board[row][col] == Player.Blank:
            self.board[row][col] = Player.Human
        else:
            print('Illegal move. Please choose a different field.')
            self.playerMove()


### If executed in the command line, you can play it there:
if __name__ == '__main__':
    result, winner = GameState.Ongoing, Player.Blank
    firstPlayer = input('Who should start (Human: h / AI: a): ')
    if firstPlayer == 'h': 
        currentPlayer = Player.Human
        symbolHuman = 'X'
        symbolAI = 'O'
        game = TicTacToe(symbolAI, symbolHuman, currentPlayer)

    elif firstPlayer == 'a': 
        currentPlayer = Player.AI
        symbolHuman = 'O'
        symbolAI = 'X'
        game = TicTacToe(symbolAI, symbolHuman, currentPlayer)
    else: print('Input not recognized.')

    while result == GameState.Ongoing and winner == Player.Blank:

            if game.currentPlayer == Player.Human:
                move = input('Your move: (row, column): ').split(',')
                row = int(move[0].strip())
                col = int(move[1].strip())
                game.playerMove(row, col)
                game.currentPlayer = Player.AI

            else:
                game.bestMove()
                game.currentPlayer = Player.Human

            result, winner = game.checkWinner()
            game.showBoard()
    else:
        if result == GameState.Draw:
            print(f"Game over! It's a {result.name}! How boring.")
        else:
            print(f"Game over! It's a win for the {winner.name}!")