import random
import streamlit as st

st.title("Welcome to the Guessing Game!")
st.write("Guess a number between 1 and 20!")

# Store the random number in session state
if "num" not in st.session_state:
    st.session_state.num = random.randint(1, 20)

guess = st.number_input("Insert a number between 1 and 20", min_value=1, max_value=20, step=1)

# Guess check button
if st.button("Check Guess"):
    if guess == st.session_state.num:
        st.success("Congratulations, You guessed it right!")
    elif guess < st.session_state.num:
        st.warning("Too low, try again!")
    else:
        st.warning("Too high, try again!")

# Reset game button
if st.button("Reset Game"):
    st.session_state.num = random.randint(1, 20)
    st.info("Game reset! Try guessing the new number.")
