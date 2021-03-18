"""
Domain file includes code for entity management
entity = number, transaction, expense etc.
"""


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
