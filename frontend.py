"""
Streamlit Frontend for snagel.io: TicTacToe
Author: Sebastian Nagel (github: does-not-compile)
"""

import streamlit as st
import backend as backend

# styling
st.set_page_config(
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# TIC TAC TOE"
    }
)

# initialize session_state
if 't' not in st.session_state: st.session_state.t = None
if 'result' not in st.session_state: st.session_state.result  = backend.GameState.Ongoing
if 'winner' not in st.session_state: st.session_state.winner = backend.Player.Blank
if 'AIWin' not in st.session_state: st.session_state.AIWin = 0
if 'HumanWin' not in st.session_state: st.session_state.HumanWin = 0
if 'Draw' not in st.session_state: st.session_state.Draw = 0


if st.session_state.t == None:
    choice = st.selectbox('Who should start:', ["Please select", "AI", "Human (that's you!)"])
    if choice == "AI":
        st.session_state.t = backend.TicTacToe(symbolAI='X', symbolHuman='O', firstPlayer=backend.Player.AI)
        st.experimental_rerun()
    elif choice == "Human (that's you!)":
        st.session_state.t = backend.TicTacToe(symbolAI='O', symbolHuman='X', firstPlayer=backend.Player.Human)
        st.experimental_rerun()
else:
    # check for end condition
    st.session_state.result, st.session_state.winner = st.session_state.t.checkWinner()

    def callback(row, col):
        # on button click, playerMove
        if st.session_state.t.currentPlayer == backend.Player.Human:
            st.session_state.t.playerMove(row, col)
            st.session_state.t.currentPlayer = backend.Player.AI

    def reset():    
        for key in st.session_state.keys():
            if key != 'Draw' and key != 'AIWin' and key != 'HumanWin':
                del st.session_state[key]
        st.experimental_rerun()


    c = st.empty()
    with c.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            r1c1 = st.button(label=st.session_state.t.symbolMap[st.session_state.t.board[0][0]], key='r1c1', on_click=callback, args=(0, 0))
            r2c1 = st.button(label=st.session_state.t.symbolMap[st.session_state.t.board[1][0]], key='r2c1', on_click=callback, args=(1, 0))
            r3c1 = st.button(label=st.session_state.t.symbolMap[st.session_state.t.board[2][0]], key='r3c1', on_click=callback, args=(2, 0))
        with col2:
            r1c2 = st.button(label=st.session_state.t.symbolMap[st.session_state.t.board[0][1]], key='r1c2', on_click=callback, args=(0, 1))
            r2c2 = st.button(label=st.session_state.t.symbolMap[st.session_state.t.board[1][1]], key='r2c2', on_click=callback, args=(1, 1))
            r3c2 = st.button(label=st.session_state.t.symbolMap[st.session_state.t.board[2][1]], key='r3c2', on_click=callback, args=(2, 1))
        with col3:
            r1c3 = st.button(label=st.session_state.t.symbolMap[st.session_state.t.board[0][2]], key='r1c3', on_click=callback, args=(0, 2))
            r2c3 = st.button(label=st.session_state.t.symbolMap[st.session_state.t.board[1][2]], key='r2c3', on_click=callback, args=(1, 2))
            r3c3 = st.button(label=st.session_state.t.symbolMap[st.session_state.t.board[2][2]], key='r3c3', on_click=callback, args=(2, 2))

        if st.button("Play again!"): reset()


    if st.session_state.result != backend.GameState.Ongoing:
            
            if st.session_state.winner != backend.Player.Blank:
            
                if st.session_state.winner == backend.Player.Human: 
                    st.success('The human wins! Yay!')
                    st.balloons()
                    st.session_state.HumanWin += 1
            
                elif st.session_state.winner == backend.Player.AI: 
                    st.error('The AI wins!')
                    st.balloons()
                    st.session_state.AIWin += 1
            
            else: 
                st.info('A draw. How boring!')
                st.session_state.Draw += 1

    else:
        st.info('Ongoing game. How exciting!')
        if  st.session_state.t.currentPlayer  == backend.Player.AI:
            with st.spinner('AI is finding its best move...'):
                # AI Move and label button accordingly
                st.session_state.t.bestMove()
                st.session_state.t.currentPlayer = backend.Player.Human
                # rerunning the app to trigger checkWinner() process
            st.success("Done!")
            st.experimental_rerun()