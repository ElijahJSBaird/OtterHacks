from flask import *
import os
import sys

app = Flask(__name__)

@app.route ("/")
def index():
    return render_template("home.html")
    
@app.route("/college")
def college():
    return render_template("CSUMontereyBay.html")
    
if __name__ == '__main__':      
    app.run(
        port = int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0'),
        debug = True
    )