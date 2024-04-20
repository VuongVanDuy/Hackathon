
# viết mã tạo ứng dụng android đơn giản, có 1 nút, khi click vào nút sẽ gửi request và nhận response từ server https://spb-transport.gate.petersburg.ru/

# Path: app.py
import requests
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview import RecycleView

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=3)
        button = Button(text='Click me')
        
        button.bind(on_press=self.on_press)
        layout.add_widget(button)
        return layout

    def on_press(self, instance):
        url = 'https://spb-transport.gate.petersburg.ru/api/stops'
        response = requests.get(url)
        print(response.text)

    
    

if __name__ == '__main__':
    MyApp().run()

