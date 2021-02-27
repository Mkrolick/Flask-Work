# Set up your imports and your flask app.
from flask import Flask, request, render_template
app = Flask(__name__)



def represents_int(username):
    for letter in username:
        try:
            str(letter)
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
    return render_template('07-solution-index.html')


# This page will be the page after the form
@app.route('/report')
def report():
    username = request.args.get('username')
    # Check the user name for the 3 requirements.
    if represents_int(username) and string_is_upper_case(username) and string_is_lower_case(username):
        report = True
    else:
        report = False
    upper = string_is_upper_case(username)
    lower = string_is_lower_case(username)
    num_end = represents_int(username)
    return render_template('07-solution-report.html', upper=upper, lower=lower, num_end=num_end, report=report)

if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True)
