from flask import Flask, render_template, request
# import numpy as np
import backend as backend
    
# create flaskApp
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# health check // WSGI
@app.route('/')
def index():
    return render_template('index_flask_iframe.html')


# 404 handling
@app.errorhandler(404)
def inv_route(e):
    return render_template('404.html')

@app.route('/ttt', methods=['GET', 'POST'])
def ttt():

    ttt_vals = {}

    # when first loading the page: GET
    if request.method == 'GET':
        for i in range(1, 10):
            ttt_vals['btn'+str(i)+'_value'] = '&nbsp;'
            ttt_vals['btn'+str(i)+'_disabled'] = ''
            ttt_vals['btn'+str(i)+'_style'] = "style='color: #000;'"

        ttt_vals['gamestate'] = 'ongoing'
        ttt_vals['winner'] = 'none'
        ttt_vals['boardState'] = [0] * 9

        return render_template('ttt_iframe_game.html', vals=ttt_vals)

    # if request method is POST
    else:

        # get current board state
        # boardState = np.reshape(np.array([backend.Player(int(s)) for s in request.form['boardState'].split(',')]), (3, 3)).tolist()

        # NUMPY BYPASS BECAUSE NAMECHEAP CAN'T INSTALL IT FOR SOME REASON
        boardState = []
        for i in range(3):
            boardState.append([backend.Player(int(s)) for s in request.form['boardState'].split(',')[3*i:(i+1)*3]])

        print(boardState)

        # create TTT object and setBoard to boardState
        t = backend.TicTacToe(symbolAI='O', symbolHuman='X', firstPlayer=backend.Player.Human)
        t.setBoard(boardState)

        # debug: show board
        t.showBoard()

        # check game state
        state, winner = t.checkWinner()

        # if game is still ongoing, bot move
        if state == backend.GameState.Ongoing:
            t.currentPlayer = backend.Player.AI
            _ = t.bestMove()
            t.currentPlayer = backend.Player.Human

            # debug: show board
            t.showBoard()
        
            # check game state
            state, winner = t.checkWinner()

        # update ttt_vals and return
        # boardState = np.ravel(t.board)
        # NUMPY BYPASS BECAUSE NAMECHEAP CAN'T INSTALL IT FOR SOME REASON
        def ravel(arr):
            return [i for j in arr for i in j]

        boardState = ravel(t.board)

        boardState = ['&nbsp;' if i.value == 0 else 'X' if i.value == -1 else 'O' for i in boardState]

        if state == backend.GameState.Ongoing:
            for i in range(1, 10):
                ttt_vals['btn'+str(i)+'_value'] = boardState[i-1]
                if boardState[i-1] != '&nbsp;':
                    ttt_vals['btn'+str(i)+'_disabled'] = 'disabled'
                else:
                    ttt_vals['btn'+str(i)+'_disabled'] = ''
                ttt_vals['btn'+str(i)+'_style'] = "style='color: #000;'"
        
        else:
            for i in range(1, 10):
                ttt_vals['btn'+str(i)+'_disabled'] = 'disabled'
                ttt_vals['btn'+str(i)+'_value'] = boardState[i-1]

        ttt_vals['gamestate'] = state.value
        ttt_vals['winner'] = winner.value
        ttt_vals['boardState'] = [i.value for i in ravel(t.board)]

        return render_template('ttt_iframe_game.html', vals=ttt_vals)
        

if __name__ == "__main__":
    app.run()