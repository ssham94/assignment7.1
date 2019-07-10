documentary = "Chernobyl"
drama = "Dunkirk"
comedy = "Disaster Artist"
dramedy = "Lala Land"

print("Do you like documentaries?")
likes_documentary = input()

print("Do you like dramas?")
likes_drama = input()

print("Do you like comedies?")
likes_comedy = input()

if likes_documentary[0].lower() == "y":
    print("I recommend watching }".format(documentary))
elif likes_drama[0].lower() == 'y' and likes_comedy[0].lower() == 'y':
    print("I recommend watching {}".format(dramedy))
elif likes_drama[0].lower() == 'y':
    print("I recommend watching {}".format(drama))
elif likes_comedy[0].lower() == 'y':
    print("I recommend watching {}".format(comedy))
else:
    print("I recommend you read Sapiens by Yuval Harari")

