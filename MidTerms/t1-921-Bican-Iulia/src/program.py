# Source code for Test 1 program. Success!
import re

def get_fname(fdef):
    rawinput = fdef.split('(') 
    fname = rawinput[0]
    return fname

def add_fName_tostr(fname, calculations):
    result = fname + "=" + calculations
    return result

def add_fName(fname, calculations):
    result = [fname, calculations]
    return result

def list_fName_tostr(fname, calculations):
    result = "def " + fname + ": return " + calculations
    return result

def inProgram(program, fname):
    for p in program:
        if get_fname(p[0]) == fname:
            return p
    return None

def add_function_ui(program, params):
    """
    :param program: the program in which to add the function
    :param params: the function that will be transformed into list
    :return: prints when succesfully added
    """
    if params == "":
        raise Exception("You need some input after the add command!")
    else:
        fname = params[0]
        calculations = params[1]
        program.append(add_fName(fname, calculations))
        print("Function Added!")

def list_function_ui(program, params):
    if params == "":
        raise Exception("You need some input after the list command!")
    else:
        fname=params
        funct = inProgram(program, fname)
        if funct is None:
            raise Exception("Function not previously defined!")
        else:
            fdef = funct[0]
            fcalc = funct[1]
            print(list_fName_tostr(fdef, fcalc))

def split_aparams(text):
    rawinput = text.split('(')
    fname = rawinput[0]
    rest = rawinput[1]
    rest = rest[:-1] #1,2,3,4
    params = rest.split(",")
    while '' in params:
        params.remove('')
    return fname, params

def split_calcs(text):
    rawinput = re.split('\+|-', text)
    while '' in rawinput:
        rawinput.remove('')
    return rawinput

def read_Params(funct, text):
    """
    For a given instruction, it splits the parameters of the right side of the command
    params: text - the given command
    return: list of parameters
    """
    # if the command were to be 'add   1', then text = '  1  3'
    if funct == 'add':
        params = text.split('=')
    elif funct =='list':
        params = text
    elif funct == 'eval':
        params = split_aparams(text) #funct name, list of act params
    # and here after execution params would be ['','','1','','','3'], so we remove the extra 'empty' spaces in the while
    # while '' in params:
    #     params.remove('')
    return params

def eval_ui(program, params):
    if params == "":
        raise Exception("You need some input after the eval command!")
    else:
        fname = params[0]
        actParams = params[1]
        funct = inProgram(program, fname)
        calculations = funct[1]
        if funct is None:
            raise Exception("Function not previously defined!")
        else:
            formalParams = split_calcs(calculations)
            if len(formalParams) != len(actParams):
                raise Exception("Function not defined like this!")
            else:
                definition = str(calculations)
                assignments=""
                for i in range(len(formalParams)):
                    assignments = assignments + str(formalParams[i]) + "=" + str(actParams[i]) + "\n"
                exec(assignments + "print(" + definition + ")")


def read_Command(text):
    """
    For a given command, it splits the left side from the right side
    params: text - the given command
    return: the command and the parameters separated in a list
    """
    cmd = text.strip().split(' ', 1)
    # cmd[0] = add/list/eval
    return cmd[0], '' if len(cmd) == 1 else read_Params(cmd[0], cmd[1].strip())


def main():
    program = []
    commands = {'add': add_function_ui, 'list': list_function_ui,  'eval': eval_ui}

    while True:
        command = input('Command >> ')
        command = read_Command(command)
        cmd = command[0]  #add/list/eval
        params = command[1]

        if cmd in commands:
            try:
                commands[cmd](program, params)
            except Exception as ex:
                print(ex)
        elif cmd == 'exit':
            break
        else:
            print("Invalid command")

main()
# print(("1,2,3").split(","))
# rawinput = re.split('\+|-', "1+2-3")
# print(rawinput)

# rawinput = re.findall('\+|-', "1+2-3")
# print(rawinput)

#exec("a=5\nb=6\nprint(a+b)\n")

"""
AND GUESS WHAT BITCHES IT WORKSSSSSS
"""