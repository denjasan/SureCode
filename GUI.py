# encoding: utf-8
import os

import requests
from flask import Flask, render_template, redirect, session, request
# from flask_ngrok import run_with_ngrok

from Main import SureCode

app = Flask(__name__)
# run_with_ngrok(app)
app.config['SECRET_KEY'] = 'Project_Secret_Key_1337'


def main():
    app.run()


@app.route('/', methods=['GET', 'POST'])
def home():
    global file_name
    if request.method == 'GET':
        prevention = SureCode(file_name=file_name, xss=True, sql_injection=True)
        if file_name:
            os.remove(file_name)
        return render_template('base.html', data=prevention.vulnerabilities,
                               keys=prevention.vulnerabilities['xss'].keys())
    elif request.method == 'POST':
        file_name = 'data/user_files/' + request.files['file'].filename
        request.files['file'].save(file_name)
        return redirect("/")


if __name__ == '__main__':
    file_name = ''
    main()


