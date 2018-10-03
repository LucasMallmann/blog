import json
from flaskblog.models import User, Post
from flaskblog import db

with open('posts.json', 'r') as j:
	data = json.load(j)

for post_dict in data:
	post = Post(title=post_dict.get('title'), 
				content=post_dict.get('content'), 
				user_id=post_dict.get('user_id'))

	db.session.add(post)
	db.session.commit()
	# print(post_dict)
	print('\n')