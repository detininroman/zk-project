from flask import Flask
from flask import render_template
from flask import request
from proof import proof, verifier, voters_list

from utils import db

app = Flask(__name__)


@app.route('/', methods=['GET'])
def voting():
    return render_template('page.html')


@app.route('/final', methods=['GET'])
def final():
    return render_template('final.html')


@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')


@app.route('/voting', methods=['POST'])
def func():
    data = request.form
    proof(data['user'])
    answers = [verifier(i) for i in range(len(voters_list))]
    valid = 0 in answers
    if valid:
        db[data['vote']] = db.get(data['vote'], 0) + 1
        print(db[data['vote']])
    return {'valid': valid}, 200
