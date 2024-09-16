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
    return bf(f"(+{loops})[{block}(<{count_moves(block)})-]")


def Write(parameters) -> str:

    _return = "[-]"

    for ascii_num in [ord(c) for c in parameters[0]]:
        _return += bf(f"(+{ascii_num}).[-]")

    return _return


def brain_cleaner_build(code_line) -> str:
    
    command = code_line[:code_line.find(':')]

    if command in ("repeat"): # blocks with parameters
        block = code_line[code_line.find('{')+1: code_line.find('}')]
        exec_data = {"repeat": repeat}
        parameters = code_line[code_line.find('(')+1:code_line.find(')')].split(',')
        exec(f"r = {command}({parameters}, '{block}')", {}, exec_data)
    elif command in ("bf"): # blocks without parameters
        block = code_line[code_line.find('{')+1:code_line.find('}')]
        exec_data = {"bf": bf}
        exec(f"r = {command}('{block}')", {}, exec_data)
    else: # functions
        exec_data = {"Write": Write}
        parameters = code_line[code_line.find('(')+1:code_line.find(')')].split(',')
        exec(f"r = {command}({parameters})", {}, exec_data)

    return exec_data['r']

