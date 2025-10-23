with open("friends_mary.txt","r") as mary:
    mary = set(mary.read().split())
with open("friends_alex.txt","r") as alex:
    alex = set(alex.read().split())


print(mary&alex)
print(alex-mary)
print(mary-alex)
with open("common_friends.txt","w") as common:
    common_friends = str(mary&alex)
    common.write(common_friends)

