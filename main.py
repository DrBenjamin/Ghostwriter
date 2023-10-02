##### `ghost.py`
##### Ghostwriter
##### Open-Source, hosted on https://github.com/DrBenjamin/Ghostwriter
##### Please reach out to ben@benbox.org for any questions
#### Loading needed Python libraries
import io
import pandas as pd
import openai
import deepl
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
        answer = ''
        sentence = 'The German Malawi Health Programme is facilitating quality improvements for the health system in Malawi. As a GIZ project, the German government, named BMZ, will provide funding for initiatives regarding health or digital health. The project is based in Lilongwe, Malawi.'
            
        # Set API key
        #openai.api_key = ""

        # OpenAI processing
        #model = 'gpt-3.5-turbo' #model == 'gpt-4-0613', 'gpt-4' or 'gpt-3.5-turbo'
        #response_answer = openai.ChatCompletion.create(
        #    model = model,
        #    messages = [{"role": "system", "content": 'Please rewrite the user sentence in a more academic form, but stick to the information given.'},
        #                {"role": "user", "content": sentence},])
                                        
        # Cleaning answer
        #answer = response_answer['choices'][0]['message']['content'].lstrip()
        #answer = answer.replace("'", "")
        #answer = answer.replace('"', '')
        #answer = trans(answer, "DE")
        
        answer = sentence

        f = FloatLayout()
        s = Scatter()
        l = Label(text = str(answer), font_size = 15)
        
        f.add_widget(s)
        s.add_widget(l)
        return f




#### Main   
if __name__ == '__main__':
    GhostwriterApp().run()
