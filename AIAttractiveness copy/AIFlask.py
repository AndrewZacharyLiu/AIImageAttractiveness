import numpy
import time
import threading 
from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField, SelectField
from eye_tracker import track_eye
import asyncio

results = []
direction = False


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
count = 0

class ButtonForm(FlaskForm):
    button = SubmitField("Start test")

class CuttonForm(FlaskForm):
    button = SubmitField("Start test")


@app.route("/", methods=['GET', 'POST'])
def home():
    form = ButtonForm()
    return render_template('index.html',form = form)

@app.route("/test", methods=['GET', 'POST'])
def test():
    form = CuttonForm()
    s = "I want this to print"
    return render_template('test.html', content={"val":s}, form = form)



@app.route("/testcall", methods=['GET', 'POST'])

#initialize the video feed


async def testcall():
    form = CuttonForm()
    results = []

    track_eye(direction, results)
    #check this thing
    #results.append(direction)
    right = 0
    left = 0
    for dir in results:
        if dir:
            right += 1
        else:
            left += 1
    left_right = (left,right)
    return render_template('test.html', content={"val":left_right}, form = form)
            
if __name__ == "__main__":
    app.run(port=5000,debug=True)

