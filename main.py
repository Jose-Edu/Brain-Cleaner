from utilities import *
from os import remove
from bc_compiler import brain_cleaner_build


# region set temp-code

with open("code.bc", 'r') as code_bc: # create temp.bcm

    code = code_bc.read()

    with open("temp.bc", 'x') as temp:

        code = code.replace(' ', '')
        code = code.replace('\n', '')

        while True:
            start = code.find("/*")

            if start == -1:
                break
            else:
                end = code.find("*/")+1
                code = code.replace(code[start:end+1], '')
            
        code = code.replace('};', '}\n')
        
        temp.write(code)
            
# endregion

# region write BF

with open("temp.bc", 'r') as code_temp:
    with open("code.bf", 'x') as code_bf:
        for lc in range(get_file_lines("temp.bc")):
            line_bc = code_temp.readline()

            code_bf.write(
                brain_cleaner_build(line_bc)
            )

# endregion

remove("temp.bc")