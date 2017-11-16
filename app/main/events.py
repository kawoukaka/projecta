from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    sid = session.get('sid')
    join_room(sid)
    emit('status', {'msg': session.get('username') + ' has started chatting'}, sid=sid)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    sid = session.get('sid')
    emit('message', {'msg': session.get('username') + ':' + message['msg']}, sid=sid)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    sid = session.get('sid')
    leave_room(sid)
    for key in session.keys():
        session.pop['sid']
    emit('status', {'msg': session.get('username') + ' has disconnected'}, sid=sid)
