import streamlit as st

def welcome_person(name):
    return f"Welcome, {name}!"

def main():
    st.title("Welcome App")
    name = st.text_input("Enter your name:")
    if name:
        message = welcome_person(name)
        st.write(message)

if __name__ == "__main__":
    main()
