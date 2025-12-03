import streamlit as st
import random

st.title("🎯 Guess the Number Game")

# Initialize the secret number once per session
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)

if "message" not in st.session_state:
    st.session_state.message = ""

st.write("I'm thinking of a number between **1 and 100**. Can you guess it?")

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Button to check guess
if st.button("Guess"):
    if guess < st.session_state.secret:
        st.session_state.message = "🔼 Too low! Try a higher number."
    elif guess > st.session_state.secret:
        st.session_state.message = "🔽 Too high! Try a lower number."
    else:
        st.session_state.message = "🎉 Correct! You guessed the number!"
        # Reset game
        st.session_state.secret = random.randint(1, 100)

st.write(st.session_state.message)
