# Web App
from flask import Flask
from multiprocessing import Process
from waitress import serve
from bot.load_environ import Environment

app = Flask(__name__)

@app.route('/')
def start():
    return "Bot is Running"

def run_flask():
    serve(app, host='0.0.0.0', port=Environment().WEB_APP_PORT)

# Start app
if __name__ == "__main__":
    print(f"WebApp is running on port {Environment().WEB_APP_PORT}")
    fl = Process(target=run_flask)
    fl.start()
    import run
