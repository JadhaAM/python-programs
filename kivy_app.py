from kivy.app import App
from kivy.uix.lable import Lable

class DemoApp(App):
    def build(self):      #combining all the visits
        return Lable(
            text = "Hello world"
        )

if __name__ == "__main__":
    app = DemoApp()
    app.run()
