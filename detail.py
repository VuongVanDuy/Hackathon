import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore  import pyqtSignal, QObject

from button import CustomWidget

class DetailRoute(QWidget):
    changeAddr = pyqtSignal(str)
    
    def __init__(self, route, stops):
        super().__init__()

        self.setFixedWidth(450)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.route = route
        self.stops = stops
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
        btn_route_go = QPushButton("Посмотреть маршрут")
        btn_route_return = QPushButton("Посмотреть обратный маршрут")
        nav_buttons_layout.addWidget(btn_route_go)
        nav_buttons_layout.addWidget(btn_route_return)
        left_panel_layout.addLayout(nav_buttons_layout)

        # Tab with route details
        tab_route = QTabWidget()
        
        # Tab 1
        tab1 = QWidget()
        tab_route.addTab(tab1, "График")
        
        tab2 = QWidget()
        layout_tab2 = QVBoxLayout(tab2)
        self.scroll_frame = QFrame()
        self.scroll_layout = QVBoxLayout(self.scroll_frame)
        
        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        scroll_content = QWidget()
        scroll_content_layout = QVBoxLayout(scroll_content)
        
        self.custom_widget = CustomWidget(self.stops)
        for button in self.custom_widget.buttons:
            button.clicked.connect(self.on_button_click)
        scroll_content_layout.addWidget(self.custom_widget)
        #scroll_content_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        scroll_area.setWidget(scroll_content)
        
        # Add scroll area to the scroll frame layout
        self.scroll_layout.addWidget(scroll_area)

        # Add scroll frame to tab layout
        layout_tab2.addWidget(self.scroll_frame)
        
        tab2.setLayout(layout_tab2)
        tab_route.addTab(tab2, "Остановка")
        # Adding left panel to the main layout
        
        tab3 = QWidget()
        tab_route.addTab(tab3, "Информация")
        
        tab4 = QWidget()
        tab_route.addTab(tab4, "Оценка")
        
        left_panel_layout.addWidget(tab_route)
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
    
    def on_button_click(self):
        sender = self.sender()
        for i in range(len(self.custom_widget.buttons)):
            if sender == self.custom_widget.buttons[i]:
                self.custom_widget.buttons[i].setStyleSheet(self.custom_widget.get_button_style(True))
                self.changeAddr.emit(self.custom_widget.nameAddr[i].text())
            else:
                self.custom_widget.buttons[i].setStyleSheet(self.custom_widget.get_button_style(False))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DetailRoute(5)
    main_window.show()
    sys.exit(app.exec_())
