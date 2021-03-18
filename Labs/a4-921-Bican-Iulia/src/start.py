"""
Assemble the program and start the user interface here
"""
from src.ui.console import *


def main():
    contest = []
    history = []
    test_init(contest)

    commands = {'add': add_ui_function, 'insert': insert_ui_function, 'remove': remove_ui_function,
                'replace': replace_ui_function, 'list': show_list_ui_function, 'avg': average_ui_function,
                'min': minim_ui_function, 'top': top_ui_function, 'undo': undo_ui}

    print_any_list(contest)

    while True:
        command = input('Command >> ')
        command = read_Command(command)
        cmd = command[0]
        params = command[1]

        if cmd in commands:
            try:
                commands[cmd](contest, params, history)
            except Exception as ex:
                print(ex)
        elif cmd == 'exit':
            break
        else:
            print("Invalid command")


test_all()
main()
