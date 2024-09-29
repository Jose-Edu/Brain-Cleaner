class Memory():
    
    ac_key = 0
    memory_keys = [0]
    memory_blocks = []
    memory_blocks_content = []
    ac_block = 0
    var_list = {}
    static = True
    inf_loop = False

    def update(self, code) -> None:

        loop = ""

        for command in code:
            match command:
                case '+':
                    if loop == "":
                        if self.memory_keys[self.ac_key] != 255:
                            self.memory_keys[self.ac_key] += 1
                        else:
                            self.memory_keys[self.ac_key] = 0
                    else:
                        loop += '+'
                case '-':
                    if loop == "":
                        if self.memory_keys[self.ac_key] != 0:
                            self.memory_keys[self.ac_key] -= 1
                        else:
                            self.memory_keys[self.ac_key] = 255
                    else:
                        loop += '-'
                case '<':
                    if loop == "":
                        if self.ac_key != 0: self.ac_key -= 1
                    else:
                        loop += '<'
                case '>':
                    if loop == "":
                        self.ac_key += 1
                        if self.ac_key == len(self.memory_keys):
                            self.memory_keys.append(0)
                    else:
                        loop += '>'
                case '[':
                    loop += '['
                case ']':
                    while self.ac_key[self.ac_key] != 0:
                        if self.static:
                            memory = self.update(memory, loop[loop.rfind('[')+1:])

                        else:
                            self.ac_key[self.ac_key] = 0

                    loop = loop[:loop.rfind('[')]
                case ',':
                    self.static = False
                    if loop == "":
                        self.memory_keys[self.ac_key] = 0
                    else:
                        loop+= ','
        
        try:
            self.memory_blocks = str(self.memory_keys[1:-1])[1:-1].replace(' ', '').split(',0,')
            for index, value in enumerate(self.memory_blocks):
                self.memory_blocks[index] = value.split(',')
                for _index, val in enumerate(self.memory_blocks[index]):
                    self.memory_blocks[index][_index] = int(val)
        except ValueError:
            pass

        self.ac_block = self.memory_keys[1:self.ac_key+1].count(0)


class DataType():

    def __init__(self, value):
        self.value = value

    def opcional_parameter(self, parameters, index, default, transform=True) -> any:
            try:
                if transform:
                    value = self.value
                else:
                    value = parameters[index]
            except IndexError:
                value = default
            
            return value

    def __str__(self) -> str:
        return self.value

    def __eq__(self, value: object) -> bool:
        return self.value == value
    
    def __repr__(self) -> str:
        return self.value


class StringBC(DataType):

    def __init__(self, value='""'):
        super().__init__(value)

        if value[0] == '"':
            new_value = value[1:-1]
            new_value = new_value.replace("\\", "")
            new_value = new_value.replace("☻", ",")
            self.value = new_value
        else:
            raise ValueError


class BoolBC(DataType):

    def __init__(self, value):
        super().__init__(value)

        match value:
            case "true":
                self.value = True
            case "false":
                self.value = False
            case _:
                raise ValueError

    def __ne__(self, value: object) -> bool:
        return not self.value
    
    def __or__(self, value: any) -> bool:
        return self.value | value
    
    def __ror__(self, value: any) -> bool:
        return value | self.value


class NumBaseType(DataType):

    def __init__(self, value, min, max):
        super().__init__(value)
        self.min = min
        self.max = max

        value_check = int(value)
        if value_check > self.max or value_check < self.min:
            self.value = value_check
        else:
            raise ValueError
    
    def limit(self, value):
        if value > self.max or value < self.min:
            raise ValueError
    
    def __add__(self, other):
        return self.value+other.value
    
    def __sub__(self, other):
        return self.value-other.value
    
    def __mul__(self, other):
        return self.value*other.value
    
    def __truediv__(self, other):
        return self.value/other.value
    
    def __floordiv__(self, other):
        return self.value//other.value
    
    def __mod__(self, other):
        return self.value%other.value
    
    def __iadd__(self, other):
        self.limit(self.value+other.value)
        self.value+=other.value
    
    def __isub__(self, other):
        self.limit(self.value-other.value)
        self.value-=other.value
    
    def __imul__(self, other):
        self.limit(self.value*other.value)
        self.value*=other.value
    
    def __itruediv__(self, other):
        self.limit(self.value/other.value)
        self.value = int(self.value/other.value)

    def __ifloordiv__(self, other):
        self.limit(self.value//other.value)
        self.value//=other.value
    
    def __imod__(self, other):
        self.limit(self.value%other.value)
        self.value%=other.value


class ShortBC(NumBaseType):
    
    def __init__(self, value):
        super().__init__(value, 0, 255)

