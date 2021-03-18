#
# Write the implementation for A3 in this file
#

#
# domain section is here (domain = numbers, transactions, expenses, etc.)
# getters / setters
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)

# Setter for the grade of a given problem
def get_problemGrade(gradeList, p):
    return gradeList[p - 1]


# Setter for the grade of a given problem
def set_problemGrade(gradeList, p, grade):
    gradeList[p - 1] = grade


def create_grades(p1, p2, p3):
    """
    Creates a participant with p1,p2,p3 scores
    params: p1, p2, p3 - grades for every problem
    return: returns a list of grades for a single participant
    """
    try:
        p1 = int(p1)
        p2 = int(p2)
        p3 = int(p3)
    except ValueError:
        raise TypeError("Scores are not integers")
    if not (0 <= p1 <= 10) or not (0 <= p2 <= 10) or not (0 <= p3 <= 10):
        raise ValueError("Scores not in [0,10]")
    else:
        return [p1, p2, p3]


def grade_average(grades):
    """
    Calculates and returns the average score of a participant
    params: grades - the list of the participant's grades
    return: avg - the average if it's within bounds
            None - otherwise
    """
    avg = round((grades[0] + grades[1] + grades[2]) / 3, 1)
    if 10 >= avg >= 0:
        return avg
    else:
        return None


def is_integer_or_in_range(parameter, start, stop):
    """
    Checks if the parameter is an integer or is within the range [start, stop]
    params: parameter - the possible number(integer)
            start, stop -  the range in which the parameter should be located
    return: True if the given parameter is an integer within the given range
    raises: TypeError - if param not integer
            ValueError - if index out of range
    """
    try:
        parameter = int(parameter)
    except ValueError:
        raise TypeError("Parameter not integer")
    else:
        if int(parameter) < start or int(parameter) > stop:
            raise ValueError("Index out of range")
        else:
            return True


def add_function(gradeList, parameters):
    """
    Adds grades(results of participants) to the list
    params: gradeList - list of participants
            parameters - the given parameters
    return: True, if the functions works fine
    raises: Exception, otherwise
    """
    try:
        new_grade = create_grades(parameters[0], parameters[1], parameters[2])
    except Exception as exc:
        return exc
    else:
        gradeList.append(new_grade)
        return True


def insert_function(gradeList, parameters):
    """
    Inserts a set of grades for a participant at a given position
    params: gradeList - list of participants, params: the given parameters
    return: True, if the functions works
    raises: Exception, otherwise
    """
    try:
        new_grade = create_grades(parameters[0], parameters[1], parameters[2])
    except Exception as ex:
        return ex
    else:
        position = parameters[-1]
        try:
            is_integer_or_in_range(position, 0, len(gradeList))
        except Exception as ex:
            return ex
        else:
            gradeList.insert(int(position), new_grade)
            return True


def remove_from_position(gradeList, parameters):
    """
    Removes the grades of a single participant
    :param gradeList: list of participants
    :param parameters: is an integer in [0, len(gradeList)]
    :return: True, if success
    raises: Exception, otherwise
    """
    try:
        is_integer_or_in_range(parameters[-1], 0, len(gradeList) - 1)
    except Exception as ex:
        return ex
    else:
        set_problemGrade(gradeList[int(parameters[0])], 1, 0)
        set_problemGrade(gradeList[int(parameters[0])], 2, 0)
        set_problemGrade(gradeList[int(parameters[0])], 3, 0)
        return True


def remove_between_indexes(gradeList, parameters):
    """
    Removes the grades of successive contestants
    :param gradeList: list of participants
    :param parameters: two integers, start index and stop index
    :return: True, if success
    :raises: Exception, otherwise
    """
    try:
        is_integer_or_in_range(parameters[0], 0, len(gradeList) - 1)
        is_integer_or_in_range(parameters[-1], 0, len(gradeList) - 1)
    except Exception as ex:
        return ex
    else:
        start = int(parameters[0])
        stop = int(parameters[-1])
        for i in range(start, stop + 1):
            gradeList[i] = [0, 0, 0]
        return True


def replace_function(gradeList, parameters):
    """
    Replaces the grade of a given participant and problem to another grade
    :param gradeList: list of participants
    :param parameters: an integer for the participant index, a problem number and a set of three integers which are
    the new grades
    :return: True, if success
    :raises: Exception, otherwise
    """
    participant = parameters[0]
    problem_nr = parameters[1][1]
    new_grade = parameters[3]
    try:
        is_integer_or_in_range(participant, 0, len(gradeList) - 1)
        is_integer_or_in_range(problem_nr, 1, 3)
        is_integer_or_in_range(new_grade, 0, 10)
    except Exception as ex:
        return ex
    else:
        set_problemGrade(gradeList[int(participant)], int(problem_nr), int(new_grade))
        # gradeList[int(participant)][int(problem_nr) - 1] = int(new_grade)
        return True


