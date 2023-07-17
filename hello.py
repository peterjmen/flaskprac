from flask import Flask

app = Flask(__name__)

# !Important, 1st need to tell terminal the application to work with by exporting the FLASK_APP envinronment variable
# TODO enironment varaible... set FLASK_APP=hello.py
# ! now can /flask run
# (env) C:\Github\fullstack\flaskprac>set FLASK_APP=hello.py
# (env) C:\Github\fullstack\flaskprac>flask run


# print(__name__)


# when user hits up this path, the first forward slash is the home and it knows that when i got there we will see the home page
# @ sign is a python decorator - decrator and ad functionalities to functions, a function that will give additional functionality
@app.route(
    "/"
)  #  Method only called when decorator says it's appropriate to do so, i.e. when address is url '/'
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/page1")  #  will run when url + /page1
def page1():
    return "You are on page one"


# if running code from this file, so like... if name aka this file == __main__ then running the code from within this current file
# checks that is is current file where code is located, if so runs it
if __name__ == "__main__":
    app.run()
