import sys
from PyQt5.QtWidgets import QApplication, QSizePolicy, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QLabel, QLineEdit, QPushButton, QFrame
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from init_data import init_data, get_info_general_routes
from detail import DetailRoute
import os

class BusMapApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('BusMap')
        self.setGeometry(100, 100, 1200, 600)
        
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QHBoxLayout(self.main_widget)
        self.buttons = []
        
        # frame tabs
        self.frame_tabs = QFrame()
        self.frame_tabs.setFixedWidth(450)
        self.frame_tabs.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.main_layout.addWidget(self.frame_tabs)
        
        # frame button hide tabs
        self.frame_hide_tab = QFrame()
        self.main_layout.addWidget(self.frame_hide_tab)
        
        # frame view map
        self.frame_view = QFrame()
        self.frame_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_layout.addWidget(self.frame_view)
        
        self.create_tabs()
        self.createBtnHideTab()
        self.createMapRoute()
        
        
    def create_tabs(self):
        main_tab_widget = QTabWidget()
        # Tab 1
        tab1 = QWidget()
        tab1_layout = QHBoxLayout()

        # Create a frame to hold the scroll area and hide button
        self.scroll_frame = QFrame()
        self.scroll_layout = QVBoxLayout(self.scroll_frame)
        
        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        scroll_content = QWidget()
        scroll_content_layout = QVBoxLayout(scroll_content)

        # Add search bar
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Поиск автобусных маршрутов")
        scroll_content_layout.addWidget(search_bar)

        # Add bus info widgets
        self.all_routes = get_info_general_routes()
        for route in self.all_routes:
            scroll_content_layout.addWidget(self.create_bus_info(route[0], route[1], route[2], route[3]))
        
        scroll_area.setWidget(scroll_content)
        
        # Add scroll area to the scroll frame layout
        self.scroll_layout.addWidget(scroll_area)

        # Add scroll frame to tab layout
        tab1_layout.addWidget(self.scroll_frame)
        
        tab1.setLayout(tab1_layout)
        main_tab_widget.addTab(tab1, 'Поиск')

        # Tab 2
        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel('Content for TÌM ĐƯỜNG'))
        tab2.setLayout(tab2_layout)
        main_tab_widget.addTab(tab2, 'Поиск маршрута')
        
        frame_layout = QVBoxLayout(self.frame_tabs)
        frame_layout.addWidget(main_tab_widget)
        self.frame_tabs.setLayout(frame_layout)
        self.frame_tabs.adjustSize()

    def createBtnHideTab(self):
        hide_tab_layout = QVBoxLayout(self.frame_hide_tab)
        self.hide_button = QPushButton("◀")
        self.hide_button.setFixedSize(30, 70)
        self.hide_button.setStyleSheet("background-color: green; color: white; font-size: 20px;")
        self.hide_button.clicked.connect(self.toggle_visibility_tabs)
        hide_tab_layout.addWidget(self.hide_button)
        self.frame_hide_tab.setLayout(hide_tab_layout)
    
    def createMapRoute(self):
        view_map_layout = QVBoxLayout(self.frame_view)
        
        self.map = QWebEngineView()
        html_file = './1062.html'
        url = QUrl.fromLocalFile(os.path.realpath(html_file))
        self.map.load(url)
        
        view_map_layout.addWidget(self.map)
        self.frame_view.setLayout(view_map_layout)
    
    def showRoute(self, html_file):
        url = QUrl.fromLocalFile(os.path.realpath(html_file))
        self.map.setUrl(url)
    
    def update_location(self, newAddr):
        lat = self.infoCurRoute[newAddr][0]
        lon = self.infoCurRoute[newAddr][1]
        # Call JavaScript function to update marker location
        self.map.page().runJavaScript(f"updateMarker({lat}, {lon});")
        
    def create_bus_info(self, route, description, time, price):
        button = QPushButton()
        button.setFixedHeight(120)
        buttonLayout = QVBoxLayout(button)

        route_label = QLabel(f"№ маршрута автобуса {route}")
        route_label.setStyleSheet("font-weight: bold; font-size: 16px; color: green")

        desc_label = QLabel(description)
        time_label = QLabel(f"Время: {time}")
        price_label = QLabel(f"Стоимость билета: {price}")

        buttonLayout.addWidget(route_label)
        buttonLayout.addWidget(desc_label)
        buttonLayout.addWidget(time_label)
        buttonLayout.addWidget(price_label)

        button.setLayout(buttonLayout)
        button.clicked.connect(lambda: self.showDetailRoute(route))
        return button

    def showDetailRoute(self, route):
        try:
            self.cur_data_route = init_data(route, 0)
            self.infoCurRoute = self.cur_data_route.get_stops_of_route()
        except Exception as e:
            print(e)
        
        stops_route = list(self.infoCurRoute.keys())
        self.frame_tabs.setVisible(False)
        self.frame_detail = DetailRoute(route, stops_route)
        self.main_layout.insertWidget(0, self.frame_detail)
        self.main_widget.setLayout(self.main_layout)   
        self.showRoute(f"./{route}" + ".html")   
        self.frame_detail.back_button.clicked.connect(self.backTabs)
        self.hide_button.clicked.disconnect(self.toggle_visibility_tabs)
        self.hide_button.clicked.connect(self.toggle_visibility_details)
        self.frame_detail.changeAddr.connect(self.update_location)
        
    
    def backTabs(self):
        self.frame_detail.setVisible(False)
        self.frame_tabs.setVisible(True)
        self.hide_button.clicked.disconnect(self.toggle_visibility_details)
        self.hide_button.clicked.connect(self.toggle_visibility_tabs)
        
    def toggle_visibility_tabs(self):
        if self.frame_tabs.isVisible():
            self.frame_tabs.setVisible(False)
            self.hide_button.setText('▶')
        else:
            self.frame_tabs.setVisible(True)
            self.hide_button.setText('◀')
    
    def toggle_visibility_details(self):
        if self.frame_detail.isVisible():
            self.frame_detail.setVisible(False)
            self.hide_button.setText('▶')
        else:
            self.frame_detail.setVisible(True)
            self.hide_button.setText('◀')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = BusMapApp()
    main_window.show()
    sys.exit(app.exec_())
