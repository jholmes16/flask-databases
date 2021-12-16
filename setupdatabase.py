from basic import db, Puppy

#Creates all the tables from model class
db.create_all()

sam = Puppy('Sammy', 3)
frank =Puppy('Frankie', 4)

print(sam.id)
print(frank.id)

#Can also add individually
db.session.add_all([sam, frank])

db.session.commit()

print(sam.id)
print(frank.id)
