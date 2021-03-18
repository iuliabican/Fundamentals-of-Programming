"""
This is the user interface module. These functions call functions from the domain and functions module.
"""
# from src.domain.entity import *
from src.functions.functions import *


def print_any_list(gradeList):
    # Prints a suitable list for the problem statement
    print("The list is:")
    i = 0
    for g in gradeList:
        print('i: ' + str(i).ljust(2) + ' p1: ' + str(get_problemGrade(g, 1)).rjust(2) + ', p2: ' +
              str(get_problemGrade(g, 2)).rjust(2) + ', p3: ' + str(get_problemGrade(g, 3)).rjust(2))
        i = i + 1


def read_Params(text):
    """
    For a given instruction, it splits the parameters of the right side of the command
    params: text - the given command
    return: list of parameters
    """
    # if the command were to be 'add   1', then text = '  1  3'
    params = text.split(' ')
    # and here after execution params would be ['','','1','','','3'], so we remove the extra 'empty' spaces in the while
    while '' in params:
        params.remove('')
    return params


def read_Command(text):
    """
    For a given command, it splits the left side from the right side
    params: text - the given command
    return: the command and the parameters separated in a list
    """
    cmd = text.strip().split(' ', 1)
    # cmd[0] = cmd[0].strip().lower()
    return cmd[0], '' if len(cmd) == 1 else read_Params(cmd[1].strip())


# UI functions


def add_ui_function(gradeList, parameters, history):
    if len(parameters) < 3:
        print("Insufficient number of parameters")
        return None
    elif len(parameters) > 3:
        print("Too many parameters")
        return None
    elif add_function(gradeList, parameters, history) is not True:
        print(add_function(gradeList, parameters, history))
        return None
    else:
        print("Added successfully!")


def insert_ui_function(gradeList, parameters, history):
    if len(parameters) < 5:
        print("Insufficient number of parameters")
        return None
    if len(parameters) > 5:
        print("Too many parameters")
        return None
    if parameters[3].lower() != 'at':
        print("Invalid parameters. Syntax should be 'insert <P1 score> <P2 score> <P3 score> at <position>'")
        return None
    if insert_function(gradeList, parameters, history) is not True:
        print(insert_function(gradeList, parameters, history))
        return None
    else:
        print("Inserted successfully!")


def remove_ui_function(gradeList, parameters, history):
    if len(parameters) > 3:
        print('Too many parameters')
        return None
    if len(parameters) == 0:
        print('Insufficient number of parameters')
        return None
    if len(parameters) == 1:  # remove at given position
        if remove_from_position(gradeList, parameters, history) is not True:
            print(remove_from_position(gradeList, parameters, history))
            return None
        else:
            print("Removed successfully!")
    elif len(parameters) == 2:  # remove < | = | > <number>
        if parameters[0] not in ('<', '=', '>'):
            print('Invalid parameters for replace participants')
            return None
        else:
            if remove_participants(gradeList, parameters, history) is not True:
                print(remove_participants(gradeList, parameters, history))
                return None
            else:
                print("Removed successfully!")
    elif len(parameters) == 3:  # remove between given positions
        if parameters[1].lower() != 'to':
            print("Invalid parameters")
            return None
        if remove_between_indexes(gradeList, parameters, history) != 1:
            print(remove_between_indexes(gradeList, parameters, history))
            return None
        elif int(parameters[0] > parameters[-1]):
            print("First index higher than the second one")
            return None
        else:
            print("Removed successfully!")
    else:
        print('invalid nr of parameters')
        return None


def replace_ui_function(gradeList, parameters, history):
    if len(parameters) != 4:
        print('Insufficient number of parameters')
    elif parameters[2] != 'with':
        print('Invalid parameters')
        return None
    elif parameters[1][0] not in ('p', 'P'):
        print('Nonexistent problem')
        return None
    elif replace_function(gradeList, parameters, history) is not True:
        print(replace_function(gradeList, parameters, history))
        return None
    else:
        print("Replaced successfully!")


def show_list_ui_function(gradeList, parameters, history):
    if len(parameters) not in range(0, 4):
        print('Invalid parameters')
        return None

    if len(parameters) == 0:
        a_list = show_list(gradeList, parameters)
        print_any_list(a_list)
    elif len(parameters) == 1:
        if parameters[0] != 'sorted':
            print('invalid parameters')
            return None
        else:
            a_list = show_list_sorted(gradeList, parameters, history)
            print_any_list(a_list)
    elif len(parameters) == 2:
        if parameters[0] not in ['<', '=', '>']:
            print('invalid parameters')
            return None
        else:
            try:
                parameters[1] = int(parameters[1])
                if parameters[1] < 0 or parameters[1] > 10:
                    print('the entered score is not valid')
                    return None
            except Exception as e:
                print(e)
                print('The entered score is not valid')
                return None
            else:
                a_list = show_list_filtered(gradeList, parameters)
                print_any_list(a_list)


def average_ui_function(gradeList, parameters, history):
    if len(parameters) != 3:
        print('Invalid number of parameters')
        return None
    if parameters[1] != 'to':
        print('Invalid parameters')
        return None
    if int(parameters[0]) > int(parameters[2]):
        print('First index higher than the second one')
        return None
    if type(average(gradeList, parameters)) != float:
        print(average(gradeList, parameters))
        return None
    print('The average score is', average(gradeList, parameters))


def minim_ui_function(gradeList, parameters, history):
    if len(parameters) != 3:
        print('Invalid number of parameters')
        return None
    if parameters[1] != 'to':
        print('Invalid parameters')
        return None
    if int(parameters[0]) > int(parameters[2]):
        print('First index higher than the second one')
        return None
    if type(minim(gradeList, parameters)) != tuple:
        print(minim(gradeList, parameters))
        return None
    print('Lowest average score between', parameters[0], 'and', parameters[2], 'is', minim(gradeList, parameters)[0],
          ', participant index:', minim(gradeList, parameters)[1])
    # print(minim(gradeList, parameters))


def undo_ui(gradeList, parameters, history):
    undoDone = undo(gradeList, history)
    if undoDone is True:
        print("Undo took place successfully!")
        print_any_list(gradeList)


def top_ui_function(gradeList, parameters, history):
    if len(parameters) > 2 or len(parameters) == 0:
        print('invalid number of parameters')
        return None
    if len(parameters) == 1:
        if type(top_number(gradeList, parameters)) != list:
            print(top_number(gradeList, parameters))
        else:
            print_any_list(top_number(gradeList, parameters))

    elif len(parameters) == 2:
        if parameters[1][0] not in ('p', 'P'):
            print('Invalid problem')
            return None
        if type(top_problem(gradeList, parameters)) != list:
            print(top_problem(gradeList, parameters))
        else:
            print_any_list(top_problem(gradeList, parameters))
        # print_any_list(top_problem(gradeList, parameters))


# UI related Tests

def test_read_command():
    # tests if read_command() works fine
    new_command = '    replace    1   p3 with 4'
    assert read_Command(new_command) is not None
    command, params = read_Command(new_command)
    assert command == 'replace'
    assert len(params) == 4
    assert params[2] == 'with'
    assert params[1][1] == '3'


def test_all():
    test_non_UI()
    test_read_command()
