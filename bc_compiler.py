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
    loops = parameters[0]
    move_back = "<"*(count_moves(block)+1) if count_moves(block) >= 0 else ">"*((count_moves(block)*-1)-1)
    return bf(f"(+{loops})[>{block}{move_back}-]")


def Write(parameters) -> str:

    string = get_str(parameters[0])
    _return = bf("(+20)>")
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

    _return += bf("<(-20)")

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

    else: # functions with parameters
        exec_data = {"Write": Write}
        parameters = code_line[code_line.find('(')+1:code_line.find(')')].split(',')
        
        exec(f"r = {command}({parameters})", {}, exec_data)

    return exec_data['r']


def enter_scope(code) -> str:

    code_inline = set_inline_code(code)

    _return = ""

    for line_bc in code_inline.split('\n')[:-1]:
        _return += brain_cleaner_build(line_bc)

    return _return