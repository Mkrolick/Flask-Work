from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey'

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class SimpleForm(FlaskForm):
    # Just One Button
    submit = SubmitField('Click Me.')
    breed = StringField('Select Breed.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        session["breed"] = form.breed.data
        flash(f"Your breed is {session['breed']}")

        return redirect(url_for('index'))
    return render_template('02-home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
