"""
Streamlit app for Website: TicTacToe
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
if 't' not in st.session_state: st.session_state.t = backend.TicTacToe()
if 'turn' not in st.session_state: st.session_state.turn = st.session_state.t.turn.name # who's turn?
if 'AIWin' not in st.session_state: st.session_state.AIWin = 0
if 'HumanWin' not in st.session_state: st.session_state.HumanWin = 0

def callback(x, y):
    st.session_state.t.move(x, y)
def reset():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()

c = st.empty()
with c.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        r1c1 = st.button(label=st.session_state.t.board[0][0].name, key='r1c1', on_click=callback, args=(0, 0))
        r2c1 = st.button(label=st.session_state.t.board[1][0].name, key='r2c1', on_click=callback, args=(1, 0))
        r3c1 = st.button(label=st.session_state.t.board[2][0].name, key='r3c1', on_click=callback, args=(2, 0))
    with col2:
        r1c2 = st.button(label=st.session_state.t.board[0][1].name, key='r1c2', on_click=callback, args=(0, 1))
        r2c2 = st.button(label=st.session_state.t.board[1][1].name, key='r2c2', on_click=callback, args=(1, 1))
        r3c2 = st.button(label=st.session_state.t.board[2][1].name, key='r3c2', on_click=callback, args=(2, 1))
    with col3:
        r1c3 = st.button(label=st.session_state.t.board[0][2].name, key='r1c3', on_click=callback, args=(0, 2))
        r2c3 = st.button(label=st.session_state.t.board[1][2].name, key='r2c3', on_click=callback, args=(1, 2))
        r3c3 = st.button(label=st.session_state.t.board[2][2].name, key='r3c3', on_click=callback, args=(2, 2))
    
    winner = st.session_state.t.winner
    if st.session_state.t.state != backend.GameState.Ongoing:
        if winner !=  backend.Player.Blank:
            if winner == backend.Player.Human: 
                st.success('The human wins! Yay!')
                st.balloons()
            elif winner == backend.Player.AI: 
                st.error('Welp. AI wins!')
                st.balloons()
        else: st.info('A draw. How boring!')
    else: st.info('Ongoing game. How exciting!')
    if st.button("Play again!"): reset()