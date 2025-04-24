# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bootmenu.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtCore, QtWidgets, QtGui

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 120, 241, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        
        self.radioRegularMode = QRadioButton(self.verticalLayoutWidget)
        self.radioRegularMode.setObjectName(u"radioRegularMode", )

        self.verticalLayout.addWidget(self.radioRegularMode)

        self.radioTestingMode = QRadioButton(self.verticalLayoutWidget)
        self.radioTestingMode.setObjectName(u"radioTestingMode")

        self.verticalLayout.addWidget(self.radioTestingMode)
        
        self.radioRegularMode.setChecked(True)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 281, 91))
        self.label.setWordWrap(True)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        
        self.radioTestingMode.toggled.connect(Dialog.boot_test)
        self.radioRegularMode.toggled.connect(Dialog.boot_regular)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.radioRegularMode.setText(QCoreApplication.translate("Dialog", u"Boot regularly (Device Connected)", None))
        self.radioTestingMode.setText(QCoreApplication.translate("Dialog", u"Boot in Testing Mode (For UI purposes)", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Hello! Welcome to the Heat-o-matic boot menu, please select which mode you would like to run.", None))
    # retranslateUi

    