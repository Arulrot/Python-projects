class User:
    def __init__(self,userid,username):
        self.id=userid
        self.name=username
        self.follower=0
        self.following=0
    
    def follow(self,user):
        user.follower+=1
        self.following+=1

user1=User("001","arul")
user2=User("002","mohan")

user1.follow(user2)
    
print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)