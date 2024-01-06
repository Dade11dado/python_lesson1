import functions
import PySimpleGUI as psg

label = psg.Text("Type in a todo")
inputBox = psg.InputText(tooltip="Enter todo",key="todo")
add_button = psg.Button("Add")

window = psg.Window("My to-do List",
                    layout=[[label], [inputBox, add_button]],
                    font=("Helvetica", 20))
while True:
    event,value = window.read()
    match event:
        case "Add":
            todos = functions.getTodos()
            new_todo = value["todo"] + '\n'
            todos.append(new_todo)
            functions.writeTodos(todos)
        case psg.WIN_CLOSED:
            break
window.close()
