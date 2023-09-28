from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QVBoxLayout,QWidget,QHBoxLayout
import sys
from PyQt5.QtGui import QPainter,QColor
class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    # def paintEvent(self,event):
    #     qp = QPainter()
    #     qp.begin(self)
    #     qp.setBrush(QColor(255,255,255))
    #     qp.setPen(QColor(255,255,255))
    #     qp.drawRect(0,0,800,600)
    #     qp.end()
    def initUI(self):

        self.setGeometry(0,0,800,600)
        self.setWindowTitle('Sayi Tahmin')

        oyun_secme_ekrani_button1 = QPushButton('Insan vs Insan')
        oyun_secme_ekrani_button2 = QPushButton('Insan vs Bilgisayar')
        oyun_secme_ekrani_button1.setFixedWidth(300)
        oyun_secme_ekrani_button2.setFixedWidth(300)

        widget = QWidget()
        self.setCentralWidget(widget)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(oyun_secme_ekrani_button1)
        hbox.addStretch()

        hbox2 = QHBoxLayout()
        hbox2.addStretch()
        hbox2.addWidget(oyun_secme_ekrani_button2)
        hbox2.addStretch()

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addStretch()
        
        vbox.addLayout(hbox)
        vbox.addStretch()
        vbox.addLayout(hbox2)

        vbox.addStretch()
        vbox.addStretch()

        widget.setLayout(vbox)
        
        oyun_secme_ekrani_button1.clicked.connect(self.secim_ekrani_button1_clicked)
    def secim_ekrani_button1_clicked(self):
        
        oyuncu1 = input('oyunucu1 in adini giriniz: ')
        oyuncu2 = input('oyunucu2 nin adini giriniz:')

        oyuncu1_sifre = input(f'{oyuncu1} sifreni gir: ')
        oyuncu2_sifre = input(f'{oyuncu2} sifreni gir: ')
       
app = QApplication(sys.argv)
win = Win()
win.show()
sys.exit(app.exec())