# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BonesCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(249, 392)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 330, 231, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.currentGamemode = QtWidgets.QComboBox(Dialog)
        self.currentGamemode.setGeometry(QtCore.QRect(10, 30, 111, 22))
        self.currentGamemode.setFrame(True)
        self.currentGamemode.setObjectName("currentGamemode")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.currentGamemode.addItem("")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(150, 30, 81, 17))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 111, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 110, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 111, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 111, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 200, 111, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 111, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 240, 111, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(10, 260, 111, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(10, 280, 111, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(10, 300, 111, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(140, 140, 91, 20))
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setReadOnly(True)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox.setMaximum(1000000000)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(140, 160, 91, 20))
        self.spinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_2.setReadOnly(True)
        self.spinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_2.setMaximum(1000000000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(140, 180, 91, 20))
        self.spinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_3.setReadOnly(True)
        self.spinBox_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_3.setMaximum(1000000000)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(140, 200, 91, 20))
        self.spinBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_4.setReadOnly(True)
        self.spinBox_4.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_4.setMaximum(1000000000)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_5.setGeometry(QtCore.QRect(140, 220, 91, 20))
        self.spinBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_5.setReadOnly(True)
        self.spinBox_5.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_5.setMaximum(1000000000)
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_6 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(140, 240, 91, 20))
        self.spinBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_6.setReadOnly(True)
        self.spinBox_6.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_6.setMaximum(1000000000)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_7.setGeometry(QtCore.QRect(140, 260, 91, 20))
        self.spinBox_7.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_7.setReadOnly(True)
        self.spinBox_7.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_7.setMaximum(1000000000)
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_8 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_8.setGeometry(QtCore.QRect(140, 280, 91, 20))
        self.spinBox_8.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_8.setReadOnly(True)
        self.spinBox_8.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_8.setMaximum(1000000000)
        self.spinBox_8.setObjectName("spinBox_8")
        self.spinBox_9 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_9.setGeometry(QtCore.QRect(140, 300, 91, 20))
        self.spinBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_9.setReadOnly(True)
        self.spinBox_9.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_9.setMaximum(1000000000)
        self.spinBox_9.setObjectName("spinBox_9")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(20, 60, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(130, 60, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.spinBox_10 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_10.setGeometry(QtCore.QRect(160, 80, 51, 20))
        self.spinBox_10.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_10.setReadOnly(False)
        self.spinBox_10.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_10.setObjectName("spinBox_10")
        self.spinBox_11 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_11.setGeometry(QtCore.QRect(20, 80, 91, 20))
        self.spinBox_11.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_11.setReadOnly(False)
        self.spinBox_11.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_11.setMaximum(200000000)
        self.spinBox_11.setObjectName("spinBox_11")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.currentGamemode.setItemText(0, _translate("Dialog", "Extreme"))
        self.currentGamemode.setItemText(1, _translate("Dialog", "Legend"))
        self.currentGamemode.setItemText(2, _translate("Dialog", "Iron Man"))
        self.currentGamemode.setItemText(3, _translate("Dialog", "Immortal"))
        self.currentGamemode.setItemText(4, _translate("Dialog", "Hardcore Iron Man"))
        self.currentGamemode.setItemText(5, _translate("Dialog", "Grand Master"))
        self.currentGamemode.setItemText(6, _translate("Dialog", "Prestiged"))
        self.checkBox.setText(_translate("Dialog", "Double Xp?"))
        self.label.setText(_translate("Dialog", "Gamemode"))
        self.label_2.setText(_translate("Dialog", "Regular Bone"))
        self.label_3.setText(_translate("Dialog", "Bone Types"))
        self.label_4.setText(_translate("Dialog", "Bones Needed"))
        self.label_5.setText(_translate("Dialog", "Big Bone"))
        self.label_6.setText(_translate("Dialog", "Zogre Bone"))
        self.label_7.setText(_translate("Dialog", "Baby Dragon Bone"))
        self.label_8.setText(_translate("Dialog", "Dragon Bone"))
        self.label_9.setText(_translate("Dialog", "Dagannoth Bone"))
        self.label_10.setText(_translate("Dialog", "Frost Dragon Bone"))
        self.label_11.setText(_translate("Dialog", "Ourg Bone (Bork)"))
        self.label_12.setText(_translate("Dialog", "Ourg Bone (Bandos)"))
        self.label_13.setText(_translate("Dialog", "Current Xp"))
        self.label_14.setText(_translate("Dialog", "Wanted Level"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

