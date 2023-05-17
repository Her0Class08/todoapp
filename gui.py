import functions
import PySimpleGUI as PSG

label = PSG.Text("Time in a to-do")
input_box = PSG.InputText(tooltip="enter todo")
add_button = PSG.Button("Add")

window = PSG.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
print("hellO")
window.close()