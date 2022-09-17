import numpy
import time
import threading 
from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField, SelectField
import random
import jyserver.Flask as jsf


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
count = 0

class ButtonForm(FlaskForm):
    button = SubmitField("Start test")

@jsf.use(app)
class App:
    def __init__(self):
        pass
    def increment(self):
        self.js.document.getElementById("count").innerHTML = 1


@app.route("/", methods=['GET', 'POST'])
def home():
    form = ButtonForm()
    return render_template('index.html',form = form)

@app.route("/test", methods=['GET', 'POST'])
def test():
    t1 = threading.Thread(target=eye_tracker)
    t1.start()
    return render_template('test.html')


def eye_tracker():
    winner =[]
    for x in range(6):
        image_bias = 0
        t2 = threading.Thread(target=image_update)
        t2.start()
        for y in range(1000):
            time.sleep(0.1)
            if (random.randrange(0,1) == 0):
                image_bias -= 1
            else:
                image_bias += 1
        if(image_bias > 0):
            winner.append("real")
        else:
            winner.append("ai")
            
def image_update():
    return App.render(render_template("test.html"))

if __name__ == "__main__":
    app.run(debug=True)