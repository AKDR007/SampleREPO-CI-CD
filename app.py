import flask
from flask import Flask, request, redirect, render_template, render_template_string


app = Flask(__name__)

@app.route('/')
def R():
    return Home()


@app.route('/AKDR_Home')
def Home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7770)