def show_list(gradeList, parameters):
    """
    Returns the grades of all participants
    :param gradeList: list of participants
    :param parameters: unused parameter
    :return: gradelist
    """
    return gradeList


def show_list_sorted(gradeList, parameters):
    """
    Returns the grades of all participants, after being sorted in decreasing order
    :param gradeList: list of participants
    :param parameters: unused parameter
    :return: gradelist(sorted)
    """
    copy_list = sorted(gradeList, key=grade_average, reverse=True)
    return copy_list


def show_list_filtered(gradeList, parameters):
    """
    Returns the grades of the participants which obey a given rule (filters all participants by a condition)
    :param gradeList: list of participants
    :param parameters: parameters which contain the restraint after which we filter
    :return: new_list - the filtered list
    """
    new_list = []
    operator = parameters[0]
    given_score = int(parameters[1])
    for g in gradeList:
        if operator == '<' and grade_average(g) < given_score and grade_average(g) is not None:
            new_list.append(g)
        elif operator == '=' and grade_average(g) == given_score and grade_average(g) is not None:
            new_list.append(g)
        elif operator == '>' and grade_average(g) > given_score and grade_average(g) is not None:
            new_list.append(g)
    return new_list


# Functionalities section (functions that implement required features)
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)
# Each function does one thing only
# Functions communicate using input parameters and their return values


# UI section
# (all functions that have input or print statements, or that CALL functions with print / input are  here).
# Ideally, this section should not contain any calculations relevant to program functionalities

def print_any_list(gradeList):
    # Prints a suitable list for the problem statement
    print("The list is:")
    for g in gradeList:
        print('p1: ' + str(get_problemGrade(g, 1)).rjust(2) + ', p2: ' + str(get_problemGrade(g, 2)).rjust(2) + ', p3: '
              + str(get_problemGrade(g, 3)).rjust(2))


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


def add_ui_function(gradeList, parameters):
    if len(parameters) < 3:
        print("Insufficient number of parameters")
        return None
    elif len(parameters) > 3:
        print("Too many parameters")
        return None
    elif add_function(gradeList, parameters) is not True:
        print(add_function(gradeList, parameters))
        return None
    else:
        print("Added successfully!")


def insert_ui_function(gradeList, parameters):
    if len(parameters) < 5:
        print("Insufficient number of parameters")
        return None
    if len(parameters) > 5:
        print("Too many parameters")
        return None
    if parameters[3].lower() != 'at':
        print("Invalid parameters. Syntax should be 'insert <P1 score> <P2 score> <P3 score> at <position>'")
        return None
    if insert_function(gradeList, parameters) is not True:
        print(insert_function(gradeList, parameters))
        return None
    else:
        print("Inserted successfully!")


def remove_ui_function(gradeList, parameters):
    if len(parameters) > 3:
        print('Too many parameters')
        return None
    if len(parameters) == 0:
        print('Insufficient number of parameters')
        return None
    if len(parameters) == 1:  # remove at given position
        if remove_from_position(gradeList, parameters) is not True:
            print(remove_from_position(gradeList, parameters))
            return None
    elif len(parameters) == 3:  # remove between given positions
        if parameters[1].lower() != 'to':
            print("Invalid parameters")
            return None
        if remove_between_indexes(gradeList, parameters) != 1:
            print(remove_between_indexes(gradeList, parameters))
            return None
        elif int(parameters[0] > parameters[-1]):
            print("First index higher than the second one")
            return None
    else:
        print('invalid nr of parameters')
        return None


def replace_ui_function(gradeList, parameters):
    if len(parameters) != 4:
        print('Insufficient number of parameters')
    elif parameters[2] != 'with':
        print('Invalid parameters')
        return None
    elif parameters[1][0] not in ('p', 'P'):
        print('Inexistent problem')
        return None
    elif replace_function(gradeList, parameters) is not True:
        print(replace_function(gradeList, parameters))
        return None


def show_list_ui_function(gradeList, parameters):
    if len(parameters) not in range(0, 4):
        print('invalid parameters')
        return None

    if len(parameters) == 0:
        listt = show_list(gradeList, parameters)
        print_any_list(listt)
    elif len(parameters) == 1:
        if parameters[0] != 'sorted':
            print('invalid parameters')
            return None
        else:
            listt = show_list_sorted(gradeList, parameters)
            print_any_list(listt)
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
            except:
                print('the entered score is not valid')
                return None
            else:
                listt = show_list_filtered(gradeList, parameters)
                print_any_list(listt)


def main():
    contest = []
    test_init(contest)

    commands = {'add': add_ui_function, 'insert': insert_ui_function, 'remove': remove_ui_function,
                'replace': replace_ui_function, 'list': show_list_ui_function}

    print_any_list(contest)

    while True:
        command = input('Command >> ')
        command = read_Command(command)
        cmd = command[0]
        params = command[1]

        if cmd in commands:
            try:
                commands[cmd](contest, params)
            except Exception as ex:
                print(ex)
        elif cmd == 'exit':
            break
        else:
            print("Invalid command")


