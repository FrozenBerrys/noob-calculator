import sys
import random
from PyQt5 import QtCore, QtWidgets as qtw, QtGui

def isInt(string):
    if ord(string) < 48 or ord(string) > 57:
        return False
    return True

class MakeWidget(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = [] # LAST ENTERED ELEMENT
        self.fin_nums = [] # concatenation of all entered elements w/ or w/o temp_num
        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        #button declaration and signal functionality
        self.result_field = qtw.QLineEdit()
        btn_result = qtw.QPushButton("Enter", clicked = lambda: self.calculate())
        btn_clear = qtw.QPushButton("Clear", clicked = lambda: self.calc_clear())
        btn_0 = qtw.QPushButton("0", clicked = lambda: self.num_pressed('0'))
        btn_1 = qtw.QPushButton("1", clicked = lambda: self.num_pressed('1'))
        btn_2 = qtw.QPushButton("2", clicked = lambda: self.num_pressed('2'))
        btn_3 = qtw.QPushButton("3", clicked = lambda: self.num_pressed('3'))
        btn_4 = qtw.QPushButton("4", clicked = lambda: self.num_pressed('4'))
        btn_5 = qtw.QPushButton("5", clicked = lambda: self.num_pressed('5'))
        btn_6 = qtw.QPushButton("6", clicked = lambda: self.num_pressed('6'))
        btn_7 = qtw.QPushButton("7", clicked = lambda: self.num_pressed('7'))
        btn_8 = qtw.QPushButton("8", clicked = lambda: self.num_pressed('8'))
        btn_9 = qtw.QPushButton("9", clicked = lambda: self.num_pressed('9'))
        btn_plus = qtw.QPushButton("+", clicked = lambda: self.func_pressed('+'))
        btn_minus = qtw.QPushButton("-", clicked = lambda: self.func_pressed('-'))
        btn_mult = qtw.QPushButton("x", clicked = lambda: self.func_pressed('*'))
        btn_divd = qtw.QPushButton("÷", clicked = lambda: self.func_pressed('/'))

        #layout
        container.layout().addWidget(self.result_field,0,0,1,4)
        container.layout().addWidget(btn_result,1,0,1,2)
        container.layout().addWidget(btn_clear,1,2,1,2)
        container.layout().addWidget(btn_9,2,0)
        container.layout().addWidget(btn_8,2,1)
        container.layout().addWidget(btn_7,2,2)
        container.layout().addWidget(btn_plus,2,3)
        container.layout().addWidget(btn_6,3,0)
        container.layout().addWidget(btn_5,3,1)
        container.layout().addWidget(btn_4,3,2)
        container.layout().addWidget(btn_minus,3,3)
        container.layout().addWidget(btn_3,4,0)
        container.layout().addWidget(btn_2,4,1)
        container.layout().addWidget(btn_1,4,2)
        container.layout().addWidget(btn_mult,4,3)
        container.layout().addWidget(btn_0,5,0,1,3)
        container.layout().addWidget(btn_divd,5,3)
        self.layout().addWidget(container)

    def num_pressed(self, key):
         self.temp_nums.append(key)
         temp_string = ''.join(self.temp_nums) 
         if self.fin_nums:
             self.result_field.setText(''.join(self.fin_nums) + temp_string)
         else: 
             self.result_field.setText(temp_string)

    def func_pressed(self, key):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(key)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))
    
    def calculate(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        prev = "num"
        if fin_string[0] != '-' and isInt(fin_string[0]) == False: #allows negative numbers uhh 
            return

        #error handling invalid eval inputs
        for i in range(len(fin_string)):
            if isInt(fin_string[i]) == False and prev == "func":
                return
            if isInt(fin_string[i]):
                prev = "num"
            elif isInt(fin_string[i]) == False:
                prev = "func"
        if isInt(fin_string[-1]) == False: 
            return

        result_string = eval(fin_string)
        fin_string = str(result_string)
        self.result_field.setText(fin_string)
        self.temp_nums = [] #resetting equation to result
        self.fin_nums = [str(result_string)]

    def calc_clear(self):
        cur = self.result_field
        if cur != "":
            self.result_field.clear()
            self.temp_nums = []
            self.fin_nums = []

app = qtw.QApplication([])

mw = MakeWidget()
app.setStyle(qtw.QStyleFactory.create("Fusion"))
sys.exit(app.exec_())