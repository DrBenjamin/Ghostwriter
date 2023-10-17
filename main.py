##### `ghost.py`
##### Ghostwriter
##### Open-Source, hosted on https://github.com/DrBenjamin/Ghostwriter
##### Please reach out to ben@benbox.org for any questions
__version__ = '1.0'
#### Loading needed Python libraries
### General libraries
import packaging
import packaging.version
import packaging.specifiers
import packaging.requirements
from platformdirs import *
from platformdirs.macos import *
import deepl
import openai



### Kivy libraries
import kivy
kivy.require('2.2.1')
from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.config import ConfigParser
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.settings import SettingsWithSidebar
from kivy.properties import ListProperty
from kivy.base import runTouchApp
from settingsjson import settings_json
from aboutjson import about_json




#### Functions
def chatgpt(text, key):
    # Set API key
    openai.api_key = key

    # Doing the requests to OpenAI for summarizing / keyword extracting the question
    try:
        # Creating summary of user question
        model = 'gpt-3.5-turbo'
        response = openai.ChatCompletion.create(model = model, messages = [
            {"role": "system", "content": "Please write this sentence in a more academic form."},
            {"role": "user", "content": text},])
        output = response['choices'][0]['message']['content'].lstrip()
        return output
    except Exception as e:
        print('Error: ', str(e))



### Function: trans = DeepL translation
def trans(input, target_lang, key):
    try:
        translator = deepl.Translator(key)
        result = translator.translate_text(input, target_lang = target_lang)
        return result
    except Exception as e:
        return 'Error: ' + str(e)




#### Classes
### Widgets
class ScatterTextWidget(BoxLayout):
    # Configutation
    config = ConfigParser()
    config.read('ghostwriter.ini')
    
    # Set text color
    text_color = ListProperty([1, 1, 1, 1]) 

    def change_text(self, *args):
        my_text = self.ids['my_textinput']
        label3 = self.ids['label3']
        label3.text = str(trans(my_text.text, self.config.get('Keys','deepl_lang'), self.config.get('Keys','deepl_key')))

    def button_pressed(self):
        # Call MyCode function
        self.MyCode()

    # My Code
    def MyCode(self, *args):

        try:
            my_text = self.ids['my_textinput']

            # Improved sentence
            label1 = self.ids['label1']
            label1.text = str(chatgpt(my_text.text, self.config.get('Keys','openai_key')))

            # Translated sentence
            label2 = self.ids['label2']
            label2.text = str(chatgpt(label1.text, self.config.get('Keys','openai_key')))

            # Translated sentence
            label3 = self.ids['label3']
            label3.text = str(trans(label2.text, self.config.get('Keys','deepl_lang'), self.config.get('Keys','deepl_key')))

        except Exception as e:
            print('Error: ', str(e))



### Layout
class GhostwriterApp(App):
    clipboard = Clipboard
    
    def build_config(self, config):
        config.setdefaults('Keys', {'openai_key': "sk-"})
        config.setdefaults('Keys', {'deepl_key': ":fx"})
        config.setdefaults('Keys', {'deepl_lang': "DE"})
        config.setdefaults('About', {'dev': 'Benjamin Gross (ben@benbox.org)'})
        config.set('About', 'dev', 'Benjamin Gross (ben@benbox.org)')
        config.setdefaults('About', {'ver': "V0.1a"})
        config.set('About', 'ver', 'V0.1a')

    def build_settings(self, settings):
        settings.add_json_panel('API keys', self.config, data = settings_json)
        settings.add_json_panel('Information', self.config, data = about_json)

    def on_config_change(self, config, section, key, value):
        print(config, section, key, value)

    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.use_kivy_settings = False
        return ScatterTextWidget()




#### Main   
if __name__ == '__main__':
    GhostwriterApp().run()
