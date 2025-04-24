from PySide6 import QtWidgets
from bootmenu import Ui_Dialog
from qtui import Ui_Main


global_testMode = False
        
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_Main()
        self.ui.setupUi(self)

class BootWindow(QtWidgets.QMainWindow):    
    def __init__(self):
        super().__init__() 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    
    def accept(self):
        print("'Ok' Clicked")
        main_window.show()
        self.hide()
        
    def reject(self):
        QtWidgets.QApplication.exit()
        print("'Cancel' Clicked")
        
    def boot_test(self):
        global_testMode = True
        print("'Test Mode' selected")
        
    def boot_regular(self):
        global_testMode = False
        print("'Regular Mode' selected")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    boot_window = BootWindow()
    boot_window.show()
    
    main_window = MainWindow()
    main_window.hide()
        
    print("oing")
    
    app.exec()