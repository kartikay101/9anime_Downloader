import os
import sys
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)


	self.ql = QLabel("URL:")
        self.le = QLineEdit()
        self.le.setObjectName("URL")

	self.ql1 = QLabel("Name of Anime:")
        self.le1 = QLineEdit()
        self.le1.setObjectName("Name")

	self.ql2 = QLabel("Episodes(From):")
        self.le2 = QLineEdit()
        self.le2.setObjectName("Episodes")

	self.ql6 = QLabel("Episodes(Till):")
        self.le6 = QLineEdit()
        self.le6.setObjectName("Episodes")

	self.ql3 = QLabel("Season:")
        self.le3 = QLineEdit()
        self.le3.setObjectName("Season")

	self.ql4 = QLabel("Quality( 1:-360p  2:-480p  3:-720p  4:-1080p ):")
        self.le4 = QLineEdit()

        self.le4.setObjectName("Quality")

	self.ql5 = QLabel("Category:")
        self.le5 = QLineEdit()
        self.le5.setObjectName("Category")

	self.ql7 = QLabel("--::It requires RapidVideo Server to be available for downloading::--")
	self.ql9 = QLabel("--::This project is in development phase, giving absurd values will lead to errors::--")
	self.ql8 = QLabel("\n")

        self.pb = QPushButton()
        self.pb.setObjectName("Download")
        self.pb.setText("Download") 

        layout = QFormLayout()


        layout.addWidget(self.ql1)
        layout.addWidget(self.le1)

        layout.addWidget(self.ql)
        layout.addWidget(self.le)

        layout.addWidget(self.ql3)
        layout.addWidget(self.le3)

        layout.addWidget(self.ql2)
        layout.addWidget(self.le2)

        layout.addWidget(self.ql6)
        layout.addWidget(self.le6)

        layout.addWidget(self.ql4)
        layout.addWidget(self.le4)

        layout.addWidget(self.ql5)
        layout.addWidget(self.le5)

        layout.addWidget(self.ql7)
        layout.addWidget(self.ql9)
        layout.addWidget(self.ql8)

        layout.addWidget(self.pb)

        self.setLayout(layout)
        self.connect(self.pb, SIGNAL("clicked()"),self.button_click)
        self.setWindowTitle("Anime Downloader")

    def button_click(self):
        # shost is a QString object
        url = self.le.text()
	anime = self.le1.text()
	episodes1 = self.le2.text()
	episodes2 = self.le6.text()
	season = self.le3.text()
	quality = self.le4.text()
	category = self.le5.text()

app = QApplication(sys.argv)
form = Form()
form.resize(1000,500)
form.show()
app.exec_()

filepath=os.path.realpath(__file__)
filepath=filepath.replace('/src/anime_downloader.py','/res/')
fo = open(filepath + 'config.cfg','w')
fo.write(category + '\n')
fo1 = open(filepath + 'links.txt','w')
fo1.write(anime + '\n' + season + '\n' + episodes1 +'\n')
fo2 = open(filepath + 'data.txt','w')
fo2.write(url + '\n' + quality + '\n' + episodes1 + '\n' + episodes2 + '\n')
fo.close()
fo.close1()
fo.close2()


