# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

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
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalLayoutWidget = QWidget(Main)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 60, 321, 101))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_5.addWidget(self.lineEdit_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Main", u"Start Ramp", None))
        self.pushButton_2.setText(QCoreApplication.translate("Main", u"Pause", None))
        self.pushButton_3.setText(QCoreApplication.translate("Main", u"End Ramp", None))
        self.label_4.setText(QCoreApplication.translate("Main", u"Channel 1 Temperature", None))
        self.label_5.setText(QCoreApplication.translate("Main", u"Channel 2 Temperature", None))
    # retranslateUi

if __name__ == "__main__":
    app = Ui_Main()

    ramp_gui = Ui_Main()
    app.exec()
    