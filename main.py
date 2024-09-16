from utilities import *
from os import remove
from bc_compiler import brain_cleaner_build


# region set mid-code

with open("code.bc", 'r') as code_bc: # create temp.bcm
    with open("temp.bc", 'x') as temp:
        for lc in range(get_file_lines("code.bc")):
            line_text = code_bc.readline()

            line_text = line_text.replace(' ', '')
            line_text = line_text.replace('\n', '')
            line_text = line_text.replace(';', '\n')

            temp.write(line_text)
            
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