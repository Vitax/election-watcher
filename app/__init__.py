import os
import json

from flask import Flask, send_from_directory

app = Flask(__name__)
app.secret_key = 'awesome-secret-key'

BASE_URL = os.path.abspath(os.path.dirname(__file__))
CLIENT_APP_FOLDER = os.path.join(BASE_URL, "ClientApp")


#-----File server


# Catch All urls, enabling copy-paste url
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')  # Catch All urls, enabling copy-paste url
def home(path):
    return send_from_directory(CLIENT_APP_FOLDER, 'index.html')


@app.route('/client-app/<path:filename>')
def client_app_folder(filename):
    print('file: %s' % filename)
    return send_from_directory(CLIENT_APP_FOLDER, filename)


@app.route('/dist/<path:filename>')
def client_app_app_folder(filename):
    print('file: %s' % filename)
    return send_from_directory(os.path.join(CLIENT_APP_FOLDER, "dist"), filename)


app.run(debug=True)
