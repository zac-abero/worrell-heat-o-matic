# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
import time
from PySide6 import QtCore, QtWidgets, QtGui
from Connect import tec_controller 

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(600, 450)
        self.gridLayoutWidget = QWidget(Main)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 310, 561, 121))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.end_button = QPushButton(self.gridLayoutWidget)
        self.end_button.setObjectName(u"end_button")

        self.gridLayout.addWidget(self.end_button, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.start_button = QPushButton(self.gridLayoutWidget)
        self.start_button.setObjectName(u"start_button")

        self.gridLayout.addWidget(self.start_button, 0, 1, 1, 1)

        self.pause_button = QPushButton(self.gridLayoutWidget)
        self.pause_button.setObjectName(u"pause_button")

        self.gridLayout.addWidget(self.pause_button, 1, 1, 1, 1)

        self.verticalLayoutWidget = QWidget(Main)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 321, 151))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.ch1temp = QLineEdit(self.verticalLayoutWidget)
        self.ch1temp.setObjectName(u"ch1temp")

        self.horizontalLayout_4.addWidget(self.ch1temp)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.ch2temp = QLineEdit(self.verticalLayoutWidget)
        self.ch2temp.setObjectName(u"ch2temp")

        self.horizontalLayout_5.addWidget(self.ch2temp)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Main)
        
        self.start_button.clicked.connect(self.start)
        self.pause_button.clicked.connect(self.pause)
        self.end_button.clicked.connect(self.end)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Dialog", None))
        self.end_button.setText(QCoreApplication.translate("Main", u"End program", None))
        self.start_button.setText(QCoreApplication.translate("Main", u"Start", None))
        self.pause_button.setText(QCoreApplication.translate("Main", u"Pause", None))
        self.label_4.setText(QCoreApplication.translate("Main", u"Channel 1 Temperature", None))
        self.label_5.setText(QCoreApplication.translate("Main", u"Channel 2 Temperature", None))
    # retranslateUi


# extra functions

# Start function
    @QtCore.Slot()
    def start(self):
        
        # Error handling for text box inputs
        try:
            
            # Attempts to get each float value of input (temperatures, C)
            temp1123_ch1 = float(self.ch1temp.text())
            temp1123_ch2 = float(self.ch2temp.text())
            
            # check if numbers are valid, and within the range of 20C -> 200C
            if (temp1123_ch1 and temp1123_ch2) and (20 < temp1123_ch1 < 200) and (20 < temp1123_ch2 < 200):
                print("Temperatures received, starting ramp. TEC1123: %s, TEC1090: %s" % (temp1123_ch1, temp1123_ch2))
        
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
        self.ch1temp.setReadOnly(True)
        self.ch2temp.setReadOnly(True)
        
        # query which device is connected to which id
        device1 = connection.get_device_type(1)
        
        connection.set_temp(temp1123_ch1, 1)
        
        connection.set_enable(1, True)
        
        # 5 second buffer applied to adjust 
        
        QtCore.QTimer.singleShot(5000, lambda: self.start_button.setText("Ramp in progress"))
        
# Pause Function -- Currently only turns off controller without exiting. Adapt this to get() the controller temps and hold it
    def pause(self):
        QtCore.QTimer.singleShot(5000, lambda: self.pause_button.setText("Pausing.."))
        self.sleep_button()
        if connect:
            print(connection.set_enable(1, False))
        print("Pausing ramp..")
        self.pause_button.setText("Pause Ramp")

        
# End Function
    def end(self):
        self.end_button.setText("Ending Ramp..")
        
        try: 
            print(connection.set_enable(1, False))
            print("Ending ramp..")
            QApplication.exit()
        except ConnectionError:
            print("Could not connect to device!")


# adapt this to input button names rather than target end button.
    def sleep_button(self):
        self.end_button.setEnabled(False)
        QtCore.QTimer.singleShot(5000, lambda: self.end_button.setDisabled(False))
        
# instantiate a connection with the TECS (comment this out for GUI testing)
#connection = tec_controller() 
