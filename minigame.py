import streamlit as st
import random

st.title('Number Guessing Game')
st.write('I have selected a number between 1 and 100. Can you guess what it is?')

# Generate random number
if 'random_number' not in st.session_state:
    st.session_state['random_number'] = random.randint(1, 100)
if 'guess_count' not in st.session_state:
    st.session_state['guess_count']=1
if 'set_scores' not in st.session_state:
    st.session_state['set_scores']=[]
if 'set_reset_score' not in st.session_state:
    st.session_state['set_reset_score']=3  
# Create a text input for the user's guess
guess = st.text_input('Enter your guess:', '')

# Check the user's guess
if len(st.session_state['set_scores'])<st.session_state['set_reset_score']:
    if guess:
        guess = int(guess)
        if guess < st.session_state['random_number']:
            st.write('Too low!')
        elif guess > st.session_state['random_number']:
            st.write('Too high!')
        else:
            st.write('Congratulations! You guessed correctly!')
            st.session_state['set_scores'].append(f'Set{len(st.session_state["set_scores"])+1}: {st.session_state["guess_count"]}')
            st.session_state['random_number'] = random.randint(1, 100)
            st.session_state['guess_count']=0
        st.write('Guess Count: ',st.session_state['guess_count'])
        st.session_state['guess_count']+=1
        for score in st.session_state['set_scores']:
            st.write(score)
else: 
    st.write('Game Over!! here are yout socres')
    for score in st.session_state['set_scores']:
        st.write(score)
# You can also add a button to reset the game
if st.button('Reset Game'):
    st.session_state['random_number'] = random.randint(1, 100)  # Reset random number
    st.session_state['guess_count'] = 1  # Reset guess count
    st.session_state['set_scores'] = []  # Reset set scores
    st.rerun()  # Rerun the script
