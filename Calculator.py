from Logger import *

CalcLog = Logger()

class Calculator:
    def __init__(self):
        self.M1 = 0
        self.M2 = 0
        self.M3 = 0
        self.M4 = 0
        self.__MemoryPointer = 0
        CalcLog.write("Object is created.")

    def receiver(self, input):
        self.__input = input
        self.parser(input)

    def parser(self, input):
        if(input.find('+') != -1):
            operator = '+'
            splitted_input = input.split('+')
            CalcLog.write("Operator is selected as '+'")
        elif(input.find('-') != -1):
            operator = '-'
            splitted_input = input.split('-')
            CalcLog.write("Operator is selected as '-'")
        elif (input.find('*') != -1):
            operator = '*'
            splitted_input = input.split('*')
            CalcLog.write("Operator is selected as '*'")
        elif (input.find('/') != -1):
            operator = '/'
            splitted_input = input.split('/')
            CalcLog.write("Operator is selected as '/'")
        else:
            CalcLog.write("Wrong Input, program will terminate.")
            exit()

        a = splitted_input[0]
        b = splitted_input[1]

        if (a.isdigit() and b.isdigit()):
            a = int(a)
            b = int(b)
            CalcLog.write("Operands are : " + str(a) + " and " + str(b))
        else:
            CalcLog.write("Wrong Input, program will terminate.")
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
        CalcLog.write("Addition operation, the result is: " + str(a+b))
        return a+b

    def sub(self, a, b):
        CalcLog.write("Substraction operation, the result is: " + str(a-b))
        return a-b

    def mult(self, a, b):
        CalcLog.write("Multiplication operation, the result is: " + str(a*b))
        return a*b

    def kurt(self, a, b):
        CalcLog.write("Division operation, the result is: " + str(a/b))
        return a/b

    def setMemo(self, result):
        if (self.__MemoryPointer == 0):
            self.M1 = str(result)
            CalcLog.write("Result is loaded into M1")
        elif(self.__MemoryPointer == 1):
            self.M1 = str(result)
            CalcLog.write("Result is loaded into M2")

        elif(self.__MemoryPointer == 2):
            self.M1 = str(result)
            CalcLog.write("Result is loaded into M3")
        else:
            self.M1 = str(result)
            CalcLog.write("Result is loaded into M4")

        self.__MemoryPointer = (self.__MemoryPointer + 1) % 4
