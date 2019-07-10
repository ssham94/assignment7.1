documentary = "Chernobyl"
drama = "Dunkirk"
comedy = "Disaster Artist"
dramedy = "Lala Land"

likes_drama = None
likes_documentary = None
likes_comedy = None

print("Do you like dramas?")
likes_drama = input()

print("Do you like documentaries?")
likes_documentary = input()

print("Do you like comedies?")
likes_comedy = input()

if likes_documentary[0].lower() == "y":
    print("I recommend watching Chernobyl")
elif likes_drama[0].lower() == 'y' and likes_comedy[0].lower() == 'y':
    print("I recommend watching Lala Land")
elif likes_drama[0].lower() == 'y':
    print("I recommend watching Dunkirk")
elif likes_comedy[0].lower() == 'y':
    print("I recommend watching Disaster Artist")
else:
    print("I recommend you read Sapiens by Yuval Harari")

