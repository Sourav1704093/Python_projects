import streamlit as st

def is_even(number):
    return number%2 == 0

def get_even_letters(msg):
    even_letters = []
    for counter in range(0,len(msg)):
        if is_even(counter):
            even_letters.append(msg[counter])
    return even_letters


def get_odd_letters(msg):
    odd_letters = []
    for counter in range(0,len(msg)):
        if not is_even(counter):
            odd_letters.append(msg[counter])
    return odd_letters

def swap_letters(msg):
    letter_list = []
    if not is_even(len(msg)):
        msg = msg+'x'
    even_letters = get_even_letters(msg)
    odd_letters = get_odd_letters(msg)
    for counter in range(0,int(len(msg)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_msg = ''.join(letter_list)
    return new_msg

st.title("End to End Encryption")
user = st.text_input("Enter your Message")
st.write(swap_letters(user))
