from flask import Flask, make_response, request
from random import randint
import os

app = Flask(__name__)


@app.route('/login/<name>')
def getCookie(name):
    resp = make_response('Cookie')
    session_id = str(randint(1, 500))
    resp.set_cookie(key="session_key", value=session_id, max_age=3600)
    resp.set_cookie(key="session_name", value=name, max_age=3600)
    f = open(f"src/session/{name}", "a")
    f.write(f"{session_id}\n")
    f.close()
    return resp


@app.route('/')
def compareCookie():
    session_name = request.cookies.get('session_name')
    if session_name is None:
        return "<p>Please login first</p>"
    session_id = request.cookies.get('session_key')
    try: 
        with open(f"src/session/{session_name}", "r") as f:
            for line in f:
                if session_id == line.strip():
                    return f"session_id: {session_id}, session_name: {session_name}"
    except FileNotFoundError:
        return "<p>Invalid session</p>"
    return "<p>Invalid session</p>"

@app.route('/logout')
def logout():
    session_name = request.cookies.get('session_name')
    if session_name is None:
        return "<p>Please login first</p>"
    try:
        os.remove(f"src/session/{session_name}")
        return "<p>Logout successfully</p>"
    except FileNotFoundError:
        return "<p>Invalid session</p>"


if __name__ == '__main__':
    app.run()
