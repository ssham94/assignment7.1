documentary = "Chernobyl"
drama = "Dunkirk"
comedy = "Disaster Artist"
dramedy = "Lala Land"

print("How would you rate documentaries? (input 1-5)")
likes_documentary = int(input())

print("How would you rate dramas? (input 1-5)")
likes_drama = int(input())

print("How would you rate comedies? (input 1-5)")
likes_comedy = int(input())

scores = {'Documentary': likes_documentary, 'Drama': likes_drama, 'Comedy': likes_comedy}

highest_score = max(scores, key=scores.get)
print(highest_score)

if likes_documentary > 3:
    print("I recommend watching {}".format(documentary))
elif likes_drama > 3 and likes_comedy > 3:
    print("I recommend watching {}".format(dramedy))
elif likes_drama > 3:
    print("I recommend watching {}".format(drama))
elif likes_comedy > 3:
    print("I recommend watching {}".format(comedy))
elif highest_score == "Documentary":
    print("I recommend watching {}".format(documentary))
elif highest_score == "Drama":
    print("I recommend watching {}".format(drama))
elif highest_score == "Comedy":
    print("I recommend watching {}".format(comedy))

