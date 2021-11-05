import sys
from PyQt5 import QtWidgets
from qt_file_with_bar import Ui_Ratespiel
app = QtWidgets.QApplication(sys.argv)
Ratespiel = QtWidgets.QMainWindow()
ui = Ui_Ratespiel()
ui.setupUi(Ratespiel)
Ratespiel.show()
sys.exit(app.exec_())