import os
import math
os.system("cls")
class Calculator:
    def __init__(self, first, second):
        self.first = int(first)
        self.second = int(second)
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return int(self.first)+int(self.second)
    def pow(self):
        return self.first**self.second
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second
    def prod(self):
        return self.first*self.second
    def sin(self):
        return math.sin(self.first)
    def cos(self):
        return math.cos(self.first)
    def tan(self):
        return math.tan(self.first)
while True:
    a=input("입력")#.replace(" ", "")
    #print("cos" in a.lower())
    #print(a.lower().find("cos"))
    if a.find("+")==True:
        c = a.split("+")
        test1=Calculator(c[0],c[1])
        print(test1.add())
    elif a.find("-")==True:
        c = a.replace(" ", "").split("-")
        test1=Calculator(c[0],c[1])
        print(test1.min())
    elif a.find("/")==True:
        c = a.replace(" ", "").split("/")
        test1=Calculator(c[0],c[1])
        print(test1.div())
    elif a.find("**")==True:
        c = a.replace(" ", "").split("**")
        test1=Calculator(c[0],c[1])
        print(test1.pow())
    elif a.find("*")==True:
        c = a.replace(" ", "").split("*")
        test1=Calculator(c[0],c[1])
        print(test1.prod())
    # if "sin" in a.lower()==True:
    #     c = a.replace(" ", "").split("sin")
    #     test1=Calculator(c[0],0)
    #     print(test1.sin())
    # elif a.find("cos")==True:
    #     c = a.replace(" ", "").split("cos")
    #     test1=Calculator(c[0],0)
    #     print(test1.tan())
    # elif "tan" in a.lower()==True:
    #     c = a.replace(" ", "").split("tan")
    #     test1=Calculator(c[0],0)
    #     print(test1.tan())
    # elif a.find("0")==True:
    #     break
    else:
        print("Please rewrite")