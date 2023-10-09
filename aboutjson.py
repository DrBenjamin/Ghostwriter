import json

about_json = json.dumps([
    {'type': 'title',
      'title': 'About'},
    {'title': 'Developer',
      'type': 'string', 
      'desc': 'The Developer of the project.',
      'section': 'About',
      'key': 'dev'},
    {'title': 'Version',
      'type': 'string', 
      'desc': 'Current App Version.',
      'section': 'About',
      'key': 'ver'}
])