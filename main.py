from extract import *

print("For this to work, two-factor-authentication needs to be off!")

user = Instagram()
while(not(user.checkLogin())):
    pass

# These are the list that holds information on the follwers, followings
# doesNotFB holds the people that the user follows but do not follow the user
followersList = user.extractFollowers()
followingList = user.extractFollowees()
doesNotFB = []

print("A file has been created that has the list of people")
print("These people do not follow you back:\n")
for person in followingList:
    if person not in followersList:
        doesNotFB.append(person)

print(doesNotFB)

followings_df = pd.DataFrame(doesNotFB)
followings_df.to_csv('followings.csv', index=True)



