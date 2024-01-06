def getTodos():
    """Get all the items from the file 'todos.txt'"""
    with open('todos.txt','r') as file:
        todos = file.readlines()
    return todos

def writeTodos(todos):
    """write the argument passed in the parameters to the file"""
    with open('todos.txt','w') as file:
        file.writelines(todos)

