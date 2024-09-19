def get_file_lines(file) -> int:
    with open(file, 'r', encoding="UTF-8") as file: 
        lines = len(file.readlines())
    
    return lines


def count_moves(bf_block) -> int:
    return bf_block.count(">") - bf_block.count("<")


def get_str(string) -> str:
    _return = string[1:-1]
    _return = _return.replace("\\", "")
    _return = _return.replace("☻", ",")

    return _return


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


def opcional_parameter_bool(parameters, index, default) -> bool | None:
    try:
        if parameters[index] == "true":
            value = True
        elif parameters[index] == "false":
            value = False
        else:
            raise ValueError
    except IndexError:
        value = default
    
    return value

