def compiler(command, parameters, code_line):
    pass


def brain_cleaner_build(code_line) -> str:
    
    command = code_line[:code_line.find(':')]

    if command in ("repeat", "repeat!"):
       parameters = code_line[code_line.find('(')+1].split(',')
    else:
        parameters = []

    block = code_line[code_line.find('{')+1: code_line.find('}')]

    return compiler(command, parameters, code_line)

