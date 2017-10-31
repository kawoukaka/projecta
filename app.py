from flask import Flask,flash,redirect,render_template,url_for, json, request,jsonify, session
from flask_socketio import SocketIO, emit
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRUITY_KEY"] = 'j7I2VDTTedstsl249uigUrtLzK0iRdTt'
socketio = SocketIO(app)
mongo = PyMongo(app)

def messageRecived():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, debug = True )
