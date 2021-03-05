from BasicModelApp import db, Puppy


dog = Puppy('aaa', 3)
db.session.add(dog)
db.session.commit()

Puppy.query.filter_by(name="aaa").delete
print(Puppy.query.all())
