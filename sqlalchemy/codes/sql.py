import random

from main import User, db

print(f'Create databse tables.')
db.create_all()

print('Try to create a new user')
random_user_name = ''.join((random.choice('abcdxyzpqr') for i in range(5)))
new_user = User(username=random_user_name,
                email=random_user_name+'@example.com')
db.session.add(new_user)
db.session.commit()
print(f'User: {new_user} created.')
