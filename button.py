from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QPainter, QPen

class CustomWidget(QWidget):
    def __init__(self, list_stops):
        super().__init__()
        self.list_stops = list_stops
        self.buttons = []
        self.nameAddr = []
        self.main_layout = QVBoxLayout(self)
        self.create_buttons()
    
    def create_buttons(self):
        # Create buttons and add them to the layout
        for i in range(len(self.list_stops)):
            self.widget = QWidget()
            layout_widget = QHBoxLayout(self.widget)
            button = QPushButton(self)
            layout_widget.addWidget(button)
            label = QLabel(self.list_stops[i])
            label.setStyleSheet("font-size: 14px")
            layout_widget.addWidget(label)

            self.widget.setLayout(layout_widget)
            button.setFixedSize(16, 16)  # Set a fixed size for the buttons
            button.setStyleSheet(self.get_button_style(i == 0))  # Style buttons, highlight the middle one
            self.main_layout.addWidget(self.widget)
            self.buttons.append(button)
            self.nameAddr.append(label)
        self.main_layout.addStretch()  # Add stretch to center the buttons

    def get_button_style(self, highlight=False):
        base_style = """
            QPushButton {
                background-color: #cccccc;
                border: 2px solid #666666;
                border-radius: 8px;
            }
            QPushButton:pressed {
                background-color: #aaaaaa;
            }
        """
        highlight_style = """
            QPushButton {
                background-color: #009688;
                border: 2px solid #666666;
                border-radius: 8px;
            }
            QPushButton:pressed {
                background-color: #00796b;
            }
            QPushButton:hover {
                background-color: #4db6ac;
            }
        """
        return highlight_style if highlight else base_style

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.gray, 2, Qt.SolidLine)
        painter.setPen(pen)

        for i in range(len(self.buttons) - 1):
            btn1 = self.buttons[i]
            btn2 = self.buttons[i + 1]
            p1 = btn1.mapTo(self, btn1.rect().center())
            p2 = btn2.mapTo(self, btn2.rect().center())
            painter.drawLine(p1, p2)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main widget and layout
        self.main_widget = CustomWidget()
        self.setCentralWidget(self.main_widget)
        self.setFixedSize(100, 300)  # Set a fixed size for the window

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
