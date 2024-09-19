from utilities import *
from os import remove
from bc_compiler import brain_cleaner_build
from re import findall


# region set temp-mid-code

with open("code.bc", 'r', encoding="UTF-8") as code_bc: # create temp.bcm

    code = code_bc.read()

    with open("./output/temp.bcm", 'x', encoding="UTF-8") as temp:

        while True: # remove comments
            start = code.find("/*")

            if start == -1:
                break
            else:
                end = code.find("*/")+1
                code = code.replace(code[start:end+1], '')
        
        # region protect the string from the next clear blocks
        
        code = code.replace('\\"','֎')
        
        strings = findall('"[^"]*"', code)

        for str_ac in strings:
            string = str_ac[1:-1]
            string = string.replace(" ", "☺")
            string = string.replace(",", "☻")
            string = string.replace("֎", '\\"')
            string = string.replace(";", "Ώ")
            code = code.replace(str_ac, str_ac[0]+string+str_ac[-1])

        # endregion

        code = code.replace(' ', '') # remove all the white spaces
        code = code.replace('\n', '') # set all the code in 1 line

        # split the code in lines
        code = set_inline_code(code)

        code = code.replace("☺", " ") # returns the whitespaces for the strings
        code = code.replace("Ώ", ";") # returns the interns ; in the code

        temp.write(code)
            
# endregion

# region write BF

with open("./output/temp.bcm", 'r', encoding="UTF-8") as code_temp:
    with open("./output/main.bf", 'w', encoding="UTF-8") as main_bf:
        for lc in range(get_file_lines("./output/temp.bcm")):
            line_bc = code_temp.readline()

            main_bf.write(
                brain_cleaner_build(line_bc)
            )

# endregion

remove("./output/temp.bcm")