"""
Flask app to host my simple bio
Habit: Develop -> test locally -> commit -> push to remote -> deploy to prod -> test on prod === 30 minutes

"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index_page():
    "The search page"
    return "<html><h1>Under construction</h1>Hello, I'm arun.<html>"

#----START OF SCRIPT
if __name__=='__main__':
    app.run(host='0.0.0.0',port=6464)