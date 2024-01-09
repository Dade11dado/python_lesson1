import functions
import PySimpleGUI as psg
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt','w'):
        pass

label = psg.Text("Type in a todo")
inputBox = psg.InputText(tooltip="Enter todo", key="todo_input")
add_button = psg.Button("Add")
list_box = psg.Listbox(values=functions.getTodos(),
                       key="list_todo",
                       enable_events=True,
                       size=(45, 10))
edit_buttom = psg.Button("Edit")
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")

window = psg.Window("My to-do List",
                    layout=[[label], [inputBox, add_button],
                            [list_box, edit_buttom,complete_button],
                            [exit_button]],
                    font=("Helvetica", 20))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.getTodos()
            new_todo = value["todo_input"] + '\n'
            todos.append(new_todo)
            functions.writeTodos(todos)
            window['list_todo'].update(values=todos)
        case "Edit":
            try:
                todo_selected = value['list_todo'][0]
                new_todo = value['todo_input'] + '\n'
                todos = functions.getTodos()
                index = todos.index(todo_selected)
                todos[index] = new_todo
                functions.writeTodos(todos)
                window['list_todo'].update(values=todos)
            except IndexError:
                psg.popup("Seleziona un elemento prima di modificarlo", font=("Helvetica",20))
        case 'list_todo':
            window['todo_input'].update(value=value['list_todo'][0])
        case "Complete":
            try:
                todo_selected = value['list_todo'][0]
                todos = functions.getTodos()
                todos.remove(todo_selected)
                functions.writeTodos(todos)
                window['list_todo'].update(values=todos)
            except IndexError:
                psg.popup("Seleziona un elemento prima di completarlo",font=("Helvetica",20))
        case 'Exit':
            break
        case psg.WIN_CLOSED:
            break
window.close()
