# Set up your imports and your flask app.
from flask import Flask, request, render_template
app = Flask(__name__)



def represents_int(username):
    try:
        str(username)
        return True
    except Exception:
        return False

def string_is_upper_case(string):
    for letter in string:
        if letter.isupper():
            return True
            pass
    return False

def string_is_lower_case(string):
    for letter in string:
        if letter.islower():
            return True
            pass
    return False

@app.route('/')
def index():
    # This home page should have the form.
    return render_template('07-solution-base.index')


# This page will be the page after the form
@app.route('/report')
def report():
    username = request.args.get('username')
    # Check the user name for the 3 requirements.
    if username[-1] == username[-1].upper() and string_is_upper_case(username) and string_is_lower_case(username):
        return True
    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.
    pass
    render_template('07-solution-base.index', report=report)

if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True)
