##### `ghost.py`
##### Ghostwriter
##### Open-Source, hosted on https://github.com/DrBenjamin/Ghostwriter
##### Please reach out to ben@benbox.org for any questions
#### Loading needed Python libraries
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
### Kivy libraries
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout




#### Functions
### Function: trans = DeepL translation
def trans(input, target_lang):
    translator = deepl.Translator("c52a9c7d-3198-063c-2bbf-8f67173820ce:fx")
    result = translator.translate_text(input, target_lang = target_lang)
    return result




#### Classes
class GhostwriterApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text = 'The German Malawi Health Programme', font_size = 15)
        
        f.add_widget(s)
        s.add_widget(l)
        return f




#### Main   
if __name__ == '__main__':
    GhostwriterApp().run()
