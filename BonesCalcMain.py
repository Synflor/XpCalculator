from PyQt5.QtWidgets import QDialog, QApplication
from BonesCalc import Ui_Dialog

dic_level_requirement = (0, 0, 83, 174, 276, 388, 512, 650, 801, 969, 1154,
                                     1358, 1584, 1833, 2107, 2411, 2746, 3115, 3523, 3973, 4470,
                                     5018, 5624, 6292, 7028, 7842, 8740, 9730, 10824, 12031, 13363,
                                     14833, 16456, 18247, 20224, 22406, 24815, 27473, 30408, 33648, 27224,
                                     41171, 45529, 50339, 55649, 61512, 67983, 75127, 83014, 91721, 101333,
                                     111945, 123660, 136594, 150872, 166636, 184040, 203254, 224466, 247886, 273742,
                                     302288, 333804, 368599, 407015, 449428, 496254, 547953, 605032, 668051, 737627,
                                     814445, 899257, 992895, 1096278, 1210421, 1336443, 1475581, 1629200, 1798808,
                                     1986068,
                                     2192818, 2421087, 2673114, 2951373, 3258594, 3597792, 3972294, 4385776, 4842295,
                                     5346332,
                                     5902831, 6517253, 7195629, 7944614, 8771558, 9684577, 10692692, 11805606, 13034431)

game_modes = {"Extreme": 150, "Legend": 50, "Iron Man": 25, "Immortal": 10, "Hardcore Iron Man": 5,
                          "Grand Master": 2, "Prestiged": 5}



class CalcDialog(QDialog):
    def __init__(self):
        super(CalcDialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted(self.calculate())
        self.ui.buttonBox.rejected()

    def calculate(self):
        try:
            game_mode_calc = CalcDialog.getGameMode(self, game_modes)

            wanted_level = self.ui.enteredLvl.value()
            dic_level_req = int(dic_level_requirement[wanted_level])

            current_xp = int(self.ui.currentXp.value())
            current_level = min(range(len(dic_level_requirement)),
                                key=lambda i: abs(dic_level_requirement[i] - current_xp))
            self.ui.currentLevel.setValue(current_level)

            new_level = min(range(len(dic_level_requirement)), key=lambda i: abs(dic_level_requirement[i] - new_xp))
            self.ui.calculatedLevel.setValue(new_level)
        except:
            # Still need to add a pop-up message here
            print("An error has occurred")

    def getCurrentGameMode(self, gamesmodes):
        current_game_mode = str(self.ui.currentGamemode.currentText())
        current_game_mode_calc = gamesmodes.get(current_game_mode)
        return current_game_mode_calc

    def getNewGameMode(self, gamemodes):
        new_game_mode = str(self.ui.newGamemode.currentText())
        new_game_mode__calc = gamemodes.get(new_game_mode)
        return new_game_mode__calc

    def getNewXP(self, GameModes):
        current_xp = int(self.ui.currentXp.value())
        current_game_mode_calc = CalcDialog.getCurrentGameMode(self, GameModes)
        new_game_mode_calc = CalcDialog.getNewGameMode(self, GameModes)
        new_xp = int((current_xp / current_game_mode_calc) * new_game_mode_calc)
        return new_xp


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = CalcDialog()
    screen.show()

    sys.exit(app.exec_())