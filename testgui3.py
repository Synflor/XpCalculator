from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(310, 143)
        Dialog.setWindowTitle("Runique Xp Calculator")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Pictures/Photoshop/Runique/Logo..png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.currentGamemode = QtWidgets.QComboBox(Dialog)
        self.currentGamemode.setGeometry(QtCore.QRect(50, 20, 111, 22))
        self.currentGamemode.setObjectName("currentGamemode")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.newGamemode = QtWidgets.QComboBox(Dialog)
        self.newGamemode.setGeometry(QtCore.QRect(50, 50, 111, 22))
        self.newGamemode.setObjectName("newGamemode")
        self.newGamemode.addItem("")
        self.newGamemode.addItem("")
        self.newGamemode.addItem("")
        self.newGamemode.addItem("")
        self.newGamemode.addItem("")
        self.newGamemode.addItem("")
        self.currentXp = QtWidgets.QLineEdit(Dialog)
        self.currentXp.setGeometry(QtCore.QRect(180, 20, 111, 20))
        self.currentXp.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.currentXp.setAlignment(QtCore.Qt.AlignCenter)
        self.currentXp.setObjectName("currentXp")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.calculatedXp = QtWidgets.QLineEdit(Dialog)
        self.calculatedXp.setEnabled(True)
        self.calculatedXp.setGeometry(QtCore.QRect(180, 50, 111, 20))
        self.calculatedXp.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.calculatedXp.setAlignment(QtCore.Qt.AlignCenter)
        self.calculatedXp.setReadOnly(True)
        self.calculatedXp.setObjectName("calculatedXp")
        self.calculateButton = QtWidgets.QPushButton(Dialog)
        self.calculateButton.setGeometry(QtCore.QRect(210, 110, 81, 21))
        self.calculateButton.setObjectName("calculateButton")
        self.calculatedXpTill99 = QtWidgets.QLineEdit(Dialog)
        self.calculatedXpTill99.setEnabled(True)
        self.calculatedXpTill99.setGeometry(QtCore.QRect(180, 80, 111, 20))
        self.calculatedXpTill99.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.calculatedXpTill99.setAlignment(QtCore.Qt.AlignCenter)
        self.calculatedXpTill99.setReadOnly(True)
        self.calculatedXpTill99.setObjectName("calculatedXpTill99")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")

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
        self.label.setText(_translate("Dialog", "From"))
        self.label_2.setText(_translate("Dialog", "To"))
        self.calculatedXp.setPlaceholderText(_translate("Dialog", "Calculated xp amount"))
        self.calculateButton.setText(_translate("Dialog", "Calculate"))
        self.calculatedXpTill99.setPlaceholderText(_translate("Dialog", "in current gamemode"))
        self.label_3.setText(_translate("Dialog", "Xp till you reach 99"))