from kivy.garden.mapview import MapView
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView


class MyApp(App):
    def build(self):
        # Tạo nút mở popup
        layout = BoxLayout(orientation='vertical')
        scroll_view = ScrollView(size_hint=(1, None), size=(500, 700))
        mapview = MapView(zoom=11, lat=50.6394, lon=3.057)
        scroll_view.add_widget(mapview)
        btn_layout = GridLayout(rows=1, cols=3)
        btn1 = Button(text="Open Popup 1", size_hint=(.5, .1))
        btn1.bind(on_press=self.show_popup1)
        btn2 = Button(text="Open Popup 2", size_hint=(.5, .1))
        btn2.bind(on_press=self.show_popup2)
        btn3 = Button(text="Open Popup 3", size_hint=(.5, .1))
        btn3.bind(on_press=self.show_popup3)
        btn_layout.add_widget(btn1)
        btn_layout.add_widget(btn2)
        btn_layout.add_widget(btn3)
        layout.add_widget(scroll_view)
        layout.add_widget(btn_layout)
        return layout
    
    def show_popup1(self, instance):
        # Tạo nội dung cho popup
        popup_content = Label(text="Hello, this is a popup!")

        # Tạo popup
        popup = Popup(title="Demo Popup", content=popup_content, size_hint=(None, None), size=(400, 400), auto_dismiss=True)
        
        # Hiển thị popup
        popup.open()
    
    def show_popup2(self, instance):
        # Tạo nội dung cho popup
        popup_content = Label(text="Hello, this is a popup!")

        # Tạo popup
        popup = Popup(title="Demo Popup", content=popup_content, size_hint=(None, None), size=(400, 400), auto_dismiss=True)
        
        # Hiển thị popup
        popup.open()
    
    def show_popup3(self, instance):
        # Tạo nội dung cho popup
        popup_content = Label(text="Hello, this is a popup!")

        # Tạo popup
        popup = Popup(title="Demo Popup", content=popup_content, size_hint=(None, None), size=(400, 400), auto_dismiss=True)
        
        # Hiển thị popup
        popup.open()

if __name__ == '__main__':
    MyApp().run()