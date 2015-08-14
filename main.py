import sys
import smtplib  # Simple Mail Transfer Protocol - za slanje mejlova
from PyQt4 import QtCore, QtGui
from Notifier_Main import Ui_Notifier_Main_GUI

class MainGUI(QtGui.QWidget, Ui_Notifier_Main_GUI):
    # unutar init metode MainGUI-a prvo se poziva init metoda parent klase QtGui.QWidget
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.sendButton.clicked.connect(self.send)

    def send(self):
        fromaddr = self.senderEmailLineEdit.text()
        toaddrs  = self.receiverEmailLineEdit.text()
        msg = self.msgTextEdit.toPlainText()
        username = self.senderEmailLineEdit.text()
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(str(username), 'pass') # Aplikacijska sifra
        server.sendmail(str(fromaddr), str(toaddrs), str(msg))
        server.quit()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_gui = MainGUI()
    main_gui.show()
sys.exit(app.exec_())
