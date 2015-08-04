# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Notifier_Main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Notifier_Main_GUI(object):
    def setupUi(self, Notifier_Main_GUI):
        Notifier_Main_GUI.setObjectName(_fromUtf8("Notifier_Main_GUI"))
        Notifier_Main_GUI.resize(477, 341)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Notifier_Main_GUI.sizePolicy().hasHeightForWidth())
        Notifier_Main_GUI.setSizePolicy(sizePolicy)
        Notifier_Main_GUI.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Notifier_Main_GUI.setMouseTracking(False)
        Notifier_Main_GUI.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout = QtGui.QGridLayout(Notifier_Main_GUI)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.senderEmailLabel = QtGui.QLabel(Notifier_Main_GUI)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.senderEmailLabel.setFont(font)
        self.senderEmailLabel.setObjectName(_fromUtf8("senderEmailLabel"))
        self.gridLayout.addWidget(self.senderEmailLabel, 1, 1, 1, 3)
        spacerItem1 = QtGui.QSpacerItem(49, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.senderEmailLineEdit = QtGui.QLineEdit(Notifier_Main_GUI)
        self.senderEmailLineEdit.setObjectName(_fromUtf8("senderEmailLineEdit"))
        self.gridLayout.addWidget(self.senderEmailLineEdit, 2, 1, 1, 4)
        self.receiverEmailLabel = QtGui.QLabel(Notifier_Main_GUI)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.receiverEmailLabel.setFont(font)
        self.receiverEmailLabel.setObjectName(_fromUtf8("receiverEmailLabel"))
        self.gridLayout.addWidget(self.receiverEmailLabel, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(49, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 0, 1, 1)
        self.receiverEmailLineEdit = QtGui.QLineEdit(Notifier_Main_GUI)
        self.receiverEmailLineEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.receiverEmailLineEdit.setObjectName(_fromUtf8("receiverEmailLineEdit"))
        self.gridLayout.addWidget(self.receiverEmailLineEdit, 4, 1, 1, 4)
        spacerItem4 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 5, 1, 1, 2)
        self.msgLabel = QtGui.QLabel(Notifier_Main_GUI)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.msgLabel.setFont(font)
        self.msgLabel.setObjectName(_fromUtf8("msgLabel"))
        self.gridLayout.addWidget(self.msgLabel, 6, 1, 1, 2)
        spacerItem5 = QtGui.QSpacerItem(49, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 7, 0, 1, 1)
        self.msgTextEdit = QtGui.QTextEdit(Notifier_Main_GUI)
        self.msgTextEdit.setObjectName(_fromUtf8("msgTextEdit"))
        self.gridLayout.addWidget(self.msgTextEdit, 7, 1, 1, 4)
        spacerItem6 = QtGui.QSpacerItem(48, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 7, 5, 1, 1)
        self.sendButton = QtGui.QPushButton(Notifier_Main_GUI)
        self.sendButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("E:/Python Projekti/Notifier/ico/1437486690_gmail_C.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendButton.setIcon(icon)
        self.sendButton.setIconSize(QtCore.QSize(60, 60))
        self.sendButton.setFlat(True)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.gridLayout.addWidget(self.sendButton, 7, 6, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(49, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 7, 7, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 8, 4, 1, 1)

        self.retranslateUi(Notifier_Main_GUI)
        QtCore.QMetaObject.connectSlotsByName(Notifier_Main_GUI)

    def retranslateUi(self, Notifier_Main_GUI):
        Notifier_Main_GUI.setWindowTitle(_translate("Notifier_Main_GUI", "Notifier", None))
        self.senderEmailLabel.setText(_translate("Notifier_Main_GUI", "Sender email:", None))
        self.receiverEmailLabel.setText(_translate("Notifier_Main_GUI", "Receiver email:", None))
        self.msgLabel.setText(_translate("Notifier_Main_GUI", "Message:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Notifier_Main_GUI = QtGui.QWidget()
    ui = Ui_Notifier_Main_GUI()
    ui.setupUi(Notifier_Main_GUI)
    Notifier_Main_GUI.show()
    sys.exit(app.exec_())

