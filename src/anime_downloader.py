# @Author: Deepanshu Maini <mainidishu>
# @Date:   2018-07-22T23:12:26+05:30
# @Last modified by:   deepanshu
# @Last modified time: 2018-07-23T22:47:46+05:30



import os
import sys
import subprocess
from time import sleep
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import (QMainWindow, QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout, QWidget, QSound)
from PyQt4.QtGui import QSound

class Form(QDialog):

    def __init__(self, parent = None):
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
        self.ql10 = QLabel("--::To exit program completely please exit UGet as well as the application window::--")
        self.ql11 = QLabel("--::For any issues raise the issue on GitHub (linl in READ.md)::--")
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
        layout.addWidget(self.ql10)
        layout.addWidget(self.ql11)
        layout.addWidget(self.ql8)

        layout.addWidget(self.pb)

        self.setLayout(layout)
        self.connect(self.pb, SIGNAL("clicked()"),self.button_click)


        self.setWindowTitle("Anime Downloader")

    def button_click(self):

        url = self.le.text()
        anime = self.le1.text()
        episodes1 = self.le2.text()
        episodes2 = self.le6.text()
        season = self.le3.text()
        quality = self.le4.text()
        category = self.le5.text()

        self.le.hide()
        self.le1.hide()
        self.le2.hide()
        self.le3.hide()
        self.le4.hide()
        self.le5.hide()
        self.ql1.hide()
        self.ql2.hide()
        self.ql3.hide()
        self.ql4.hide()
        self.ql5.hide()
        self.ql6.hide()
        self.ql7.hide()
        self.ql8.hide()
        self.ql9.hide()
        self.ql10.hide()
        self.ql11.hide()
        self.ql.hide()
        self.pb.hide()
        self.le6.hide()

        filepath = os.path.realpath(__file__)
        filepath = filepath.replace('/src/anime_downloader.py','/res/')
        fo = open(filepath + 'config.cfg','w')
        fo.write(category + '\n')
        fo.close()
        fo1 = open(filepath + 'links.txt','w')
        fo1.write(anime + '\n' + season + '\n' + episodes1 +'\n')
        fo1.close()
        fo2 = open(filepath + 'data.txt','w')
        fo2.write(url + '\n' + quality + '\n' + episodes1 + '\n' + episodes2 + '\n')
        fo2.close()
        filepath1 = filepath.replace('/res/','/src/')
        subprocess.call(['python','populate_links.py'])
        subprocess.call(['python','download_script.py'])
        self.setStyleSheet("border-image: url(2830378.jpg); background-repeat: no-repeat;")


app = QApplication(sys.argv)
form = Form()
form.resize(1000,500)
form.show()
sys.exit(app.exec_())
