import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt

class DotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.dot_radius = 4
        self.setFixedSize(self.dot_radius * 2 + 40, self.dot_radius * 2 + 20)  # Adjust window size
      
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(QColor(0, 128, 128), Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawEllipse(20, 5, self.dot_radius * 2, self.dot_radius * 2)
        painter.end()

class InfoRoute(QWidget):
    def __init__(self, info_route):
        super().__init__()
        self.info_route = info_route
        self.initUI()

    def initUI(self):
        # Set the window properties
        self.setWindowTitle('Bus Information')
        #self.setFixedSize(350, 500)

        self.main_layout = QVBoxLayout(self)

        # Add metro information to the layout
        for info in self.info_route:
            h_layout = QHBoxLayout()
            dot_widget = DotWidget()
            text_label = QLabel(info)
            text_label.setStyleSheet("font-size: 14px")
            text_label.setWordWrap(True)
            h_layout.addWidget(dot_widget, 0, Qt.AlignTop)
            h_layout.addWidget(text_label, 0, Qt.AlignTop)
            h_layout.addStretch()  # Add stretch to push items to the left
            self.main_layout.addLayout(h_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    metro_info = [
            "Tuyến số: Metro 1",
            "Tên tuyến: Bến Thành - Suối Tiên",
            "Loại tuyến: 2",
            "Giá vé: 20,000 VND",
            "Độ dài tuyến: 19 km",
            "Thời gian chạy: 5:30 - 22:30",
            "Số chuyến: 237",
            "Đơn vị: BAN QUẢN LÝ ĐƯỜNG SẮT ĐÔ THỊ",
            "Lượt đi: Ga Bến Thành (MRT) ➞ Ga Nhà hát Thành Phố (MRT) ➞ Ga Ba Son (MRT) ➞ Ga Văn Thánh (MRT) ➞ Ga Cầu Sài Gòn (MRT) ➞ Ga Thảo Điền (MRT) ➞ Ga An Phú (MRT) ➞ Ga Rạch Chiếc (MRT) ➞ Ga Phước Long (MRT) ➞ Ga Bình Thái (MRT) ➞ Ga Thủ Đức (MRT) ➞ Ga Khu Công Nghệ Cao (MRT) ➞ Ga Suối Tiên (MRT) ➞ Ga Bến xe Miền Đông Mới (MRT)",
            "Lượt về: Ga Bến Xe Miền Đông Mới (MRT) ➞ Ga Suối Tiên (MRT) ➞ Ga Khu Công Nghệ Cao (MRT) ➞ Ga Thủ Đức (MRT) ➞ Ga Bình Thái (MRT) ➞ Ga Phước Long (MRT) ➞ Ga Rạch Chiếc (MRT) ➞ Ga An Phú (MRT) ➞ Ga Thảo Điền (MRT) ➞ Ga Cầu Sài Gòn (MRT) ➞ Ga Văn Thánh (MRT) ➞ Ga Ba Son (MRT) ➞ Ga Nhà hát Thành Phố (MRT) ➞ Ga Bến Thành (MRT)"
        ]
    ex = InfoRoute(metro_info)
    ex.show()
    sys.exit(app.exec_())
