
with open(input("Enter file path: "), 'r') as file:
    tokens = [line.rstrip('\n') for line in file if line != '\n'] #standard tokenize from file

tokens = [t for t in tokens if t[0] != "`"] #make the interpreter ignore any comments

#further split tokens based on section headers
configTokens = tokens[:tokens.index("~DEFENITION~")]
definitionTokens = tokens[tokens.index("~DEFENITION~") + 1 : tokens.index("~SCHEMATIC~")]
schematicTokens = tokens[tokens.index("~SCHEMATIC~") + 1 : tokens.index("~EXECUTE~")]
executeTokens = tokens[tokens.index("~EXECUTE~") + 1:]

definitionTokens = [token.replace(" ", "") for token in definitionTokens]

conobi_dict = {}

for i in definitionTokens:
    conobi_dict[i[0]] = i[2:].split('/') #further tokenize conobi definition

executeTokens = [t for t in executeTokens[0].split("/")]

conobi_matrix = [list(i) for i in schematicTokens]

value_matrix = [[0] * len(i) for i in conobi_matrix] #create zeroed matrix with same dimensions as conobi_matrix

class header():
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
    
    def jump(self, x, y, relative=False):
        if relative:
            self.pos_x += int(x)
            self.pos_y += int(y)
        else:
            self.pos_x = int(x)
            self.pos_y = int(y)
    
    def read_conobi(self):
        return conobi_matrix[self.pos_y][self.pos_x]

    def read_value(self):
        return value_matrix[self.pos_y][self.pos_x]

    def write(self, value):
        try:
            value_matrix[self.pos_y][self.pos_x] = int(value)
        except:
            raise Exception("Attempted to access element outside Conobi Matrix; halting program")
    
    def mutate(self): #store the first instruction of the conobi at current location
        self.instruction = conobi_dict[conobi_matrix[self.pos_y][self.pos_x]][0]
        self.modValue = int(self.instruction[3:]) if self.instruction[3:] != "" else 1
        match self.instruction[:3]:
            case "add":
                self.write(self.read_value() + self.modValue)
            case "sub":
                self.write(self.read_value() - self.modValue)
            case "mul":
                self.write(self.read_value() * self.modValue)
            case "div":
                self.write(self.read_value() / self.modValue)
            case "exp":
                self.write(self.read_value() ** self.modValue)
            # case "rot": doesnt work for some reason
            #     self.write(self.read_value() ** (1/self.modValue))
            case "out":
                print(chr(self.read_value()) * self.modValue, end="")
        
    def understandCondition(self, condition): #tokenize contiion and return true or false
        if condition == "~":
            return False
        if condition == "?":
            return True
        self.condition_value = float(condition[2:])
        match condition[:2]:
            case "gt":
                return self.read_value() > self.condition_value
            case "lt":
                return self.read_value() < self.condition_value
            case "eq":
                return self.read_value() == self.condition_value
            case "ne":
                return self.read_value() != self.condition_value
            case "ge":
                return self.read_value() >= self.condition_value
            case "le":
                return self.read_value() <= self.condition_value
        
    def evaluate(self): #check conditions and jump accordingy
        self.conditionList = conobi_dict[conobi_matrix[self.pos_y][self.pos_x]][1:]
        if self.understandCondition(self.conditionList[0]): #fix this awful elif tower eventually
            self.tempval = self.read_value()
            self.jump(0, 1, True)
            self.write(self.tempval)
        elif self.understandCondition(self.conditionList[1]):
            self.tempval = self.read_value()
            self.jump(1, 0, True)
            self.write(self.tempval)
        elif self.understandCondition(self.conditionList[2]):
            self.tempval = self.read_value()
            self.jump(0, -1, True)
            self.write(self.tempval)
        elif self.understandCondition(self.conditionList[3]):
            self.tempval = self.read_value()
            self.jump(-1, 0, True)
            self.write(self.tempval)
        else:
            raise Exception("No codition of current Conobi returned true; halting program")


head = header() #init header with ~EXECUTE~ parameters
head.jump(executeTokens[0], executeTokens[1])
head.write(executeTokens[2])

while True:
    try:
        head.mutate()
    except:
        break
    try:
        head.evaluate()
    except:
        break
