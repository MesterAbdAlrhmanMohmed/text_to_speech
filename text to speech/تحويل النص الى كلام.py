from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import gtts
import os
import langdetect
if not os.path.exists("data"):
        os.makedirs("data")
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("تحويل النص الى كلام")
        self.إظهار=qt.QLabel("أكتب النص هنا")
        self.الكتابة=qt.QLineEdit()
        self.الكتابة.setAccessibleName("أكتب النص هنا")
        self.تحويل=qt.QPushButton("تحويل النص الى كلام")
        self.تحويل.setDefault(True)
        self.تحويل.clicked.connect(self.listen)
        l=qt.QVBoxLayout()        
        l.addWidget(self.إظهار)
        l.addWidget(self.الكتابة)
        l.addWidget(self.تحويل)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)        
    def listen(self):
        try:
            النص=self.الكتابة.text()
            lang=langdetect.detect(النص)
            result=gtts.gTTS(النص,lang=lang)
            result.save("data/message.mp3")
            os.startfile(os.getcwd()+"/data/message.mp3")
        except:
            qt.QMessageBox.information(self,"تنبيه","عفوا, يرجى إدخال نص أو التأكد من الإتصال بالإنترنت")
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()