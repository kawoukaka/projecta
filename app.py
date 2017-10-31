from flask import Flask,flash,redirect,render_template,url_for, json, request,jsonify, session
from flask_socketio import SocketIO, send
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRUITY_KEY"] = 'j7I2VDTTedstsl249uigUrtLzK0iRdTt'
socketio = SocketIO(app)
mongo = PyMongo(app)

@socketio.on('message')
def handleMessage(msg):
    print(msg)
    send(msg, broadcast=True)

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app)
