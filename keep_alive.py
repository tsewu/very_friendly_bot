"""
Author:      Roy Wu
Description: webserver code
History:     05/25/2021 - intial version
Referebce:   https://www.youtube.com/watch?v=SPTfmiYiuok
"""

from flask     import Flask  #*use Flask as the web server
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Hello, I am alive!"


def run():
  app.run(host='0.0.0.', port=800)


def keep_alive():
  t = Thread(target=run)
  t.start()  