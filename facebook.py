class User(object):
	def __init__(name, email, password, friends_list+[], posts[]):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]

	def add_friend(self,email):
		friends_list.append(email)
		print(self.name + 'has added' + email + 'as friends')

	def remove_friend(self,email):
		friends_list.remove(email)
		print(self.name + 'has removed' + email + 'from friends list')
	
	def new_post(self,text):
		posts.append(text)
		print(self.name + 'had posted' + text)

	def get_userinfo(self):
		print('Name' + self.name)
		print('Email' + self.email)
		print('Password' + self.password)
		print('Friends' + self.friends_list)
		print('Posts' + self.posts)

user1=User('maradona', 'maradona40@gmail.com', 1948)
user2=User('jobani', 'jobani39@gmail.com', 1949)

	user1.add_friend('jobani39@gmail.com')