# Test functions go here
#
# Test functions:
#   - no print / input
#   - great friends with assert

def test_create_grades():
    # tests if create_grades() works fine
    new_grade = create_grades(1, 2, 3)
    assert new_grade is not None and get_problemGrade(new_grade, 2) == 2 and get_problemGrade(new_grade, 3) == 3
    try:
        new_grade = create_grades(-1, 0, 1)
        assert new_grade is None
    except ValueError:
        assert new_grade is not None
    except Exception:
        assert new_grade is None


def test_read_command():
    # tests if read_command() works fine
    new_command = '    replace    1   p3 with 4'
    assert read_Command(new_command) is not None
    command, params = read_Command(new_command)
    assert command == 'replace'
    assert len(params) == 4
    assert params[2] == 'with'
    assert params[1][1] == '3'


def test_add():
    # Tests if the function add() works fine
    listt = []
    new_grade = create_grades(1, 2, 3)
    assert new_grade is not None
    assert add_function(listt, new_grade) is True
    assert len(listt) == 1
    assert add_function(listt, (7, 'yyy', 8)) is not True
    assert len(listt) == 1


def test_insert():
    # Tests if the function insert() works fine
    listt = []
    new_grade = create_grades(1, 2, 2)
    assert insert_function(listt, new_grade) is not True  # invalid params given
    assert len(listt) == 0
    test_init(listt)
    assert insert_function(listt, (1, 2, 3, 'at', 4)) is True  # correct input
    assert len(listt) == 11
    assert insert_function(listt, ('at', 'ttt')) is not True  # invalid param numbers & format
    assert insert_function(listt, ('insert', 1, 2, 3)) is not True  # invalid param numbers & format


def test_remove_from_position():
    # Tests if the function remove_from_position() works fine
    listt = []
    test_init(listt)
    copy_list = listt
    assert remove_from_position(listt, [11]) is not True  # out of range position
    assert listt == copy_list
    assert remove_from_position(listt, [6]) is True  # correct input
    assert listt[6] == [0, 0, 0]


def test_remove_between_indexes():
    # Tests if the function remove_between_indexes() works fine
    listt = []
    test_init(listt)
    copy_list = listt
    assert remove_between_indexes(listt, [11, 'to', 12]) is not True  # out of range positions
    assert listt == copy_list
    assert remove_between_indexes(listt, [6, 'to', 8]) is True  # correct input
    assert listt[6] == [0, 0, 0]
    assert listt[7] == [0, 0, 0]
    assert listt[8] == [0, 0, 0]


def test_replace_function():
    # Tests if the function replace_function() works fine
    listt = []
    test_init(listt)
    copy_list = listt
    assert replace_function(listt, [11, "P1", "with", 6]) is not True  # out of range position
    assert listt == copy_list
    assert replace_function(listt, [5, "P4", "with", 6]) is not True  # out of range problem
    assert listt == copy_list
    assert replace_function(listt, [5, "P1", "with", 11]) is not True  # out of range grade
    assert listt == copy_list
    assert replace_function(listt, [5, "P1", "with", 8]) is True  # correct input
    assert listt[5][0] == 8


def test_show_list_sorted():
    # Tests if the function show_list_sorted() works fine
    listt = []
    test_init(listt)
    sorted_list = show_list_sorted(listt, [])  # correct input
    assert sorted_list[0] == [10, 10, 10]
    assert sorted_list[1] == [9, 10, 9]
    assert sorted_list[2] == [8, 9, 10]


def test_show_list_fitered():
    # Tests if the function show_list_filtered() works fine
    listt = []
    test_init(listt)
    filtered_list = show_list_filtered(listt, ['=', 7])  # correct input
    assert len(filtered_list) == 2  # (6,7,8) & (8,8,5)
    filtered_list = show_list_filtered(listt, ['<', 2])  # correct input
    assert len(filtered_list) == 1  # (0,0,0)
    filtered_list = show_list_filtered(listt, ['>', 9])  # correct input
    assert len(filtered_list) == 2  # (10,10,10) & (9,10,9)
    filtered_list = show_list_filtered(listt, ['sdfg', 9])  # incorrect operator
    assert len(filtered_list) == 0
    filtered_list = show_list_filtered(listt, ['=', 11])  # out of range comparison done
    assert len(filtered_list) == 0


def test_init(test_list):
    # use this function to add the 10 required items
    # use it to set up test data
    test_list.append([0, 0, 0])
    test_list.append([10, 10, 10])
    test_list.append([2, 1, 4])
    test_list.append([6, 7, 8])
    test_list.append([8, 9, 10])
    test_list.append([2, 2, 2])
    test_list.append([8, 4, 1])
    test_list.append([9, 2, 5])
    test_list.append([8, 8, 5])
    test_list.append([9, 10, 9])


test_create_grades()
test_read_command()
test_add()
test_insert()
test_remove_from_position()
test_remove_between_indexes()
test_replace_function()
test_show_list_sorted()
test_show_list_fitered()
main()
