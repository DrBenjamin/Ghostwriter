##### `ghost.py`
##### Ghostwriter
##### Open-Source, hosted on https://github.com/DrBenjamin/Ghostwriter
##### Please reach out to ben@benbox.org for any questions
#### Loading needed Python libraries
### General libraries
import deepl
import openai



### Kivy libraries
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout




#### Functions
### Function: trans = DeepL translation
def trans(input, target_lang):
    translator = deepl.Translator("c52a9c7d-3198-063c-2bbf-8f67173820ce:fx")
    result = translator.translate_text(input, target_lang = target_lang)
    return result




#### Classes
class ScatterTextWidget(BoxLayout):
    pass

class GhostwriterApp(App):
    def build(self):
        return ScatterTextWidget()




#### Main   
if __name__ == '__main__':
    GhostwriterApp().run()
