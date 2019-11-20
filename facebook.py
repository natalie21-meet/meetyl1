users=[]
posts_list=[]
class User(object):
	def __init__(self, name, email, password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]


	def add_friend(self,email):	
		self.friends_list.append(email)
		print(self.name + ' has added ' + email + ' to friends list ')

	def remove_friend(self,email):
		self.friends_list.remove(email)
		print(self.name + ' has removed ' + email + ' from friends list ')
		
	def new_post(self,text):
		post1=Post(0, text, self.email)
		posts_list.append(post1)
		print(self.name + ' had posted: ' + text)


	def get_userinfo(self):
		print('Name: ' + self.name)
		print('Email: ' + self.email)
		print('Password: ' + str(self.password))
		print('Friends: ' + str(self.friends_list))

class Post(object):
	def __init__(self, likes, text, author):
		self.likes=0
		self.comments=[]
		self.text=text
		self.author=author

	def like_post(self,email):
		self.like=+1
		print(email + ' liked your post.')

	def comment_post(self, text):
		self.comments.append(text)
		print(email + ' commented on your post ' + text )

class Comment(Post):
	def __init__(self, like):
		self.like=like
		self.reply=[]


user1=User('maradona', 'maradona40@gmail.com', 1948)
user2=User('jobani', 'jobani39@gmail.com', 1949)

user1.add_friend('jobani39@gmail.com')
user2.add_friend('maradona40@gmail.com')

user1.new_post('miss playing soccer like profesional')
user2.new_post('had fun training the kids team yesterday. keep going!')

user1.get_userinfo()
user2.get_userinfo()


class Post(object):
	def __init__(self, likes, text):
		self.likes=0
		self.comments=[]
		self.text=text

	def like_post(self,email):
		self.like=+1
		print(email + ' liked your post.')

	def comment_post(self, text):
		self.comments.append(text)
		print(email + ' commented on your post ' + text )




