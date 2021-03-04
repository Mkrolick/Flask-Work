from BasicModelApp import db, Puppy


dog = Puppy('aaa', 3)
db.session.add(dog)
db.session.commit()


print(Puppy.query.get(5).name)
print(Puppy.query.all())
