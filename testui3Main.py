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
            Dic_Level_Requirement = (0,0,83,174,276,388,512,650,801,969,1154,
                                     1358,1584,1833,2107,2411,2746,3115,3523,3973,4470,
                                     5018,5624,6292,7028,7842,8740,9730,10824,12031,13363,
                                     14833,16456,18247,20224,22406,24815,27473,30408,33648,27224,
                                     41171,45529,50339,55649,61512,67983,75127,83014,91721,101333,
                                     111945,123660,136594,150872,166636,184040,203254,224466,247886,273742,
                                     302288,333804,368599,407015,449428,496254,547953,605032,668051,737627,
                                     814445,899257,992895,1096278,1210421,1336443,1475581,1629200,1798808,1986068,
                                     2192818,2421087,2673114,2951373,3258594,3597792,3972294,4385776,4842295, 5346332,
                                     5902831,6517253,7195629,7944614,8771558,9684577,10692692,11805606,13034431)
            
            GameModes = {"Extreme":150,"Legend":50,"Iron Man":25, "Immortal":10, "Hardcore Iron Man":5, "Grand Master":2}
            
            Current_GameMode_Calc = CalcDialog.getCurrentGameMode(self, GameModes)
            New_GameMode_Calc = CalcDialog.getNewGameMode(self, GameModes)
            New_Xp = CalcDialog.getNewXP(self, GameModes)
            self.ui.calculatedXp.setText(str(New_Xp))
            Wanted_Level = int(self.ui.enteredLvlCompared.text())
            Dic_Level_Req = int(Dic_Level_Requirement[Wanted_Level])
            Till_Wanted_Level = int(((Dic_Level_Req - New_Xp) / New_GameMode_Calc) * Current_GameMode_Calc)
            self.ui.calculatedXpTill99.setText(str(Till_Wanted_Level))
        except:
            #Still need to add a pop-up message here
            print("An error has occurred")
    
    def getCurrentGameMode(self, GameModes):
        Current_GameMode = str(self.ui.currentGamemode.currentText())
        Current_GameMode_Calc = GameModes.get(Current_GameMode)
        return Current_GameMode_Calc
    
    def getNewGameMode(self, GameModes):
        New_GameMode = str(self.ui.newGamemode.currentText())
        New_GameMode_Calc = GameModes.get(New_GameMode)
        return New_GameMode_Calc
    
    def getNewXP(self, GameModes):
        Current_Xp = int(self.ui.currentXp.text())
        Current_GameMode_Calc = CalcDialog.getCurrentGameMode(self, GameModes)
        New_GameMode_Calc = CalcDialog.getNewGameMode(self, GameModes)
        New_Xp = int((Current_Xp / Current_GameMode_Calc)*New_GameMode_Calc)
        return New_Xp
    
if __name__ == '__main__':
    import sys
 
    app = QApplication(sys.argv)

    screen = CalcDialog()
    screen.show()
    
    sys.exit(app.exec_())
