import functions
import PySimpleGUI as psg

label = psg.Text("Type in a todo")
inputBox = psg.InputText(tooltip="Enter todo")
add_button = psg.Button("Add")

window = psg.Window("My to-do List", layout=[[label], [inputBox,add_button]])
window.read()
window.close()
