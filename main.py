from operator import truediv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random
MY_GUESS = random.randint(1,101)
print(MY_GUESS)

#...Variables...#
counts = 6
attempts = 6
no_of_guesses = False
count = 1

#.... import ui ....#
from guess_number import Ui_MainWindow

#.... base class....#
class RootMain(QMainWindow):
    

    #... Set Ui ...#
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #... Window Settings ...#
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


        #.... Btn Connect ....#
        self.ui.pushButton.clicked.connect(self.Geuss)


        #... Show ...#
        self.show()


    #.... Move window with Mouse ....#
    def mousePressEvent(self , evt):
        self.oldpos = evt.globalPos()
    
    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldpos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldpos = evt.globalPos()

    #.... Base Code of Guess num ....#
    def Geuss (self):
        global counts , attempts , no_of_guesses , count
        guess = int( self.ui.lineEdit.text())
        if count < counts :
            if guess == MY_GUESS :
                self.ui.label_4.setText( f"True Number : {MY_GUESS}")
                no_of_guesses = True
            elif guess < MY_GUESS:
                self.ui.label_4.setText( "your num is smaller")
                count += 1
                attempts -= 1
                self.ui.label_3.setText(f"You have {attempts} attempts remaining")
            elif guess > MY_GUESS:
                self.ui.label_4.setText( "your num is biger")
                count += 1
                attempts -= 1
            self.ui.label_3.setText(f"You have {attempts} attempts remaining")
        
        else:
            self.ui.label_3.setText("end!")
                

            
         


#.... main file condition ....#

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    root = RootMain()
    sys.exit(app.exec_())