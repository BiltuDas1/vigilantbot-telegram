# Web App
from flask import Flask
from multiprocessing import Process

app = Flask(__name__)

import logging
logging.getLogger('werkzeug').setLevel(logging.ERROR)

@app.route('/')
def start():
    return ""

def run_flask():
    app.run(host='0.0.0.0', port='5000')

# Start app
print("Vigilant bot has been started...")
fl = Process(target=run_flask)
fl.start()
import run