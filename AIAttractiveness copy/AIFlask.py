import numpy
import time
import threading 
from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField, SelectField
import random
from eye_tracker import track_eye
import cv2

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


def testcall():
    form = CuttonForm()
    results = []
    cv2.destroyAllWindows()
    track_eye(direction, results)
    cv2.destroyAllWindows()
    #check this thing
    #results.append(direction)
    return render_template('test.html', content={"val":results}, form = form)
            
if __name__ == "__main__":
    app.run(port=5012,debug=True)

