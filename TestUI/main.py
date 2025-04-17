from PySide6 import QtWidgets
from qtui import Ui_Main


# class MainWindow(QtWidgets.QMainWindow):
#     def __init(self):
#         QtWidgets.QMainWindow.__init__(self)
#         self.ui = Ui_Main()
#         self.ui.setupUi(self)
        
        
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() #alteration was to add super().init() for calling itself
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()
    app.exec()
    