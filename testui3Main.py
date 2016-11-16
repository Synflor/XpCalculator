from PyQt5.QtWidgets import QDialog, QApplication
from testgui3 import Ui_Dialog

class CalcDialog(QDialog):
    def __init__(self):
        super(CalcDialog, self).__init__()
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.calculateButton.clicked.connect(self.calculate)
        
    def calculate(self):
        try:
            GameModes = {"Extreme":150,"Legend":50,"Iron Man":25, "Immortal":10, "Hardcore Iron Man":5, "Grand Master":2}
            Current_GameMode = str(self.ui.currentGamemode.currentText())
            Current_GameMode_Calc = GameModes.get(Current_GameMode)
            New_GameMode = str(self.ui.newGamemode.currentText())
            New_GameMode_Calc = GameModes.get(New_GameMode)
            Current_Xp = int(self.ui.currentXp.text())
            New_Xp = int((Current_Xp / Current_GameMode_Calc)*New_GameMode_Calc)
            self.ui.calculatedXp.setText(str(New_Xp))
        except:
            print("An error has occurred")
            print("TEST here")
			
if __name__ == '__main__':
    import sys
 
    app = QApplication(sys.argv)

    screen = CalcDialog()
    screen.show()
    
    sys.exit(app.exec_())