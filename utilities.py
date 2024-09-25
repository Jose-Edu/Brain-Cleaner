def get_file_lines(file) -> int:
    with open(file, 'r', encoding="UTF-8") as file: 
        lines = len(file.readlines())
    
    return lines


def count_moves(bf_block) -> int:
    return bf_block.count(">") - bf_block.count("<")


def get_str(string) -> str|None:

    if string[0] == '"':
        _return = string[1:-1]
        _return = _return.replace("\\", "")
        _return = _return.replace("☻", ",")
        return _return
    else:
        raise ValueError


def get_bool(value) -> bool|None:
    match value:
        case "true":
            return True
        case "false":
            return False
        case _:
            raise ValueError


def return_file_content(file_path) -> str:

    with open(file_path, 'r', encoding="UTF-8") as file:
        _return = file.read()
    
    return _return


def set_inline_code(code) -> str:
    
    scope = 0
    _code = code

    for index, char in enumerate(_code):
        if char in ('{', '('):
            scope += 1
        elif char in ('}', ')'):
            scope -= 1
        elif char == ';' and scope == 0:
            _code = _code[:index]+'\n'+code[index+1:]

    return _code


def opcional_parameter_bool(parameters, index, default, transform=True) -> bool | None:
    try:
        if transform:
            value = get_bool(parameters[index])
        else:
            value = parameters[index]
    except IndexError:
        value = default
    
    return value


def opcional_parameter_str(parameters, index, default, transform=True) -> str | None:
    try:
        if transform:
            value = get_str(parameters[index])
        else:
            value = parameters[index]
    except IndexError:
        value = default
    
    return value


def memory_update(memory, code) -> dict:

    loop = ""

    for command in code:
        match command:
            case '+':
                if loop == "":
                    if memory["memoryKeys"][memory['acKey']] != 255:
                        memory["memoryKeys"][memory['acKey']] += 1
                    else:
                        memory["memoryKeys"][memory['acKey']] = 0
                else:
                    loop += '+'
            case '-':
                if loop == "":
                    if memory["memoryKeys"][memory['acKey']] != 0:
                        memory["memoryKeys"][memory['acKey']] -= 1
                    else:
                        memory["memoryKeys"][memory['acKey']] = 255
                else:
                    loop += '-'
            case '<':
                if loop == "":
                    if memory["acKey"] != 0: memory["acKey"] -= 1
                else:
                    loop += '<'
            case '>':
                if loop == "":
                    memory["acKey"] += 1
                    if memory["acKey"] == len(memory["memoryKeys"]):
                        memory["memoryKeys"].append(0)
                else:
                    loop += '>'
            case '[':
                loop += '['
            case ']':
                while memory['memoryKeys'][memory['acKey']] != 0:
                    if memory["static"]:
                        memory = memory_update(memory, loop[loop.rfind('[')+1:])

                    else:
                        memory['memoryKeys'][memory['acKey']] = 0

                loop = loop[:loop.rfind('[')]
            case ',':
                memory['static'] = False
                if loop == "":
                    memory["memoryKeys"][memory['acKey']] = 0
                else:
                    loop+= ','
    
    try:
        memory["memoryBlocks"] = str(memory["memoryKeys"][1:-1])[1:-1].replace(' ', '').split(',0,')
        for index, value in enumerate(memory["memoryBlocks"]):
            memory["memoryBlocks"][index] = value.split(',')
            for _index, val in enumerate(memory["memoryBlocks"][index]):
                memory["memoryBlocks"][index][_index] = int(val)
    except ValueError:
        pass

    memory["acBlock"] = memory["memoryKeys"][1:memory["acKey"]+1].count(0)

    return memory