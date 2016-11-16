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
            Dic_Level_Requirement = (0,0,83,174,276,388,512,650,801,969,1154,1358,1584,1833,2107,2411,2746,3115,3523,3973,4470)
            Current_GameMode = str(self.ui.currentGamemode.currentText())
            Current_GameMode_Calc = GameModes.get(Current_GameMode)
            New_GameMode = str(self.ui.newGamemode.currentText())
            New_GameMode_Calc = GameModes.get(New_GameMode)
            Current_Xp = int(self.ui.currentXp.text())
            New_Xp = int((Current_Xp / Current_GameMode_Calc)*New_GameMode_Calc)
            self.ui.calculatedXp.setText(str(New_Xp))
            CalcDialog.calculateRemainingXP(self)
            Wanted_Level = int(self.ui.enteredLvlCompared.text())
            Dic_Level_Req = int(Dic_Level_Requirement[Wanted_Level])
            Till_Wanted_Level = int(((Dic_Level_Req - New_Xp) / New_GameMode_Calc) * Current_GameMode_Calc)
            self.ui.calculatedXpTill99.setText(str(Till_Wanted_Level))
        except:
            #Still need to add a pop-up message here
            print("An error has occurred")
    
    def calculateRemainingXP(self):
        GameModes = {"Extreme":150,"Legend":50,"Iron Man":25, "Immortal":10, "Hardcore Iron Man":5, "Grand Master":2}
        Current_GameMode = str(self.ui.currentGamemode.currentText())
        Current_GameMode_Calc = GameModes.get(Current_GameMode)
        New_GameMode = str(self.ui.newGamemode.currentText())
        New_GameMode_Calc = GameModes.get(New_GameMode)
        Current_Xp = int(self.ui.currentXp.text())
        New_Xp = int((Current_Xp / Current_GameMode_Calc)*New_GameMode_Calc)
        

        
if __name__ == '__main__':
    import sys
 
    app = QApplication(sys.argv)

    screen = CalcDialog()
    screen.show()
    
    sys.exit(app.exec_())
