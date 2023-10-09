import json

settings_json = json.dumps([
    {'type': 'title',
      'title': 'Keys'},
    {'type': 'string',
      'title': 'OpenAI API key',
      'desc': 'Please insert your OpenAI API key here.',
      'section': 'Keys',
      'key': 'openai_key'},
    {'type': 'string',
      'title': 'Deepl API key',
      'desc': 'Please insert your Deepl API key here.',
      'section': 'Keys',
      'key': 'deepl_key'},
    {'type': 'string',
      'title': 'Deepl API language',
      'desc': 'Please set the Deepl target language here.',
      'section': 'Keys',
      'key': 'deepl_lang'}
])