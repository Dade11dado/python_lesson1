import streamlit as st
import functions

st.title("My todo app")
st.subheader("This is my todo app")
st.write("This is for s web developement app")

todos = functions.getTodos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo")
