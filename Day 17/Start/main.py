class User:
    def __init__(self, user_id, username, followers=0, following=0):
        self.id = user_id
        self.username = username
        self.followers = followers
        self.following = following

user_1 = User("001", "Alex")

print(user_1.username) 
