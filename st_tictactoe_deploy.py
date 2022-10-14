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
if 'turn' not in st.session_state: st.session_state.turn = True # switch for x and o turns
if 'x_wins' not in st.session_state: st.session_state.x_wins = 0 # count x wins
if 'o_wins' not in st.session_state: st.session_state.o_wins = 0 # count o wins
if 'draws' not in st.session_state: st.session_state.draws = 0 # count draws
if 'gameover' not in st.session_state: st.session_state.gameover = False
if 'message' not in st.session_state: st.session_state.message = ""
for i in range(1, 10):
    if str(i) not in st.session_state: st.session_state[str(i)] = '.'   # populate session_state for button labels
    if (str(i)+"state") not in st.session_state: st.session_state[str(i)+"state"] = False   # populate session_state for button states

# change button labels when clicked
def callback(idx):
    """ function checks who's turn it is and replaces the button label accordingly and disables the button """
    if st.session_state.turn:
            st.session_state[idx] = 'x'
            st.session_state[idx+"state"] = True
            st.session_state.turn = False
    else:
        st.session_state[idx] = 'o'
        st.session_state[idx+"state"] = True
        st.session_state.turn = True
    
    checkwin()  # check if winning combination has been achieved by either player

def checkwin():
    """ checks if one player reached a winning combination of buttons! """
    if st.session_state['1'] == 'x' and st.session_state['2'] == 'x' and st.session_state['3'] == 'x' or \
    st.session_state['4'] == 'x' and st.session_state['5'] == 'x' and st.session_state['6'] == 'x' or \
    st.session_state['7'] == 'x' and st.session_state['8'] == 'x' and st.session_state['9'] == 'x' or \
    st.session_state['1'] == 'x' and st.session_state['4'] == 'x' and st.session_state['7'] == 'x' or \
    st.session_state['2'] == 'x' and st.session_state['5'] == 'x' and st.session_state['8'] == 'x' or \
    st.session_state['3'] == 'x' and st.session_state['6'] == 'x' and st.session_state['9'] == 'x' or \
    st.session_state['1'] == 'x' and st.session_state['5'] == 'x' and st.session_state['9'] == 'x' or \
    st.session_state['3'] == 'x' and st.session_state['5'] == 'x' and st.session_state['7'] == 'x': 
        for i in range(1, 10):
            st.session_state[str(i)+'state'] = True
        st.session_state.x_wins += 1
        st.session_state.gameover = True
        if st.session_state.x_wins > 1: st.session_state.message = f"X wins and has {st.session_state.x_wins} wins so far!"
        else: st.session_state.message = f"X wins and has {st.session_state.x_wins} win so far!"

    if st.session_state['1'] == 'o' and st.session_state['2'] == 'o' and st.session_state['3'] == 'o' or \
    st.session_state['4'] == 'o' and st.session_state['5'] == 'o' and st.session_state['6'] == 'o' or \
    st.session_state['7'] == 'o' and st.session_state['8'] == 'o' and st.session_state['9'] == 'o' or \
    st.session_state['1'] == 'o' and st.session_state['4'] == 'o' and st.session_state['7'] == 'o' or \
    st.session_state['2'] == 'o' and st.session_state['5'] == 'o' and st.session_state['8'] == 'o' or \
    st.session_state['3'] == 'o' and st.session_state['6'] == 'o' and st.session_state['9'] == 'o' or \
    st.session_state['1'] == 'o' and st.session_state['5'] == 'o' and st.session_state['9'] == 'o' or \
    st.session_state['3'] == 'o' and st.session_state['5'] == 'o' and st.session_state['7'] == 'o': 
        for i in range(1, 10):
            st.session_state[str(i)+'state'] = True
        st.session_state.o_wins += 1
        st.session_state.gameover = True
        if st.session_state.o_wins > 1: st.session_state.message = f"O wins and has {st.session_state.o_wins} wins so far!"
        else: st.session_state.message = f"O wins and has {st.session_state.o_wins} win so far!"
    # draw?
    # if all buttons have been pressed --> session_state[str(i)+state] are all True
    # but no winner --> gameover == False
    n = 0
    for i in range(1, 10):
        if st.session_state[str(i)+'state'] == True: n += 1
    if n == 9 and st.session_state.gameover == False:
        st.session_state.gameover = True
        st.session_state.draws += 1
        if st.session_state.draws > 1: st.session_state.message = f"Draw! Nobody wins. There have been {st.session_state.draws} draws so far."
        else: st.session_state.message = f"Draw! Nobody wins. There has been {st.session_state.draws} draw so far."

def reset():
    for i in range(1, 10):
        st.session_state[str(i)+'state'] = False
        st.session_state[str(i)] = '.'
    
    st.session_state.turn = True
    st.session_state.gameover = False
    st.session_state.message = ""

    st.experimental_rerun()

c = st.empty()

with c.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button(label=st.session_state['1'], key='a', disabled=st.session_state['1state'], on_click=callback, args=('1', ))
        st.button(label=st.session_state['2'], key='b', disabled=st.session_state['2state'], on_click=callback, args=('2', ))
        st.button(label=st.session_state['3'], key='c', disabled=st.session_state['3state'], on_click=callback, args=('3', ))
    with col2:
        st.button(label=st.session_state['4'], key='d', disabled=st.session_state['4state'], on_click=callback, args=('4', ))
        st.button(label=st.session_state['5'], key='e', disabled=st.session_state['5state'], on_click=callback, args=('5', ))
        st.button(label=st.session_state['6'], key='f', disabled=st.session_state['6state'], on_click=callback, args=('6', ))
    with col3:
        st.button(label=st.session_state['7'], key='g', disabled=st.session_state['7state'], on_click=callback, args=('7', ))
        st.button(label=st.session_state['8'], key='h', disabled=st.session_state['8state'], on_click=callback, args=('8', ))
        st.button(label=st.session_state['9'], key='i', disabled=st.session_state['9state'], on_click=callback, args=('9', ))
    
    st.text(st.session_state.message)

    if st.button("Play again!"): reset()
