FILE_NAME = 'todo.txt'

COMMANDS = { "add",
    "list",
    "ls",
    "select"
}

ADD_COMMAND = 'add'

EXIT_COMMAND = 'exit'

SELECT_COMMAND = 'select'

LIST_TASKS_KEYWORDS = {'list', 'ls'}

HELPER_TEXT = (
    "Invalid Command\nUse 'add' to add a task\n"
    "Use 'list' or 'ls' to list tasks\n"
    "Use 'exit' to exit to terminal"
)

SELECT_TEXT = ("Please use the correct format")

SELECT_EXAMPLE = ("e.g. -> select 2")


def main():
    initialise_file()
    while (True):
        user_input = input("Enter your command: ").strip()
        if user_input.lower() == EXIT_COMMAND:
            print("Exiting")
            break
        elif not user_input:
            continue
        else:
            user_input = user_input.split()
            user_command = user_input[0].lower()
            if user_input[0].lower() in COMMANDS:
                if user_command == ADD_COMMAND:
                    task = " ".join(user_input[1:])
                    if (task):
                        create_task(task)
                    else:
                        print("Please add some text for task")
                # if user is asking for ls
                if user_command in LIST_TASKS_KEYWORDS:
                    if (len(user_input) > 1):
                        list_compound_tasks(user_input[1:])
                    else:
                        list_tasks()
                if user_command == SELECT_COMMAND:
                    if len(user_input) > 2:
                        print_select_texts()
                    elif len(user_input) == 2 and not is_number(user_input[1]):
                        print_select_texts()
                    elif len(user_input) == 1:
                        print_select_texts()
                    else:
                        task_number = user_input[1]
                        print(f"task number is {task_number}")
                        select_task(int(task_number))
            else:
                print(HELPER_TEXT)


def select_task(task_number):
    with open(FILE_NAME, 'r') as file:
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
        with open(FILE_NAME, 'r') as file:
            for line in file:
                return_line = True
                for i in inputs:
                    if i not in line:
                        return_line = False
                if(return_line):
                    print(line, end = '')
    else:
        param = inputs[0]
        with open(FILE_NAME, 'r') as file:
            for line in file:
                if param in line:
                    print(line, end = '')


def list_tasks():
    with open(FILE_NAME, 'r') as file:
        content = file.read()
        if(content):
            print(content, end = '')
        else:
            print("There are no tasks in the file")


def create_task(task):
    line_count = 0
    with open(FILE_NAME, 'r') as file:
        for line in file:
            line_count += 1
    line_count += 1
    with open(FILE_NAME, 'a') as file:
        file.write(str(line_count) + ' ' + task + '\n')
        print("Task is created")


def initialise_file():
    try:
        with open(FILE_NAME, 'r') as file:
            content = file.read()
            print("File exists")
    except FileNotFoundError:
        with open(FILE_NAME, 'w') as file:
            print(f"File {FILE_NAME} created")


########################################################################
# Helper functions


def is_number(input_string):
    try:
        float_value = float(input_string)
        return True
    except ValueError:
        return False


def print_select_texts():
    print(SELECT_TEXT)
    print(SELECT_EXAMPLE)

# End helper functions
########################################################################

if __name__ == '__main__':
    main()
