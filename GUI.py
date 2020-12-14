# encoding: utf-8
import os
import datetime

import requests
from flask import Flask, render_template, redirect, session, request
# from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)
app.config['SECRET_KEY'] = 'Project_Secret_Key_1337'


def main():
    app.run()


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('base.html')


if __name__ == '__main__':
    main()


