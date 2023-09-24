"""
my implementation for todo.txt
"""
file_name = 'todo.txt'

commands = {
    "add",
    "list",
    "ls",
    "select",
    "complete",
    "edit"
}

add_command = 'add'

exit_command = 'exit'

select_command = 'select'

complete_command = 'complete'

edit_command = 'edit'

list_tasks_keywords = {'list', 'ls'}

helper_text = (
    "Invalid Command\nUse 'add' to add a task\n"
    "Use 'list' or 'ls' to list tasks\n"
    "Use 'exit' to exit to terminal"
)


def main():
    initialise_file()
    while True:
        user_input = input("Enter your command: ").strip()
        if user_input.lower() == exit_command:
            print("Exiting")
            break
        elif not user_input:
            continue
        else:
            user_input = user_input.split()
            user_command = user_input[0].lower()
            if user_input[0].lower() in commands:
                if user_command == add_command:
                    task = " ".join(user_input[1:])
                    if task:
                        create_task(task)
                    else:
                        print("Please add some text for task")
                # if user is asking for ls
                if user_command in list_tasks_keywords:
                    if len(user_input) > 1:
                        list_compound_tasks(user_input[1:])
                    else:
                        list_tasks()
                if user_command == select_command:
                    if len(user_input) > 2:
                        print_select_texts(select_command)
                    elif len(user_input) == 2 and not is_number(user_input[1]):
                        print_select_texts(select_command)
                    elif len(user_input) == 1:
                        print_select_texts(select_command)
                    else:
                        task_number = user_input[1]
                        select_task(int(task_number))
                if user_command == complete_command:
                    if len(user_input) > 2:
                        print_select_texts(complete_command)
                    elif len(user_input) == 2 and not is_number(user_input[1]):
                        print_select_texts(complete_command)
                    elif len(user_input) == 1:
                        print_select_texts(complete_command)
                    else:
                        task_number = user_input[1]
                        edit_task(int(task_number), True)
                if user_command == edit_command:
                    if len(user_input) > 2:
                        print_select_texts(edit_command)
                    elif len(user_input) == 2 and not is_number(user_input[1]):
                        print_select_texts(edit_command)
                    elif len(user_input) == 1:
                        print_select_texts(edit_command)
                    else:
                        task_number = user_input[1]
                        edit_task(int(task_number))
            else:
                print(helper_text)

def edit_task(task_number, complete = False):
    if complete:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if 1 <= task_number <= len(lines):
                print(f"Task - {lines[task_number - 1]}")
                new_text = "X {}".format(lines[task_number - 1]) # FIXME: this could be a f-string
                lines[task_number - 1] = new_text
            else:
                print(f"Task number {task_number} does not exist")
    else:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if 1 <= task_number <= len(lines):
                print(f"Task - {lines[task_number - 1]}")
                new_text = input("Input your changes: ")
                text_to_write = "{} {} \n".format(str(task_number), new_text) # FIXME: this could be a f-string
                lines[task_number - 1] = text_to_write
            else:
                print(f"Task number {task_number} does not exist")
    with open(file_name, 'w') as file:
        file.writelines(lines)



def select_task(task_number):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print(lines)
        if 1 <= task_number <= len(lines):
            for i in lines:
                if i[0] == str(task_number):
                    print(f"selected task is - {i}")
            pass
        else:
            print(f"Task number {task_number} does not exist")


def list_compound_tasks(inputs):
    if len(inputs) > 1:
        with open(file_name, 'r') as file:
            for line in file:
                return_line = True
                for i in inputs:
                    if i not in line:
                        return_line = False
                if return_line:
                    print(line, end = '')
    else:
        param = inputs[0]
        if param == '-a':
            with open(file_name, 'r') as file:
                for line in file:
                    print(line, end = '')
        else:
            with open(file_name, 'r') as file:
                for line in file:
                    if param in line and line[0] != 'X':
                        print(line, end = '')


# TODO: need to impement some code to print something if there are no tasks in the file
def list_tasks():
    with open(file_name, 'r') as file:
        for line in file:
            if line[0] != 'X':
                print(line, end = '')


def create_task(task):
    line_count = 0
    with open(file_name, 'r') as file:
        for line in file:
            line_count += 1
    line_count += 1
    with open(file_name, 'a') as file:
        file.write(str(line_count) + ' ' + task + '\n')
        print("Task is created")


def initialise_file():
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File exists")
    except FileNotFoundError:
        with open(file_name, 'w') as file:
            print(f"File {file_name} created")


########################################################################
# Helper functions


def is_number(input_string):
    try:
        float_value = float(input_string)
        return True
    except ValueError:
        return False


def print_select_texts(action):
    select_text = "Please use the correct format"
    select_example = f"e.g. -> {action} 2"
    print(select_text)
    print(select_example)


# End helper functions
########################################################################

if __name__ == '__main__':
    main()
