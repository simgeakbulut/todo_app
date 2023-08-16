from functions import get_todos, write_todos
import time

now = time.strftime("%b %d %Y - %H:%M:%S")
print("It is ",now)

while 1:
    user_action = input("Type 'add','show', 'edit', 'complete' or 'exit'")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index +1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:

            number = int(user_action[5:])
            print(number)

            number-=1

            todos = get_todos()

            new_todo= input("New todo:")
            todos[number] = new_todo

            write_todos(todos)

        except ValueError:
            print ('Your command is not valid.')
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            number -= 1
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed"
            print(message)

        except IndexError:
            print ('There is no number with that number')
            continue

    elif user_action.startswith("exit"):
            break

    else:
        print("Invalid")


print("byeee !!!")

#
# # filenames =["1.doc","1.report","1.presentation"]
# # filenames = [filename.replace('.','-') + ".txt" for filename in filenames]
# # print(filenames)
#
