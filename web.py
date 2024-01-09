import streamlit as st
import functions

todos = functions.getTodos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.writeTodos(todos)
    st.session_state["new_todo"] = ""


st.title("My todo app")
st.subheader("This is my todo app")
st.write("This is for s web developement app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.writeTodos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter todo", placeholder="Add new todo",
              on_change=add_todo,
              key="new_todo")
