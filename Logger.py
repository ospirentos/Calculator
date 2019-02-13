import time

class Logger:
    def __init__(self):
        self.__isConsoleLoggingActive = False
        self.__isFileLoggingActive = True

    """Fix this shit!
    def __del__(self):
        self.write("Program is terminated.")"""
    def setConsoleLogging(self, a):
        if(a == True or a == False):
            self.__isConsoleLoggingActive = a
        else:
            self.write("In Logger class: In setConsoleLogging method: Wrong input.")

    def setFileLogging(self, a):
        if(a == True or a == False):
            self.__isFileLoggingActive = a
        else:
            self.write("In Logger class: In setFileLogging method: Wrong input.")

    def write(self, stringToWrite):
        if (self.__isFileLoggingActive == True):
            with open("KurtLog.txt", 'a') as file:
                file.write(time.ctime(time.time()) + " -> " + stringToWrite + "\n")

        if (self.__isConsoleLoggingActive == True):
            print(time.ctime(time.time()) + " -> " +stringToWrite)


