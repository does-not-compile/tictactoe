"""
Streamlit app: TicTacToe
Author: Sebastian Nagel (github: does-not-compile)
"""

import streamlit as st

# initialize session_state
if 'turn' not in st.session_state: st.session_state.turn = True # switch for x and o turns
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
    if st.session_state['1'] == 'x' and st.session_state['2'] == 'x' and st.session_state['3'] == 'x': st.warning("X WINS!")
    if st.session_state['4'] == 'x' and st.session_state['5'] == 'x' and st.session_state['6'] == 'x': st.warning("X WINS!")
    if st.session_state['7'] == 'x' and st.session_state['8'] == 'x' and st.session_state['9'] == 'x': st.warning("X WINS!")
    if st.session_state['1'] == 'x' and st.session_state['4'] == 'x' and st.session_state['7'] == 'x': st.warning("X WINS!")
    if st.session_state['2'] == 'x' and st.session_state['5'] == 'x' and st.session_state['8'] == 'x': st.warning("X WINS!")
    if st.session_state['3'] == 'x' and st.session_state['6'] == 'x' and st.session_state['9'] == 'x': st.warning("X WINS!")
    if st.session_state['1'] == 'x' and st.session_state['5'] == 'x' and st.session_state['9'] == 'x': st.warning("X WINS!")
    if st.session_state['3'] == 'x' and st.session_state['5'] == 'x' and st.session_state['7'] == 'x': st.warning("X WINS!")

    if st.session_state['1'] == 'o' and st.session_state['2'] == 'o' and st.session_state['3'] == 'o': st.warning("O WINS!")
    if st.session_state['4'] == 'o' and st.session_state['5'] == 'o' and st.session_state['6'] == 'o': st.warning("O WINS!")
    if st.session_state['7'] == 'o' and st.session_state['8'] == 'o' and st.session_state['9'] == 'o': st.warning("O WINS!")
    if st.session_state['1'] == 'o' and st.session_state['4'] == 'o' and st.session_state['7'] == 'o': st.warning("O WINS!")
    if st.session_state['2'] == 'o' and st.session_state['5'] == 'o' and st.session_state['8'] == 'o': st.warning("O WINS!")
    if st.session_state['3'] == 'o' and st.session_state['6'] == 'o' and st.session_state['9'] == 'o': st.warning("O WINS!")
    if st.session_state['1'] == 'o' and st.session_state['5'] == 'o' and st.session_state['9'] == 'o': st.warning("O WINS!")
    if st.session_state['3'] == 'o' and st.session_state['5'] == 'o' and st.session_state['7'] == 'o': st.warning("O WINS!")


st.title("TIC TAC TOE")
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

# st.session_state  # show session states of all variables