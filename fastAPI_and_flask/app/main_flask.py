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

from flask import Flask, render_template
from flask_sock import Sock
import backend as backend
    
# create flaskApp
app = Flask(__name__, template_folder='../templates', static_folder='../static')
# socketio = SocketIO(app)
sock = Sock(app)

# health check // WSGI
@app.route('/')
def index():
    return render_template('index_flask_sock.html')


@sock.route('/ws')
def ttt(sock):

    t = backend.TicTacToe(symbolAI='O', symbolHuman='X', firstPlayer=backend.Player.Human)
    boardmap = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    #sock.accept()

    state, winner = t.checkWinner()

    while state == backend.GameState.Ongoing:

        if t.currentPlayer == backend.Player.Human:
            
            # get user input
            btn = sock.receive()

            # convert to row/col
            row = 0
            col = 0
            for ridx, r in enumerate(boardmap):
                if int(btn[-1]) in r:
                    row = ridx
                    col = r.index(int(btn[-1]))

            print(f'Button: {btn}, Row: {row}, Col: {col}')

            # player move
            t.playerMove(row, col)

            # change current player
            t.currentPlayer = backend.Player.AI
        
        else:
            # AI move
            move = t.bestMove()
            
            # change current player
            t.currentPlayer = backend.Player.Human
            
            # convert move to button name
            btn = 'btn' + str(boardmap[move[0]][move[1]])

            # return AI play
            sock.send(f'{btn}')
        
        # check game state
        state, winner = t.checkWinner()

        # debug printout
        t.showBoard()

    else:
        if state == backend.GameState.Draw:
            sock.send('A draw! How boring.')
        
        elif state == backend.GameState.Over:
            if winner == backend.Player.Human:
                sock.send('You won! This message will never be displayed :D')
            else:
                sock.send('You lost! It\'s okay. You can always try again (just reload the page)!')


if __name__ == "__main__":
    app.run()