#
# Write the implementation for A2 in this file
#
import math


# UI section
# (write all functions that have input or print statements here). 
# Ideally, this section should not contain any calculations relevant to program functionalities

def print_menu():
    print("1. Read numbers")
    print("2. Show numbers")
    print("3. Show longest sequence which contains at most 3 distinct values (functionality 2)")
    print("4. Show longest sequence where the modulus of all elements is in the [0, 10] range (functionality 8)")
    print("5. Exit")


def show_numbers(data):
    print("List of numbers")
    for s in data:
        print("Real part is: " + str(get_number_real_part(s)) + ", Imaginary part is: " + str(get_number_img_part(s)))


def read_number():
    # this function reads and checks if the imputed text is valid,
    # creates a complex number if it is, and displays an error message if it's not
    stringNumber = input("Enter number in form a +/- bi (for fractional numbers use x.x not x,x) >> z = ")
    params = stringNumber.split(' ')  # params should contain [rpart] [+/-] [ipart'i']
    realPart = params[0]
    imagPart = params[2][:-1]
    if len(params) != 3 or (len(params) == 3 and (params[1] != '+' and params[1] != '-') or params[2][-1] != 'i'):
        raise Exception("Wrong format! You should write the complex number as a +/- bi !")
    elif validate_number(realPart) is True and validate_number(imagPart) is True:
        if params[1] == '-':
            return create_number(float(realPart), -float(imagPart))
        else:
            return create_number(float(realPart), float(imagPart))
    else:
        raise Exception("The real part or the imaginary part is not a number, but a string!")


def add_number(numbers):
    # this function adds a complex number to the list of numbers
    n = int(input("Give the number of complex numbers you want to add to the list: "))
    for i in range(n):
        try:
            s = read_number()
            numbers.append(s)
        except Exception as e:
            print(e)


def print_sequence(beginning, stop, numbers):
    """
    This function prints out the sequence between two given indexes
    input: beginning-first index
           stop-second index
           numbers-list of complex numbers
    """
    print("The searched for sequence with length of " + str(stop - beginning) + " is: ")
    for i in range(beginning, stop):
        if get_number_img_part(numbers[i]) >= 0:
            print(str(get_number_real_part(numbers[i])) + "+" + str(get_number_img_part(numbers[i])) + "i")
        else:
            print(str(get_number_real_part(numbers[i])) + "-" + str(get_number_img_part(numbers[i]) * -1) + "i")


def longest_sequence_modulus_between_0_10_ui(numbers):
    start_max, stop_max = longest_sequence_modulus_between_0_10(numbers)
    print_sequence(start_max, stop_max + 1, numbers)


def longest_sequence_3_distinct_ui(numbers):
    start_max, stop_max = longest_sequence_3_distinct(numbers)
    print_sequence(start_max, stop_max + 1, numbers)


# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

# Setters and Getters

def set_number_real_part(number, realPart):
    """
    Sets the number's real part
    params:
        number - the number
        realPart - the real part of that number
    """
    number[0] = realPart


def get_number_real_part(number):
    return number[0]


def set_number_img_part(number, imagPart):
    """
    Sets the number's imaginary part
    params:
        number - the number
        imagPart - the imaginary part of that number
    """
    number[1] = imagPart


def get_number_img_part(number):
    return number[1]


def toString(number):
    numberToString = str(get_number_real_part(number))
    if get_number_img_part(number) < 0:
        numberToString = numberToString + "-" + str(get_number_img_part(number) * (-1)) + 'i'
    else:
        numberToString = numberToString + "+" + str(get_number_img_part(number)) + 'i'
    return numberToString


def validate_number(x):  # validation
    # The function returns -> True - number ok
    #                         False - not ok (ex - string)
    try:
        float(x)
        return True
    except ValueError:
        return False


def create_number(realPart, imagPart):
    # function that creates a complex number using setters for the imaginary and real parts
    number = [0, 0]
    set_number_real_part(number, realPart)
    set_number_img_part(number, imagPart)
    return number


def init_number_list():  # function that initializes the number list
    numbers = [create_number(4, -2), create_number(-6, 1), create_number(5, 5), create_number(5, -3),
               create_number(6, 2), create_number(5, -3), create_number(5, -3), create_number(9, -5),
               create_number(5, 1), create_number(5, 0)]
    return numbers


# Here beginning the 'utilities' functions
def module_calc(x):
    # This function calculates the modulus of a complex number
    return math.sqrt(get_number_real_part(x) ** 2 + get_number_img_part(x) ** 2)


def longest_sequence_3_distinct(numbers):
    """
    This function returns the first and last positions of the longest sequence which contains at most 3 distinct values
    input: numbers - the list of complex numbers
    output: beginning - the starting position of the longest required sequence
            end       - the stopping position of the longest required sequence
    """
    frequencyDictionary = {}
    beginning = 0
    end = 0
    counter_distinct = 0
    index = 0
    for i in range(len(numbers)):
        # Mark the number as visited (with frequency = 1)
        if toString(numbers[i]) not in frequencyDictionary:
            frequencyDictionary[toString(numbers[i])] = 1
        else:
            frequencyDictionary[toString(numbers[i])] = frequencyDictionary[toString(numbers[i])] + 1

        # If it's visited for the first time, then increase the counter of distinct elements by 1
        if frequencyDictionary[toString(numbers[i])] == 1:
            counter_distinct += 1

        # Each time the counter of distinct elements increases from 3, it's then reduced to 3
        while counter_distinct > 3:
            # Starting from the left, reduce the number of times of visit
            frequencyDictionary[toString(numbers[index])] = frequencyDictionary[toString(numbers[index])] - 1

            # If the reduced visited time element is not present in further segment then
            # decrease the count of distinct elements
            if frequencyDictionary[toString(numbers[index])] == 0:
                counter_distinct -= 1

            # Increase the starting position of the seeked subsequence
            index += 1

        # Here we check the length of the longest subsequence, and when it's greater than
        # the previous best one, we change it
        if i - index + 1 >= end - beginning + 1:
            end = i
            beginning = index

    return beginning, end


def longest_sequence_modulus_between_0_10(numbers):
    """
    This function returns the first and last positions of the longest sequence in which all the numbers
    have the modulus in [0,10]
    input: numbers - the list of complex numbers
    output: start_max - the starting position of the longest required sequence
            stop_max  - the stopping position of the longest required sequence
    """
    length = 1
    sstart = 0
    stop = 0
    start_max = 0
    stop_max = 0
    length_max = 0
    for i in range(len(numbers) - 1):
        if 0 <= module_calc(numbers[i]) <= 10 and 0 <= module_calc(numbers[i + 1]) <= 10:
            # Increased length of potential sequence & end position
            length += 1
            stop = i + 1
        else:
            # In case we found a new max length sequence
            if length > length_max:
                # Replace the end-result variables(with max) with the auxiliaries accordingly
                length_max = length
                start_max = sstart
                stop_max = stop
            # Moved along in the list, excluding the elem on position i and restarting the length to 1
            sstart = i + 1
            length = 1
    # Extra check in case the last element is part of the required max sequence
    if length > length_max:
        start_max = sstart
        stop_max = stop
    return start_max, stop_max


def start():
    numbers = init_number_list()
    while True:
        print_menu()
        choice = input(">")
        if choice == "1":
            add_number(numbers)
        elif choice == "2":
            show_numbers(numbers)
        elif choice == "3":
            longest_sequence_3_distinct_ui(numbers)
        elif choice == "4":
            longest_sequence_modulus_between_0_10_ui(numbers)
        elif choice == "5":
            break
        else:
            print("Bad command")


start()
