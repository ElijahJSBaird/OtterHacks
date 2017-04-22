# main py file to run flask
from flask import *
import os # library for system functions
import smtplib # library for email rendering

app = Flask(__name__) # initializes app
comments = {}
#Homepage#######################################
@app.route('/') # homepage route
def home():
    return render_template("home.html") # renders homepage
    
@app.route('/comment') # comment page
def write_comment():
    return render_template("comment.html")

@app.route('/comment', methods=["POST"])
def take_comment():
    name = request.form['name']
    email = request.form['email']
    comment = request.form['comment']
    comments[name] = {"email" : email, "comment" : comment}
    for person in comments:
        step1 = comments[person]
        step2 = step1['comment']
        print (person + " said " + step2)
    return render_template("comment.html")
    
    

#Checking if run from user######################
if __name__ == '__main__':
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv("IP", "0.0.0.0"),
        debug=True
        )