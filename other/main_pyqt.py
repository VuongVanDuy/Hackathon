from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSlider
from PyQt5.QtCore import Qt
import sys
import os

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        
        self.setupUI()
        self.btn1.clicked.connect(lambda: self.showRoute('./route_map1.html'))
        self.btn2.clicked.connect(lambda: self.showRoute('./route_map2.html'))
        self.btn3.clicked.connect(lambda: self.showRoute('./route_map3.html'))

    def setupUI(self):
        self.view = QWebEngineView()

        html_file = './route_map1.html'
        url = QUrl.fromLocalFile(os.path.realpath(html_file))
        self.view.load(url)
        
        layout = QVBoxLayout()
        layoutbtn = QHBoxLayout()
        self.btn1 = QPushButton("1062")
        self.btn2 = QPushButton("1064")
        self.btn3 = QPushButton("1065")
        layoutbtns = QHBoxLayout()
        self.btns = []
        for i in range(5):
            btn = QPushButton("☆")
            btn.setStyleSheet("font-size: 20px;")
            btn.clicked.connect(self.setRating)
            #btn.setAlignment(Qt.AlignCenter)
            self.btns.append(btn)
            layoutbtns.addWidget(btn)
        self.label = QLabel("Average Rating: 0.0")  
        self.btn1.setStyleSheet("background-color: #4CAF50; color: #fff;")
        self.btn2.setStyleSheet("background-color: #4CAF50; color: #fff;")
        self.btn3.setStyleSheet("background-color: #4CAF50; color: #fff;")
        layoutbtn.addWidget(self.btn1)
        layoutbtn.addWidget(self.btn2)
        layoutbtn.addWidget(self.btn3)
        layout.addWidget(self.view)
        layout.addLayout(layoutbtn)
        layout.addLayout(layoutbtns)
        layout.addWidget(self.label)
        #layout.addWidget(self.slider)
        # Đặt QVBoxLayout làm layout cho widget
        self.setLayout(layout)
    
    def setRating(self):
        button = self.sender()
        for i in range(5):
            if self.btns[i] == button:
                for j in range(i+1):
                    self.btns[j].setText("★")
                for j in range(i+1, 5):
                    self.btns[j].setText("☆")
        
                self.label.setText(f"Average Rating: {i+1}.0")
        
           
    def showRoute(self, html_file):
        url = QUrl.fromLocalFile(os.path.realpath(html_file))
        self.view.load(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    app.exec_()       
