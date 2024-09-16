from re import findall


def bf(block) -> str:

    """
    return a bf code, command by command
    """
    return block


def bfMacro(block) -> str:
    """
    allow you to write a bf code with a repeat macro (from 2-999). Set your macros with (command, numOfRepeats):\n
    >+<-(>5) = >+<->>>>>
    """
    r_block = block

    macros = findall(r"\(..\)|\(...\)|\(....\)", r_block)
    
    for macro in macros:
        m = macro[1:-1]
        print(macro, m, m[0]*int(m[1:]))
        r_block = r_block.replace(macro, m[0]*int(m[1:]))

    return r_block


def brain_cleaner_build(code_line) -> str:
    
    command = code_line[:code_line.find(':')]
    block = code_line[code_line.find('{')+1: code_line.find('}')]

    _return = {
        "bf": bf,
        "bfMacro": bfMacro
    }

    if command in ("repeat", "repeatMacro"):
        parameters = code_line[code_line.find('(')+1].split(',')
        exec(f"r = {command}({parameters}, {block})", {}, _return)
    else:
        exec(f"r = {command}('{block}')", {}, _return)

    return _return['r']

