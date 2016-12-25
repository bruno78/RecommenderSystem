
users = {
	"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
	"Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0}, 
	"Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
	"Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
	"Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
	"Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
	"Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
	"Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}}


# Minkowski formula: MD = (sum(abs(xi - yi)**r))**1/float(r)

def minkowski(user1, user2, r):
	distance = 0
	for key in user1:
		if key in user2:
			distance += (user1[key] - user2[key])**r
	return round(distance**1/float(r), 2)

print minkowski(users['Hailey'], users['Veronica'], 2)
print minkowski(users['Hailey'], users['Jordyn'], 2)
print minkowski(users['Sam'], users['Jordyn'], 2)

def computeNearestNeighbor(username, users):
	neighbors=[]
	for user in users:
		if user != username:
			distance = minkowski(users[user], users[username], 2)
			neighbors.append((distance, user))
	neighbors.sort()
	return neighbors

print computeNearestNeighbor('Hailey', users)

def recommend(username, users):
	recommendations = []
	nearest = computeNearestNeighbor(username, users)
	condition = True
	
	for i in nearest:
		neighbor = i[1]
		for artist in users[neighbor]:
			if artist not in users[username]:
				recommendations.append((artist, users[neighbor][artist]))
		if len(recommendations) > 0:
			return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)



print recommend('Hailey', users)
print recommend('Chan', users)
print recommend('Sam', users)
print recommend('Angelica', users)
