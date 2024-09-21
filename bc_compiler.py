from re import findall
from utilities import *


def bf(block) -> str:
    """
    allow you to write a bf code with a repeat macro (from 2-999). Set your macros with (command, numOfRepeats):\n
    >+<-(>5) = >+<->>>>>
    """
    r_block = block

    macros = findall(r"\(..\)|\(...\)|\(....\)", r_block)
    
    for macro in macros:
        m = macro[1:-1]
        r_block = r_block.replace(macro, m[0]*int(m[1:]))

    return r_block


def repeat(parameters, block) -> str:
    loops = int(parameters[0])
    return block*loops


def Write(parameters) -> str:
    string = get_str(parameters[0])
    newline = opcional_parameter_bool(parameters, 1, True)

    _return = ">"
    memory = 0

    for ascii_num in [ord(c) for c in string]:

        while True:
            if ascii_num == 20:
                _return += "<.>"
                break

            if ascii_num == memory:
                _return += '.'
                break
            elif ascii_num > memory and ascii_num-memory <= 127:
                _return += '+'
                memory += 1
            else:
                _return += '-'
                memory -= 1

            if memory > 255:
                memory = 0
            elif memory < 0:
                memory = 255

    if memory >= 128:
        _return += bf(f"(+{255-memory})")
    else:
        _return += bf(f"(-{memory})")

    _return += '<'

    if newline == True:
        _return += bf("(+10).(-10)")

    return _return


def Find(parameters, side) -> str:
    value = int(parameters[0])
    clean = opcional_parameter_bool(parameters, 1, True)

    _return = side
    _return += bf(f"(-{value})[(+{value}){side}(-{value})]") if 255-value >= 128 else bf(f"(+{256-value})[(-{256-value}){side}(+{256-value})]")

    if clean: _return += bf(f"(+{value})")

    return _return


def FindNext(parameters) -> str:
    _return = Find(parameters, '>')

    return _return


def FindLast(parameters) -> str:
    _return = Find(parameters, '<')

    return _return


def Input(parameters=()) -> str:

    mensage = opcional_parameter_str(parameters, 0, "", False)

    if mensage == "":
        return bf("(-13)[(+13)>,.(-13)]")
    else:
        _return = Write((mensage, "false"))
        _return += bf("(-13)[(+13)>,.(-13)]")
        return _return


def MoveBlocks(parameters) -> str:
    num_of_moves = int(parameters[0])

    move_side = '>' if num_of_moves > 0 else '<'
    num_of_moves = abs(num_of_moves)

    _return = move_side+f"[{move_side}]"
    _return *= num_of_moves

    return _return


def brain_cleaner_build(code_line) -> str:
    
    command = code_line[:code_line.find(':')]

    if command in ("repeat"): # blocks with parameters
        block = code_line[code_line.find('{')+1:code_line.rfind('}')]
        block = enter_scope(block)

        exec_data = {"repeat": repeat}
        parameters = code_line[code_line.find('(')+1:code_line.find(')')].split(',')

        exec(f"r = {command}({parameters}, '{block}')", {}, exec_data)
    
    elif command in ("bf"): # blocks without parameters
        block = code_line[code_line.find('{')+1:code_line.rfind('}')]
        if command != "bf": block = enter_scope(block)

        exec_data = {"bf": bf}

        exec(f"r = {command}('{block}')", {}, exec_data)

    else: # functions
        exec_data = {
            "Write": Write,
            "FindLast": FindLast,
            "FindNext": FindNext,
            "Input": Input,
            "MoveBlocks": MoveBlocks
            }
        parameters = code_line[code_line.find('(')+1:code_line.find(')')].split(',')
        
        exec(f"r = {command}({parameters})", {}, exec_data)

    return exec_data['r']


def enter_scope(code) -> str:

    code_inline = set_inline_code(code)

    _return = ""

    for line_bc in code_inline.split('\n')[:-1]:
        _return += brain_cleaner_build(line_bc)

    return _return

