import os
from forms import  AddForm , DelForm, AddOwner
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request


app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    owner = db.relationship('owners',backref='puppy',uselist=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name: {self.name} Owner: {self.owner}"
        else:
            return f"Puppy name: {self.name} No Owner Exists."

class Owner(db.Model):

    __tablename__ = 'owners'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    pup_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, pup_id):
        self.pup_id = pup_id
        self.name = name


    def __repr__(self):
        return f"Name: {self.name} Puppy Id: {self.pup_id}"


############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Puppy to database
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html',form=form)

@app.route('/list')
def list_pup():
    # Grab a list of puppies from database.
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html',form=form)

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    form = AddOwner()

    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        new_owner = Owner(name, id)
        db.session.add(new_owner)
        db.session.commit()
        return render_template(url_for('list_owners'))

    return render_template('add_owner.html',form=form)

@app.route('/list_owners')
def list_owners():
    Owners = Owner.query.all()
    return render_template('list_owners.html', Owners = Owners)







if __name__ == '__main__':
    app.run(debug=True)
