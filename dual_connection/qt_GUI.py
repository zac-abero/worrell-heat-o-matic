import sys
import random
import time
from PySide6 import QtCore, QtWidgets, QtGui
from Connect import tec_controller 

# Will later be using Qt Designer to make better UI, just adjusting this for testing purposes now.

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Establishing Buttons/boxes
        self.tec_1123_text = QtWidgets.QLabel("Temperature 1123 (°C):",
                                     alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.tec_1123_temp = QtWidgets.QLineEdit(
                                     alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        
        self.tec_1090_text = QtWidgets.QLabel("Temperature 1090 (°C):",
                                     alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)   
        self.tec_1090_temp = QtWidgets.QLineEdit(
                                     alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.start_button = QtWidgets.QPushButton("Start Ramp")
        self.pause_button = QtWidgets.QPushButton("Pause Ramp")
        self.end_button = QtWidgets.QPushButton("End Ramp")  
    
        # Starting box layout
        self.layout = QtWidgets.QVBoxLayout(self)
        
        # Implementing widgets
        self.layout.addWidget(self.tec_1123_text)
        self.layout.addWidget(self.tec_1123_temp)
        
        self.layout.addWidget(self.tec_1090_text)
        self.layout.addWidget(self.tec_1090_temp)
        
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.pause_button)
        self.layout.addWidget(self.end_button)
        
        self.start_button.clicked.connect(self.start)
        self.pause_button.clicked.connect(self.pause)
        self.end_button.clicked.connect(self.end)

# Start function
    @QtCore.Slot()
    def start(self):
        
        # Error handling for text box inputs
        try:
            
            # Attempts to get each float value of input (temperatures, C)
            temp1123 = float(self.tec_1123_temp.text())
            temp1090 = float(self.tec_1090_temp.text())
            
            # check if numbers are valid, and within the range of 20C -> 200C
            if (temp1123 and temp1090) and (20 < temp1123 < 200) and (20 < temp1090 < 200):
                print("Temperatures received, starting ramp. TEC1123: %s, TEC1090: %s" % (temp1123, temp1090))
        
        except ValueError: 
            # throws this error when no input or non-numerical values 
            print("Improper input was added. Please retry with numerical values only!")
            return 
        except :
            # real broken shit fr idk what you did if you got this message
            print("error: you broke some shit fr")
            return 
        
        self.start_button.setText("Starting Ramp..")
        self.sleep_button()
        

        # locks out temp boxes therefore no edits can be made until pausing/ending ramp
        self.tec_1123_temp.setReadOnly(True)
        self.tec_1090_temp.setReadOnly(True)
        
        # query which device is connected to which id
        device1 = connection.get_device_type(1)
        device2 = connection.get_device_type(2)
        
        if device1== 1123:
            connection.set_temp(temp1123, 1)
            connection.set_temp(temp1090, 2) 
        else:
            connection.set_temp(temp1090, 1)
            connection.set_temp(temp1123, 2)
        
        connection.set_enable(1, True)
        connection.set_enable(2, True) 
        
        # 5 second buffer applied to adjust 
        
        QtCore.QTimer.singleShot(5000, lambda: self.start_button.setText("Ramp in progress"))
        
# Pause Function -- Currently only turns off controller without exiting. Adapt this to get() the controller temps and hold it
    def pause(self):
        QtCore.QTimer.singleShot(5000, lambda: self.pause_button.setText("Pausing.."))
        self.sleep_button()

        print(connection.set_enable(1, False))
        print(connection.set_enable(2, False))
        print("Pausing ramp..")
        self.end_button.setText("Pause Ramp")

        
# End Function
    def end(self):
        self.end_button.setText("Ending Ramp..")
        print(connection.set_enable(1, False))
        print(connection.set_enable(2, False))
        print("Ending ramp..")
        sys.exit(app.exec())


# adapt this to input button names rather than target end button.
    def sleep_button(self):
        self.end_button.setEnabled(False)
        QtCore.QTimer.singleShot(5000, lambda: self.end_button.setDisabled(False))
        
# instantiate a connection with the TECS (comment this out for GUI testing)
connection = tec_controller() 

# GUI Main
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    ramp_gui = GUI()
    ramp_gui.resize(400, 400)
    ramp_gui.show()

    sys.exit(app.exec())
    
    
