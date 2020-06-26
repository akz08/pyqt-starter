import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWinExtras import QtWin

# todo: replace with your own app id
appid = 'mycompany.myproduct.subproduct.version'
QtWin.setCurrentProcessExplicitAppUserModelID(appid)    

class HelloWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialiseUI()

    def initialiseUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Empty PyQt window')
        self.displayLabels()

        self.show()

    def displayLabels(self):
        text = QLabel(self)
        text.setText('Hello World')
        text.move(85, 140)
        text.setFont(QFont('Arial', 20))

if __name__ == '__main__':
    # app = QApplication(sys.argv) # if we expect to get arguments
    app = QApplication([])
    app.setWindowIcon(QIcon('icons/app.ico'))
    mainWin = HelloWindow()
    sys.exit( app.exec_() )