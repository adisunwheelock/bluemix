import os
try:
  from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
  from SocketServer import TCPServer as Server
except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

language_translator = LanguageTranslator(
            username="1195a6c7-d79c-41de-b913-3aa03ac9d702",
                password="54DvzUgK2ovt")
import json
with open('glossary.tmx', 'rb') as training_data:
        custom_model = language_translator.create_model(
                        base_model_id = 'en-es',
                                name = 'custom-english-to-spanish',
                                        forced_glossary = training_data)
            print(json.dumps(custom_model, indent=2))
# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files
os.chdir('static')

httpd = Server(("", PORT), Handler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()

