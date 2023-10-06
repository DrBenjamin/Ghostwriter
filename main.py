##### `ghost.py`
##### Ghostwriter
##### Open-Source, hosted on https://github.com/DrBenjamin/Ghostwriter
##### Please reach out to ben@benbox.org for any questions
#### Loading needed Python libraries
### General libraries




### Kivy libraries
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ListProperty




#### Classes
### Widgets
class ScatterTextWidget(BoxLayout):
    text_color = ListProperty([1, 0, 0, 1])

    def change_text(self, *args):
        label = self.ids['my_label']	
        label.text = 'Test'

        self.text_color = (1, 0, 0, 1)
        label1 = self.ids.label1
        label2 = self.ids.label2



### Layout
class GhostwriterApp(App):
    def build(self):
        return ScatterTextWidget()




#### Main   
if __name__ == '__main__':
    GhostwriterApp().run()
