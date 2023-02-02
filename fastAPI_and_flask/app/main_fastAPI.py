# uvicorn main_fastAPI:app --host 127.0.0.1 --port 8080 --reload

from fastapi import FastAPI, WebSocket, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import backend as backend

app = FastAPI()
app.mount('/static', StaticFiles(directory='../static'), name='static')
templates = Jinja2Templates(directory='../templates')


@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse('index_fastAPI.html', {'request': request})


@app.websocket('/ws')
async def ws_endpoint(websocket: WebSocket):
    t = backend.TicTacToe(symbolAI='O', symbolHuman='X', firstPlayer=backend.Player.Human)
    boardmap = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    await websocket.accept()

    state, winner = t.checkWinner()

    while state == backend.GameState.Ongoing:

        if t.currentPlayer == backend.Player.Human:
            
            # get user input
            data = await websocket.receive_text()
            chb = data.split(',')[0]
            val = data.split(',')[1]

            # convert to row/col
            row = 0
            col = 0
            for ridx, r in enumerate(boardmap):
                if int(chb[-1]) in r:
                    row = ridx
                    col = r.index(int(chb[-1]))

            print(f'Button: {chb}, Row: {row}, Col: {col}')

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
            chb = 'chb' + str(boardmap[move[0]][move[1]])

            # return AI play
            await websocket.send_text(f'{chb}')
        
        # check game state
        state, winner = t.checkWinner()

        # debug printout
        t.showBoard()

    else:
        if state == backend.GameState.Draw:
            await websocket.send_text('A draw! How boring.')
        
        elif state == backend.GameState.Over:
            if winner == backend.Player.Human:
                await websocket.send_text('You won! This message will never be displayed :D')
            else:
                await websocket.send_text('You lost! It\'s okay. You can always try again (just reload the page)!')


if __name__ == "__main__":
    app = FastAPI()