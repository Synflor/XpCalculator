from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(303, 196)
        Dialog.setWindowTitle("Runique Xp Calculator")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Pictures/Photoshop/Runique/Logo..png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.currentGamemode = QtWidgets.QComboBox(Dialog)
        self.currentGamemode.setGeometry(QtCore.QRect(20, 40, 111, 22))
        self.currentGamemode.setObjectName("currentGamemode")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.newGamemode = QtWidgets.QComboBox(Dialog)
        self.newGamemode.setGeometry(QtCore.QRect(170, 40, 111, 22))
        self.newGamemode.setObjectName("newGamemode")
        self.newGamemode.addItem("")
        self.newGamemode.addItem("")
        self.newGamemode.addItem("")
        self.newGamemode.addItem("")
        self.newGamemode.addItem("")
        self.newGamemode.addItem("")
        self.currentXp = QtWidgets.QLineEdit(Dialog)
        self.currentXp.setGeometry(QtCore.QRect(20, 70, 111, 20))
        self.currentXp.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.currentXp.setAlignment(QtCore.Qt.AlignCenter)
        self.currentXp.setObjectName("currentXp")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.calculatedXp = QtWidgets.QLineEdit(Dialog)
        self.calculatedXp.setEnabled(True)
        self.calculatedXp.setGeometry(QtCore.QRect(170, 70, 111, 20))
        self.calculatedXp.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.calculatedXp.setAlignment(QtCore.Qt.AlignCenter)
        self.calculatedXp.setReadOnly(True)
        self.calculatedXp.setObjectName("calculatedXp")
        self.calculateButton = QtWidgets.QPushButton(Dialog)
        self.calculateButton.setGeometry(QtCore.QRect(170, 160, 111, 21))
        self.calculateButton.setObjectName("calculateButton")
        self.calculatedXpTill99 = QtWidgets.QLineEdit(Dialog)
        self.calculatedXpTill99.setEnabled(True)
        self.calculatedXpTill99.setGeometry(QtCore.QRect(20, 160, 111, 20))
        self.calculatedXpTill99.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.calculatedXpTill99.setAlignment(QtCore.Qt.AlignCenter)
        self.calculatedXpTill99.setReadOnly(True)
        self.calculatedXpTill99.setObjectName("calculatedXpTill99")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.enteredLvlCompared = QtWidgets.QLineEdit(Dialog)
        self.enteredLvlCompared.setGeometry(QtCore.QRect(80, 130, 51, 20))
        self.enteredLvlCompared.setMaxLength(3)
        self.enteredLvlCompared.setAlignment(QtCore.Qt.AlignCenter)
        self.enteredLvlCompared.setObjectName("enteredLvlCompared")
        self.currentLevel = QtWidgets.QLineEdit(Dialog)
        self.currentLevel.setGeometry(QtCore.QRect(20, 100, 111, 20))
        self.currentLevel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentLevel.setObjectName("currentLevel")
        self.currentLevel.setReadOnly(True)
        self.calculatedLevel = QtWidgets.QLineEdit(Dialog)
        self.calculatedLevel.setGeometry(QtCore.QRect(170, 100, 111, 20))
        self.calculatedLevel.setAlignment(QtCore.Qt.AlignCenter)
        self.calculatedLevel.setObjectName("calculatedLevel")
        self.calculatedLevel.setReadOnly(True)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(140, 40, 20, 141))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.currentGamemode, self.newGamemode)
        Dialog.setTabOrder(self.newGamemode, self.currentXp)
        Dialog.setTabOrder(self.currentXp, self.calculateButton)
        Dialog.setTabOrder(self.calculateButton, self.calculatedXp)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.currentGamemode.setItemText(0, _translate("Dialog", "Extreme"))
        self.currentGamemode.setItemText(1, _translate("Dialog", "Legend"))
        self.currentGamemode.setItemText(2, _translate("Dialog", "Iron Man"))
        self.currentGamemode.setItemText(3, _translate("Dialog", "Immortal"))
        self.currentGamemode.setItemText(4, _translate("Dialog", "Hardcore Iron Man"))
        self.currentGamemode.setItemText(5, _translate("Dialog", "Grand Master"))
        self.newGamemode.setItemText(0, _translate("Dialog", "Extreme"))
        self.newGamemode.setItemText(1, _translate("Dialog", "Legend"))
        self.newGamemode.setItemText(2, _translate("Dialog", "Iron Man"))
        self.newGamemode.setItemText(3, _translate("Dialog", "Immortal"))
        self.newGamemode.setItemText(4, _translate("Dialog", "Hardcore Iron Man"))
        self.newGamemode.setItemText(5, _translate("Dialog", "Grand Master"))
        self.currentXp.setPlaceholderText(_translate("Dialog", "Amount of xp"))
        self.label.setText(_translate("Dialog", "Current"))
        self.label_2.setText(_translate("Dialog", "To"))
        self.calculatedXp.setPlaceholderText(_translate("Dialog", "Calculated xp amount"))
        self.calculateButton.setText(_translate("Dialog", "Calculate"))
        self.calculatedXpTill99.setPlaceholderText(_translate("Dialog", "In current gamemode"))
        self.label_3.setText(_translate("Dialog", "Xp till: "))
        self.enteredLvlCompared.setText(_translate("Dialog", "99"))
        self.enteredLvlCompared.setPlaceholderText(_translate("Dialog", "Lvl"))
        self.currentLevel.setPlaceholderText(_translate("Dialog", "Current level"))
        self.calculatedLevel.setPlaceholderText(_translate("Dialog", "Calculated level"))