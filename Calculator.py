class Calculator:
    def __init__(self):
        self.M1 = 0
        self.M2 = 0
        self.M3 = 0
        self.M4 = 0
        self.__MemoryPointer = 0
        print("Object is created.")

    def receiver(self, input):
        self.__input = input
        self.parser(input)

    def parser(self, input):
        if(input.find('+') != -1):
            operator = '+'
            splitted_input = input.split('+')
            print("Operator is selected as '+'")
        elif(input.find('-') != -1):
            operator = '-'
            splitted_input = input.split('-')
            print("Operator is selected as '-'")
        elif (input.find('*') != -1):
            operator = '*'
            splitted_input = input.split('*')
            print("Operator is selected as '*'")
        elif (input.find('/') != -1):
            operator = '/'
            splitted_input = input.split('/')
            print("Operator is selected as '/'")
        else:
            print("Wrong Input, program will terminate.")
            exit()

        a = splitted_input[0]
        b = splitted_input[1]

        if (a.isdigit() and b.isdigit()):
            a = int(a)
            b = int(b)
            print("Operands are : " + str(a) + " and " + str(b))
        else:
            print("Wrong Input, program will terminate.")
            exit()

        if (operator == '+'):
            self.setMemo(self.add(a,b))
        elif(operator == '-'):
            self.setMemo(self.sub(a, b))
        elif (operator == '*'):
            self.setMemo(self.mult(a, b))
        else:
            self.setMemo(self.kurt(a,b))
    def add(self, a, b):
        print("Addition operation, the result is: " + str(a+b))
        return a+b

    def sub(self, a, b):
        print("Substraction operation, the result is: " + str(a-b))
        return a-b

    def mult(self, a, b):
        print("Multiplication operation, the result is: " + str(a*b))
        return a*b

    def kurt(self, a, b):
        print("Division operation, the result is: " + str(a/b))
        return a/b

    def setMemo(self, result):
        if (self.__MemoryPointer == 0):
            self.M1 = result
            print("Result is loaded into M1")
        elif(self.__MemoryPointer == 1):
            self.M2 = result
            print("Result is loaded into M2")
        elif(self.__MemoryPointer == 2):
            self.M3 = result
            print("Result is loaded into M3")
        else:
            self.M4 = result
            print("Result is loaded into M4")

        self.__MemoryPointer = (self.__MemoryPointer + 1) % 4