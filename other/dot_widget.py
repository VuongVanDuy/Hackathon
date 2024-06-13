import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QBrush, QColor, QPixmap
from PyQt5.QtCore import Qt

class DotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.dot_radius = 10
        self.setFixedSize(self.dot_radius * 2 + 40, self.dot_radius * 2 + 20)  # Adjust window size
      

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(QColor(0, 128, 128), Qt.SolidPattern)

        painter.setBrush(brush)

        # Draw dots vertically
        # dot_radius = 10
        # spacing = 20
        # for i in range(10):
        #     y = i * (dot_radius * 2 + spacing)
        #     painter.drawEllipse(20, y, dot_radius * 2, dot_radius * 2)
        painter.drawEllipse(20, 0, self.dot_radius * 2, self.dot_radius * 2)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dot = DotWidget()
    dot.show()
    sys.exit(app.exec_())
