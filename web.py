import streamlit as st
import functions

todos = functions.getTodos()

def add_todo():
    todo = st.session_state["new_todo"] +'\n'
    todos.append(todo)
    functions.writeTodos(todos)
    st.session_state["new_todo"] = ""




st.title("My todo app")
st.subheader("This is my todo app")
st.write("This is for s web developement app")



for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo",
              on_change=add_todo,
              key="new_todo")
