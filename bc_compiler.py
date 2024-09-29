from re import findall
from utilities import *
from brain_cleaner_classes import *


def bf(memory, block) -> str:
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


def repeat(memory, parameters, block) -> str:
    loops = int(parameters[0])
    return block*loops


def Write(memory, parameters) -> str:
    string = StringBC(parameters[0])
    newline = BoolBC.opcional_parameter(parameters, 1, True)
    set_on_memory = BoolBC.opcional_parameter(parameters, 2, False)

    _return = "" if not set_on_memory else ">"
    memo = 0

    for ascii_num in [ord(c) for c in str(string)]:

        while True:
            if ascii_num == memo:
                _return += '.'
                if set_on_memory: 
                    _return += ">"
                    memo = 0
                break
            elif ascii_num > memo and ascii_num-memo <= 127:
                _return += '+'
                memo += 1
            else:
                _return += '-'
                memo -= 1

            if memo > 255:
                memo = 0
            elif memo < 0:
                memo = 255

    if memo >= 128:
        _return += bf(memory, f"(+{256-memo})")
    else:
        _return += bf(memory, f"(-{memo})")

    if newline == True:
        _return += bf(memory, "(+10).(-10)")

    return _return


def Find(parameters, side, memory) -> str:
    value = ShortBC(parameters[0])
    clean = BoolBC.opcional_parameter(parameters, 1, True)

    _return = side
    _return += bf(memory, f"(-{value})[(+{value}){side}(-{value})]") if 255-value >= 128 else bf(memory, f"(+{256-value})[(-{256-value}){side}(+{256-value})]")

    if clean: _return += bf(memory, f"(+{value})")

    return _return


def FindNext(memory, parameters) -> str:
    _return = Find(parameters, '>', memory)

    return _return


def FindLast(memory, parameters) -> str:
    _return = Find(parameters, '<', memory)

    return _return


def Input(memory, parameters=()) -> str:

    mensage = BoolBC.opcional_parameter(parameters, 0, "", False)

    if mensage == "":
        return bf(memory, "(-13)[(+13)>,.(-13)]")
    else:
        _return = Write(memory, (mensage, "false"))
        _return += bf(memory, "(-13)[(+13)>,.(-13)]")
        return _return


def MoveBlocks(memory, parameters) -> str:
    num_of_moves = ShortBC(parameters[0])

    move_side = '>' if num_of_moves > 0 else '<'
    num_of_moves = abs(num_of_moves)

    _return = move_side+f"[{move_side}]"
    _return *= num_of_moves

    return _return


def brain_cleaner_build(code_line, memory, in_scope=False) -> str:
    
    command = code_line[:code_line.find(':')]

    if command in ("repeat"): # blocks with parameters
        block = code_line[code_line.find('{')+1:code_line.rfind('}')]
        block = enter_scope(block, memory)

        exec_data = {"repeat": repeat}
        parameters = code_line[code_line.find('(')+1:code_line.find(')')].split(',')

        exec(f"r = {command}({memory}, {parameters}, '{block}')", {}, exec_data)
    
    elif command in ("bf"): # blocks without parameters
        block = code_line[code_line.find('{')+1:code_line.rfind('}')]
        if command != "bf": block = enter_scope(block, memory)

        exec_data = {"bf": bf}

        exec(f"r = {command}({memory}, '{block}')", {}, exec_data)

    else: # functions
        exec_data = {
            "Write": Write,
            "FindLast": FindLast,
            "FindNext": FindNext,
            "Input": Input,
            "MoveBlocks": MoveBlocks
            }
        parameters = code_line[code_line.find('(')+1:code_line.find(')')].split(',')
        
        exec(f"r = {command}({memory}, {parameters})", {}, exec_data)

    if not in_scope: memory.update(exec_data['r'])
    return exec_data['r']


def enter_scope(code, memory) -> str:

    code_inline = set_inline_code(code)

    _return = ""

    for line_bc in code_inline.split('\n')[:-1]:
        _return += brain_cleaner_build(line_bc, memory, True)

    return _return

