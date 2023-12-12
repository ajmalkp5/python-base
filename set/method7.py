insta_users={"mohanlal","dq","prithvi","vijay","surya","fahad","lalu","mammookka"}

mohanlal_following={"dq","prithvi","vijay"}
dq_friends={"prithvi","vijay","surya","lalu"}

#suggestion to mohanlal
# insta_users.remove("mohanlal")
suggestion_mohanlal=insta_users.difference(mohanlal_following)
suggestion_mohanlal.discard("mohanlal")

#mutual freinds of both
mutual_friends=mohanlal_following.intersection(dq_friends)
print(mutual_friends)