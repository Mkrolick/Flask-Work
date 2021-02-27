# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    if name[-1] != "y":
        name = name[0:-1] + "y"
    elif name[-1] == "y":
        name = name[0:-1] + "iful"
    return "<h>This is a page for {}</h>".format(name)

if __name__ == '__main__':
    app.run(debug=True)
