"""
Functions that implement program features. They should call each other, or other functions from the domain
"""
from unittest import TestCase
# import copy
from src.domain.entity import *


# Utilities
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


# Service/Controller functions

def add_function(gradeList, parameters, history):
    """
    Adds grades(results of participants) to the list
    params: gradeList - list of participants
            parameters - the given parameters
            history - list in order to do the reversed operation
    return: True, if the functions works fine
    raises: Exception, otherwise
    """
    try:
        new_grade = create_grades(parameters[0], parameters[1], parameters[2])
    except Exception as exc:
        return exc
    else:
        history.append(gradeList[:])
        gradeList.append(new_grade)
        return True


def insert_function(gradeList, parameters, history):
    """
    Inserts a set of grades for a participant at a given position
    :param parameters: the given parameters
    :param gradeList: list of participants
    :param history: list in order to do the reversed operation
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
            history.append(gradeList[:])
            gradeList.insert(int(position), new_grade)
            return True


def remove_from_position(gradeList, parameters, history):
    """
    Removes the grades of a single participant
    :param gradeList: list of participants
    :param parameters: is an integer in [0, len(gradeList)]
    :param history: list in order to do the reversed operation
    :return: True, if success
    raises: Exception, otherwise
    """
    try:
        is_integer_or_in_range(parameters[-1], 0, len(gradeList) - 1)
    except Exception as ex:
        return ex
    else:
        history.append(gradeList[:])
        set_problemGrade(gradeList[int(parameters[0])], 1, 0)
        set_problemGrade(gradeList[int(parameters[0])], 2, 0)
        set_problemGrade(gradeList[int(parameters[0])], 3, 0)
        return True


def remove_between_indexes(gradeList, parameters, history):
    """
    Removes the grades of successive contestants
    :param gradeList: list of participants
    :param parameters: two integers, start index and stop index
    :param history: list in order to do the reversed operation
    :return: True, if success
    :raises: Exception, otherwise
    """
    try:
        is_integer_or_in_range(parameters[0], 0, len(gradeList) - 1)
        is_integer_or_in_range(parameters[-1], 0, len(gradeList) - 1)
    except Exception as ex:
        return ex
    else:
        history.append(gradeList[:])
        start = int(parameters[0])
        stop = int(parameters[-1])
        for i in range(start, stop + 1):
            gradeList[i] = [0, 0, 0]
        return True


def replace_function(gradeList, parameters, history):
    """
    Replaces the grade of a given participant and problem to another grade
    :param gradeList: list of participants
    :param parameters: an integer for the participant index, a problem number and a set of three integers which are
    the new grades
    :param history: list in order to do the reversed operation
    :return: True, if success
    :raises: Exception, otherwise
    """
    participant = parameters[0]
    problem_nr = parameters[1][1]
    new_grade = parameters[3]
    copy_list = []
    for g in range(len(gradeList)):
        copy_list.append(gradeList[g].copy())
    history.append(copy_list)
    try:
        is_integer_or_in_range(participant, 0, len(gradeList) - 1)
        is_integer_or_in_range(problem_nr, 1, 3)
        is_integer_or_in_range(new_grade, 0, 10)
    except Exception as ex:
        return ex
    else:
        # history.append(gradeList[:])
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


def show_list_sorted(gradeList, parameters, history):
    """
    Returns the grades of all participants, after being sorted in decreasing order
    :param history: list in order to do the reversed operation
    :param gradeList: list of participants
    :param parameters: unused parameter
    :return: gradelist(sorted)
    """
    history.append(gradeList[:])
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


def average(gradeList, parameters):
    """
    Returns the average of the average scores for participants between <startposition> and <stopposition>
    :param gradeList: list of participants
    :param parameters: 2 integers, start position and stop position
    :return: average score, if success, error in contrary
    """

    start = parameters[0]
    stop = parameters[2]
    try:
        is_integer_or_in_range(start, 0, len(gradeList) - 1)
        is_integer_or_in_range(stop, 0, len(gradeList) - 1)
    except Exception as ex:
        return ex
    else:
        start = int(parameters[0])
        stop = int(parameters[2])
        avg_score = 0
        for i in range(start, stop + 1):
            avg_score += grade_average(gradeList[i])
        avg_score = avg_score / (stop - start + 1)
    return round(avg_score, 2)


def minim(gradeList, parameters):
    """
    Returns the lowest average score of participants between two positions
    :param gradeList: list of participants
    :param parameters: 2 integers, start position and stop position
    :return: minimal average score and the participant, if success, error in contrary
    """
    start = parameters[0]
    stop = parameters[2]
    try:
        is_integer_or_in_range(start, 0, len(gradeList) - 1)
        is_integer_or_in_range(stop, 0, len(gradeList) - 1)
    except Exception as ex:
        return ex
    else:
        start = int(parameters[0])
        stop = int(parameters[2])
        min_avg = 111
        participant = -1
        for i in range(start, stop + 1):
            if grade_average(gradeList[i]) < min_avg:
                participant = i
                min_avg = grade_average(gradeList[i])
    return min_avg, participant


def top_number(gradeList, parameters):
    """
    Returns n participants having the highest average score, in descending order of their average score
    :param gradeList: list of participants
    :param parameters: one integer, which is the number of participants we want to print
    :return: list of participants, if success, error in contrary
    """
    index = parameters[-1]
    try:
        is_integer_or_in_range(index, 1, len(gradeList))
    except Exception as ex:
        return ex
    else:
        index = int(parameters[-1])
        copy_list = gradeList.copy()
        copy_list.sort(key=grade_average, reverse=True)
        return copy_list[:index]


def top_problem(gradeList, parameters):
    """
    writes n participants having the highest score for a problem p, in descending order
    :param gradeList: list of participants
    :param parameters: one integer - the number of participants we want to print; problem number
    :return: list of participants if success, error in contrary
    """
    index = parameters[0]
    problem = parameters[-1][1]
    try:
        is_integer_or_in_range(index, 0, len(gradeList))
        is_integer_or_in_range(problem, 0, 11)
    except Exception as ex:
        return ex
    else:
        index = int(index)
        problem = int(problem)
        copy = gradeList.copy()
        copy.sort(key=lambda gradeList: gradeList[problem - 1], reverse=True)
        return copy[:index]


def remove_participants(gradeList, parameters, history):
    """
    Sets the scores of participants having an average score <,=,> n to 0
    :param gradeList: list of participants
    :param parameters: a symbol in (<,>) and a score
    :param history: list in order to do the reversed operation
    :return: True if success, error in contrary
    """
    ok = True
    score = parameters[-1]
    try:
        is_integer_or_in_range(score, 0, 10)
    except Exception as ex:
        ok = False
        return ex
    else:
        score = int(score)
        operator = parameters[0]
        copy_list = gradeList  # .copy()
        # copy.sort(key = grade_average, reverse = True)
        if operator == '<':
            history.append(gradeList[:])
            for i in range(len(copy_list)):
                if grade_average(copy_list[i]) < int(score):
                    copy_list[i] = [0, 0, 0]

        elif operator == '=':
            history.append(gradeList[:])
            for i in range(len(copy_list)):
                if grade_average(copy_list[i]) == score:
                    copy_list[i] = [0, 0, 0]
        elif operator == '>':
            history.append(gradeList[:])
            for i in range(len(copy_list)):
                if grade_average(copy_list[i]) > score:
                    copy_list[i] = [0, 0, 0]
        return ok


def undo(gradeList, history):
    """
    The last operation that has modified program data will be reversed
    :param gradeList: list of contestants
    :param history: list in order to do the reversed operation
    """
    undoDone = True
    if len(history) == 0:
        undoDone = False
        raise ValueError('No more undos!')
    gradeList.clear()
    gradeList.extend(history.pop())
    return undoDone


# Non-UI Test functions

def test_create_grades():
    # tests if create_grades() works fine
    new_grade = create_grades(1, 2, 3)
    assert new_grade is not None and get_problemGrade(new_grade, 2) == 2 and get_problemGrade(new_grade, 3) == 3
    try:
        new_grade = create_grades(-1, 0, 1)
        assert new_grade is None
    except ValueError:
        assert new_grade is not None
    except Exception as e:
        print(e)
        assert new_grade is None


def test_add():
    # Tests if the function add() works fine
    listt = []
    history = []
    new_grade = create_grades(1, 2, 3)
    assert new_grade is not None
    assert add_function(listt, new_grade, history) is True
    assert len(listt) == 1
    assert add_function(listt, (7, 'yyy', 8), history) is not True
    assert len(listt) == 1


def test_insert():
    # Tests if the function insert() works fine
    listt = []
    history = []
    new_grade = create_grades(1, 2, 2)
    assert insert_function(listt, new_grade, history) is not True  # invalid params given
    assert len(listt) == 0
    test_init(listt)
    assert insert_function(listt, (1, 2, 3, 'at', 4), history) is True  # correct input
    assert len(listt) == 11
    assert insert_function(listt, ('at', 'ttt'), history) is not True  # invalid param numbers & format
    assert insert_function(listt, ('insert', 1, 2, 3), history) is not True  # invalid param numbers & format


def test_remove_from_position():
    # Tests if the function remove_from_position() works fine
    listt = []
    history = []
    test_init(listt)
    copy_list = listt
    assert remove_from_position(listt, [11], history) is not True  # out of range position
    assert listt == copy_list
    assert remove_from_position(listt, [6], history) is True  # correct input
    assert listt[6] == [0, 0, 0]


def test_remove_between_indexes():
    # Tests if the function remove_between_indexes() works fine
    listt = []
    history = []
    test_init(listt)
    copy_list = listt
    assert remove_between_indexes(listt, [11, 'to', 12], history) is not True  # out of range positions
    assert listt == copy_list
    assert remove_between_indexes(listt, [6, 'to', 8], history) is True  # correct input
    assert listt[6] == [0, 0, 0]
    assert listt[7] == [0, 0, 0]
    assert listt[8] == [0, 0, 0]


def test_replace_function():
    # Tests if the function replace_function() works fine
    listt = []
    history = []
    test_init(listt)
    copy_list = listt
    assert replace_function(listt, [11, "P1", "with", 6], history) is not True  # out of range position
    assert listt == copy_list
    assert replace_function(listt, [5, "P4", "with", 6], history) is not True  # out of range problem
    assert listt == copy_list
    assert replace_function(listt, [5, "P1", "with", 11], history) is not True  # out of range grade
    assert listt == copy_list
    assert replace_function(listt, [5, "P1", "with", 8], history) is True  # correct input
    assert listt[5][0] == 8


def test_show_list_sorted():
    # Tests if the function show_list_sorted() works fine
    listt = []
    history = []
    test_init(listt)
    sorted_list = show_list_sorted(listt, [], history)  # correct input
    assert sorted_list[0] == [10, 10, 10]
    assert sorted_list[1] == [9, 10, 9]
    assert sorted_list[2] == [8, 9, 10]


def test_show_list_filtered():
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


def test_average():
    # Tests if the function average() works fine
    test_list = []
    test_list.append([0, 0, 0])
    test_list.append([10, 10, 10])
    test_list.append([5, 5, 5])
    average_grade = average(test_list, ['1', 'to', '2'])  # correct input
    assert average_grade == 7.5


def test_minim():
    # Tests if the function minim() works fine
    test_list = []
    test_list.append([0, 0, 0])
    test_list.append([10, 10, 10])
    test_list.append([5, 5, 5])
    minimum_average, position = minim(test_list, ['0', 'to', '2'])  # correct input
    assert minimum_average == 0 and position == 0


def test_top_number():
    # Tests if the function top_number() works fine
    test_list = []
    test_init(test_list)
    top_3_numbers = top_number(test_list, ['3'])  # correct input
    assert top_3_numbers[0] == [10, 10, 10]
    assert top_3_numbers[1] == [9, 10, 9]
    assert top_3_numbers[2] == [8, 9, 10]


def test_top_problem():
    # Tests if the function top_problem() works fine
    test_list = []
    test_init(test_list)
    top_3_P1 = top_problem(test_list, ['3', 'P1'])  # correct input p1
    assert top_3_P1[0] == [10, 10, 10]
    assert top_3_P1[1] == [9, 2, 5]
    assert top_3_P1[2] == [9, 10, 9]
    top_3_P2 = top_problem(test_list, ['3', 'P2'])  # correct input p2
    assert top_3_P2[0] == [10, 10, 10]
    assert top_3_P2[1] == [9, 10, 9]
    assert top_3_P2[2] == [8, 9, 10]
    top_3_P3 = top_problem(test_list, ['3', 'P3'])  # correct input p3
    assert top_3_P3[0] == [10, 10, 10]
    assert top_3_P3[1] == [8, 9, 10]
    assert top_3_P3[2] == [9, 10, 9]


def test_remove_participants():
    # Tests if the function show_list_filtered() works fine
    test_list = []
    history = []
    test_init(test_list)
    removed_list = remove_participants(test_list, ['=', 7], history)  # correct input
    assert removed_list is True
    test_list = []
    history = []
    test_init(test_list)
    removed_list = remove_participants(test_list, ['<', 2], history)  # correct input
    assert removed_list is True
    test_list = []
    history = []
    test_init(test_list)
    removed_list = remove_participants(test_list, ['>', 9], history)  # correct input
    assert removed_list is True
    # try:
    #     remove_participants(test_list, ['ast', 9], history)  # incorrect parameter but it's validated in ui
    #     assert False
    # except Exception:
    #     assert True


def test_undo():
    test_list = []
    history = []
    test_init(test_list)
    remove_participants(test_list, ['<', 3], history)
    assert test_list[2] == [0, 0, 0] and test_list[5] == [0, 0, 0]  # 2,1,4 & 2,2,2
    undo(test_list, history)
    assert test_list[2] == [2, 1, 4] and test_list[5] == [2, 2, 2]


def test_non_UI():
    test_create_grades()
    test_add()
    test_insert()
    test_remove_from_position()
    test_remove_between_indexes()
    test_replace_function()
    test_show_list_sorted()
    test_show_list_filtered()
    test_average()
    test_minim()
    test_top_number()
    test_top_problem()
    test_remove_participants()
    test_undo()
