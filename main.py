# main py file to run flask
from flask import *
import os # library for system functions
import smtplib # library for email rendering

app = Flask(__name__) # initializes app

#Homepage#######################################
@app.route('/') # homepage route
def home():
    return render_template("home.html") # renders homepage


#Checking if run from user######################
if __name__ == '__main__':
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv("IP", "0.0.0.0"),
        debug=True
        )