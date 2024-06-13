import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore  import pyqtSignal
from PyQt5.QtCore import Qt
from button_stops import CustomWidget
from info_route import InfoRoute

class DetailRoute(QWidget):
    changedAddr = pyqtSignal(str)
    changedDirection = pyqtSignal(int)
    
    def __init__(self, info_route):
        super().__init__()
        self.info_route = info_route
        self.routeId = self.info_route.routeId
        self.direction = self.info_route.direction
        self.stops = list(self.info_route.get_stops_of_route().keys())
        
        self.setFixedWidth(450)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        layout = QVBoxLayout(self)
        self.frame_detail = QFrame()
        self.create_frame()
        layout.addWidget(self.frame_detail)
        self.setLayout(layout)  

    def update_direction(self, route_with_new_direction):
        self.info_route = route_with_new_direction
        self.direction = self.info_route.direction
        self.stops = list(self.info_route.get_stops_of_route().keys())
        
        self.scroll_content_layout.removeWidget(self.custom_widget)
        self.custom_widget = CustomWidget(self.stops)
        for button in self.custom_widget.buttons:
            button.clicked.connect(self.on_button_click)
        self.scroll_content_layout.addWidget(self.custom_widget)
    
        self.scroll_content_layout_3.removeWidget(self.info_widget)
        type_route = "исходящий маршрут" if self.direction == 0 else "обратный маршрут"
        bus_info = [
            f"Номер маршрута: {self.routeId}",
            f"Название маршрута: {self.info_route.name_route}",
            f"Тип маршрута: {type_route}",
            f"Стоимость билета: {self.info_route.ticket_price}",
            f"Время работы: {self.info_route.time}",
            f"Остановки: {' ➞ '.join(self.stops)}"
        ]
        self.info_widget = InfoRoute(bus_info)
        self.scroll_content_layout_3.addWidget(self.info_widget)
        
        self.btn_route_go.setEnabled(self.direction != 0)
        self.btn_route_return.setEnabled(self.direction != 1)
        
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
        route_title = QLabel(f"Маршрут № {self.routeId}")
        route_title.setStyleSheet("font-size: 18px; font-weight: bold;")
        header_layout.addWidget(self.back_button)
        header_layout.addWidget(route_title)
        left_panel_layout.addLayout(header_layout)

        # Navigation buttons
        nav_buttons_layout = QHBoxLayout()
        self.btn_route_go = QPushButton("Посмотреть маршрут")
        self.btn_route_return = QPushButton("Посмотреть обратный маршрут")
        nav_buttons_layout.addWidget(self.btn_route_go)
        nav_buttons_layout.addWidget(self.btn_route_return)
        self.btn_route_go.setEnabled(self.direction != 0)
        self.btn_route_return.setEnabled(self.direction != 1)
        self.btn_route_go.clicked.connect(lambda: self.changedDirection.emit(0))
        self.btn_route_return.clicked.connect(lambda: self.changedDirection.emit(1))
        left_panel_layout.addLayout(nav_buttons_layout)

        # Tab with route details
        self.tab_widget = QTabWidget()
        self.create_tab1()
        self.create_tab2()
        self.create_tab3()
        self.create_tab4()
        self.tab_widget.setCurrentIndex(1)
        
        left_panel_layout.addWidget(self.tab_widget)
        layout_widget.addWidget(left_panel)
       # layout_widget.addWidget(tab_widget)
        
        main_layout = QVBoxLayout(self.frame_detail)
        main_layout.addWidget(widget)
        self.frame_detail.setLayout(main_layout)
        
    
    def create_tab1(self):
        # Tab 1
        self.tab1 = QWidget()
        self.tab_widget.addTab(self.tab1, "График")
        
    def create_tab2(self):
        self.tab2 = QWidget()
        layout_tab2 = QVBoxLayout(self.tab2)
        scroll_frame = QFrame()
        scroll_layout = QVBoxLayout(scroll_frame)
        
        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        scroll_content = QWidget()
        self.scroll_content_layout = QVBoxLayout(scroll_content)
        
        self.custom_widget = CustomWidget(self.stops)
        for button in self.custom_widget.buttons:
            button.clicked.connect(self.on_button_click)
        self.scroll_content_layout.addWidget(self.custom_widget)
        #scroll_content_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        scroll_area.setWidget(scroll_content)
        
        # Add scroll area to the scroll frame layout
        scroll_layout.addWidget(scroll_area)

        # Add scroll frame to tab layout
        layout_tab2.addWidget(scroll_frame)
        
        self.tab2.setLayout(layout_tab2)
        self.tab_widget.addTab(self.tab2, "Остановка")
    
    def create_tab3(self):
        self.tab3 = QWidget()
        layout_tab3 = QVBoxLayout(self.tab3)
        scroll_frame = QFrame()
        scroll_layout = QVBoxLayout(scroll_frame)
        
        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        scroll_content = QWidget()
        self.scroll_content_layout_3 = QVBoxLayout(scroll_content)
        
        type_route = "исходящий маршрут" if self.direction == 0 else "обратный маршрут"
        bus_info = [
            f"Номер маршрута: {self.routeId}",
            f"Название маршрута: {self.info_route.name_route}",
            f"Тип маршрута: {type_route}",
            f"Стоимость билета: {self.info_route.ticket_price}",
            f"Время работы: {self.info_route.time}",
            f"Остановки: {' ➞ '.join(self.stops)}"
        ]
        self.info_widget = InfoRoute(bus_info)
        self.scroll_content_layout_3.addWidget(self.info_widget)
        scroll_area.setWidget(scroll_content)
        scroll_layout.addWidget(scroll_area)
        layout_tab3.addWidget(scroll_frame)
        self.tab3.setLayout(layout_tab3)
        self.tab_widget.addTab(self.tab3, "Информация")
    
    def create_tab4(self):
        self.tab4 = QWidget()
        self.tab_widget.addTab(self.tab4, "Оценка")

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
                self.changedAddr.emit(self.custom_widget.nameAddr[i].text())
            else:
                self.custom_widget.buttons[i].setStyleSheet(self.custom_widget.get_button_style(False))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DetailRoute(5)
    main_window.show()
    sys.exit(app.exec_())
