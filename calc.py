from PyQt5 import QtCore, QtGui, QtWidgets
import qdarktheme


# Enable HiDPI.
qdarktheme.enable_hi_dpi()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(352, 556)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.OutputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OutputLabel.setLineWidth(3)
        self.OutputLabel.setText("0")
        self.OutputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.OutputLabel.setObjectName("OutputLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget,
                                                   clicked = lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(95, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget,
                                                 clicked = lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(185, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget,
                                                 clicked = lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(95, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(185, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(275, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(95, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(185, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(275, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(95, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(185, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.plus_minus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(185, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(95, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(275, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 352, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # add a remove character
    def remove_it(self):
        #grab the screen last variable
        screen = self.OutputLabel.text()
        #remove the last item in list/string
        screen = screen[:-1]
        self.OutputLabel.setText(screen)

    #change from positve/negative
    def plus_minus_it(self):
        
        screen = self.OutputLabel.text()
        # Replace multiple characters at once
        if screen[0] == '-':
            screen = screen[1:]
        else:
            screen = f'+{screen}'
        screen = screen.replace('+', '%temp%').replace('-', '+').replace('%temp%', '-')
        self.OutputLabel.setText(screen)

    # lets do some math
    def math_it(self):
        screen = self.OutputLabel.text()
        #do the math
        try:
            answer = eval(screen)
            self.OutputLabel.setText(str(answer))
        except:
            self.OutputLabel.setText("ERROR")
    
    # add a decimal
    def dot_it(self):
        screen = self.OutputLabel.text()
        dmas = ['+','-','*','/','%']
        ivalid = False
        for each in dmas:
            if each in screen:
                ivalid = True
                index = screen[1:].rfind(each)
                if ("." in screen[index:]):
                    pass
                else:
                    self.OutputLabel.setText(f'{screen}.')          

        if ivalid == False:
            if ("." in screen):
                pass
            else:
                self.OutputLabel.setText(f'{screen}.')          

    def press_it(self, pressed):
        if pressed == "C":
            self.OutputLabel.setText("0")
        else:
            if  self.OutputLabel.text() == "0":
                self.OutputLabel.setText("")
            self.OutputLabel.setText(f'{self.OutputLabel.text()}{pressed}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.equalButton.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # Apply dark theme.
    qdarktheme.setup_theme()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())