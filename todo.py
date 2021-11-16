class Activity:
    def __init__(self, description):
        self.description = description
        self.done = False
    
    def setDone(self):
        self.done = True
    
    def setUndone(self):
        self.done = False

def newTodo(todos):
    description = input('ToDo: ')
    exists = False
    for todo in todos:
        if todo.description == description:
            exists = True
            break
    
    if exists:
        print('This activity is allready in the list')
    else:
        todos.append(Activity(description))
    
def finishTodo(todos):
    index = int(input('Todo Index: '))
    try:
        todos[index-1].setDone()
    except:
        print('That Todo is not in the list')

def undoTodo(todos):
    index = int(input('Todo Index: '))
    try:
        todos[index-1].setUndone()
    except:
        print('That Todo is not in the list')

def isDone(done):
    if done == True:
        return 'Done'
    else:
        return 'Not Done'

def printTodos(todos):
    print('\nToDos:')
    for i in range(len(todos)):
        print(f'#{i+1} - {todos[i].description} - {isDone(todos[i].done)}')
    
    print('')
    
todos = []
#choices = [1,2,3,4]

while True:
    printTodos(todos)
    choice = int(input('1 - New Todo \n2 - Finish Todo \n3 - Unfinish Todo\n4 - Quit\n\nChoice: '))

    if choice == 1:
        newTodo(todos)
    elif choice == 2:
        if todos:
            finishTodo(todos)
        else:
            print('There are no Todos in the list')
    elif choice == 3:
        if todos:
            undoTodo(todos)
        else:
            print('There are no Todos in the list')
    elif choice == 4:
        break
    else:
        print('Invalid choice')


