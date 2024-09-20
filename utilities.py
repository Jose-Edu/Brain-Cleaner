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

