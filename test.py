from flask import Flask #get the Flask classes methods

app = Flask(__name__)#constructor

@app.route("/")
def hey():
    return __name__ + "\thello"

@app.route("/help")
def no():
    return __name__ + "\nno"

@app.route("/secret")
def what():
    return __name__ + "<b> leave me alone </b>"

if __name__ == "__main__":
    app.run()#start webserver
