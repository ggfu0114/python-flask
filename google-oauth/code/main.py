import datetime
import time
import os
import firebase_admin
import flask
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import exceptions
from flask import Flask
from flask import render_template
import pathlib

app = Flask(__name__)

cred_path = os.path.join(pathlib.Path().resolve(), 'secret','firebase-credential-file.json')
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred) 


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/sessionLogin', methods=['POST'])
def session_login():
    # To ensure that cookies are set only on recently signed in users, check auth_time in
    # ID token before creating a cookie.

    id_token = flask.request.json['idToken']

    try:
        decoded_claims = auth.verify_id_token(id_token)

        # Only process if the user signed in within the last 5 minutes.
        if time.time() - decoded_claims['auth_time'] < 5 * 60:
            # Set session expiration to 5 days.
            expires_in = datetime.timedelta(days=5)
            # Create the session cookie. This will also verify the ID token in the process.
            # The session cookie will have the same claims as the ID token.
            session_cookie = auth.create_session_cookie(
                id_token, expires_in=expires_in)
            response = flask.jsonify({'status': 'success'})
            # Set cookie policy for session cookie.
            expires = datetime.datetime.now() + expires_in
            response.set_cookie('session', session_cookie,
                                expires=expires,
                                httponly=True,
                                # Set True for only delivery cookie over https
                                secure=False)
            return response
        # User did not sign in recently. To guard against ID token theft, require
        # re-authentication.
        return flask.abort(401, 'Recent sign in required')
    except auth.RevokedIdTokenError as ex:
        return flask.abort(401, 'ID token has been revoked')
    except auth.ExpiredIdTokenError as ex:
        return flask.abort(401, 'ID token is expired')
    except auth.InvalidIdTokenError as ex:
        return flask.abort(401, 'ID token is invalid')
    except exceptions.FirebaseError:
        return flask.abort(401, 'Failed to create a session cookie')


@app.route('/sessionLogout', methods=['GET'])
def session_logout():
    session_cookie = flask.request.cookies.get('session')
    try:
        decoded_claims = auth.verify_session_cookie(session_cookie)
        auth.revoke_refresh_tokens(decoded_claims['sub'])
        response = flask.make_response(flask.redirect('/login'))
        response.set_cookie('session', expires=0)
        return response
    except auth.InvalidSessionCookieError:
        return flask.redirect('/login')


@app.route('/profile', methods=['GET'])
def access_restricted_content():
    session_cookie = flask.request.cookies.get('session')
    if not session_cookie:
        # Session cookie is unavailable. Force user to login.
        return flask.redirect('/login')

    # Verify the session cookie. In this case an additional check is added to detect
    # if the user's Firebase session was revoked, user deleted/disabled, etc.
    try:
        decoded_claims = auth.verify_session_cookie(
            session_cookie, check_revoked=True)
        print('decoded_claims', decoded_claims)
        return render_template('authorized.html', name='Paul', desc='Yo make it.')

    except auth.InvalidSessionCookieError:
        # Session cookie is invalid, expired or revoked. Force user to login.
        return flask.redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
