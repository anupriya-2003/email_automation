from flask import *
import trial
app=Flask(__name__)
@app.route("/")
def invitation():
    #return "working"
    return render_template("first.html")
@app.route("/dummy")
def submit():
    return render_template("submit.html")
app.run()
    
