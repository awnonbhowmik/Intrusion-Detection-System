from flask import Flask, render_template
from ids.logging.logger import Logger

app = Flask(__name__)
logger = Logger()

@app.route('/')
def home():
    # Read the last 100 lines from the log file for display
    logs = []
    try:
        with open("ids_log.log", "r") as f:
            logs = f.readlines()[-100:]  # Get the last 100 lines
    except FileNotFoundError:
        logs = ["Log file not found."]
    
    return render_template('index.html', logs=logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
