from PySide6 import QtWidgets
from bootmenu import Ui_Dialog
from qtui import Ui_Main


# class MainWindow(QtWidgets.QMainWindow):
#     def __init(self):
#         QtWidgets.QMainWindow.__init__(self)
#         self.ui = Ui_Main()
#         self.ui.setupUi(self)
        
        
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()
    app.exec()



class BootWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = BootWindow()
    window.show()
    app.exec()