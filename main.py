from functions import getTodos, writeTodos
import time

while True:
    print(time.strftime("%d - %b - %Y, %H:%M:%S"))
    user_action = input("Type 'add', 'edit', 'complete', 'show' or 'exit': ")
    user_action = user_action.strip()


    if user_action.startswith('add'):
        if(len(user_action)<=4):
            todo = input("Enter the todo: ")
        else:
            todo = user_action[4:]
        todo = todo.title()
        todos = getTodos()
        todos.append(todo+'\n')

        writeTodos(todos)

    elif user_action.startswith('show'):
        todos = getTodos()
        new_todos = [item.strip('\n') for item in todos]
        for index, element in enumerate(new_todos):
            print(f"{index+1}-{element}")

    elif user_action.startswith('edit'):
        try:
            num = int(user_action[5:])
            num = num -1
            todos = getTodos()
            new_todo = input('Enter a new todo: ')
            new_todo = new_todo.title()
            todos[num] = new_todo + "\n"
            writeTodos(todos)
            print("Item updated")
        except ValueError:
            print("Your command wasn't valid, please retry")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(input("Number to complete: "))
            todos = getTodos()
            to_remove = todos[number-1].strip('\n')
            todos.pop(number-1)
            writeTodos(todos)
            print(f"{to_remove} removed from the list")
        except IndexError:
            print("The number you inserted is bigger than the size of the list, retry")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command not found")


print('Bye!')
