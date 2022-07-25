import imp
import sys

from matplotlib.pyplot import connect
import Ui_Dictool0
import Ui_Dictool1
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
 
class mywd1(QWidget,Ui_Dictool0.MainWindow):
    def __init__(self):
        QWidget.__init__(self)
        Ui_Dictool0.MainWindow.__init__(self)
        self.setupUi(self)
          
    def read_ct(self):
        x = self.chapter
        y = self.test
        return (x,y)

class mywd2(QWidget,Ui_Dictool1.ChildWindow1):
    def __init__(self):
        QWidget.__init__(self)
        Ui_Dictool1.ChildWindow1.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.onButtonClick)
          
    def onButtonClick(self):
        my_text = self.textEdit.toPlainText()
        self.textEdit.append("over")
        print(my_text)
        
 
if __name__=='__main__':
    app=QApplication(sys.argv)
    
    wd1 = mywd1()
    wd2 = mywd2()
    
    ch,te = wd1.read_ct()
    print(ch,te)
    btn1 = wd1.pushButton
    btn1.clicked.connect(wd2.show)
    
    wd1.show()
    sys.exit(app.exec_())