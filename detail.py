import sys
from PyQt5.QtWidgets import QApplication,QSizePolicy, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QListWidget
from button import CustomWidget
class DetailRoute(QWidget):
    def __init__(self, route):
        super().__init__()

        self.setFixedWidth(450)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.route = route
        layout = QVBoxLayout(self)
        self.frame_detail = QFrame()
        layout.addWidget(self.frame_detail)
        self.setLayout(layout)
        self.create_frame()

    def create_frame(self):
        widget = QWidget()
        layout_widget = QHBoxLayout(widget)
        # Left panel for route information
        
        left_panel = QFrame()
        left_panel.setFrameShape(QFrame.StyledPanel)
        left_panel_layout = QVBoxLayout(left_panel)

        # Route title and back button
        header_layout = QHBoxLayout()
        self.back_button = QPushButton("←")
        self.back_button.setFixedSize(30, 30)
        route_title = QLabel(f"Маршрут № {self.route}")
        route_title.setStyleSheet("font-size: 18px; font-weight: bold;")
        header_layout.addWidget(self.back_button)
        header_layout.addWidget(route_title)
        left_panel_layout.addLayout(header_layout)

        # Navigation buttons
        nav_buttons_layout = QHBoxLayout()
        btn_route_go = QPushButton("Xem lượt đi")
        btn_route_return = QPushButton("Xem lượt về")
        nav_buttons_layout.addWidget(btn_route_go)
        nav_buttons_layout.addWidget(btn_route_return)
        left_panel_layout.addLayout(nav_buttons_layout)

        # Tab with route details
        tab_route = QTabWidget()
        
        # Tab 1
        tab1 = QWidget()
        tab_route.addTab(tab1, "Biểu đồ giờ")
        
        tab2 = QWidget()
        layout_tab2 = QVBoxLayout(tab2)
        tab_route.addTab(tab2, "Trạm dừng")
        
        tab3 = QWidget()
        tab_route.addTab(tab3, "Thông tin")
        
        tab4 = QWidget()
        tab_route.addTab(tab4, "Đánh giá")
        
        left_panel_layout.addWidget(tab_route)
        # List of stops
        stop_list = QListWidget()
        stops = [
            "Tòa nhà S2.01", "Tòa nhà S1.01", "Chợ Gò Công",
            "UBND phường Long Thạnh Mỹ", "Cao đẳng Cảnh sát nhân dân 2",
            "Trường Nguyễn Huệ", "Trạm y tế Phường Long Thạnh Mỹ",
            "Ngã ba Mỹ Thành", "Ngã ba Mỹ Thành", "Saigon Hi-tech Park",
            "Trường ĐH Nguyễn Tất Thành", "Công ty Platel Vina",
            "Công ty SAMSUNG", "Vòng xoay Liên Phường"
        ]
        stop_list.addItems(stops)
        #layout_tab2.addWidget(stop_list)
        btns = CustomWidget()
        layout_tab2.addWidget(btns)
        #left_panel_layout.addWidget(stop_list)

        # Adding left panel to the main layout
        
        layout_widget.addWidget(left_panel)
       # layout_widget.addWidget(tab_route)
        
        main_layout = QVBoxLayout(self.frame_detail)
        main_layout.addWidget(widget)
        self.frame_detail.setLayout(main_layout)

    def toggle_visibility(self):
        if self.scroll_frame.isVisible():
            self.scroll_frame.setVisible(False)
            self.hide_button.setText('▶')
        else:
            self.scroll_frame.setVisible(True)
            self.hide_button.setText('◀')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DetailRoute(5)
    main_window.show()
    sys.exit(app.exec_())
