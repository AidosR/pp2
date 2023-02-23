# Dictionary of movies


movies = [
{

"name": "Usual Suspects",

"imdb": 7.0,

"category": "Thriller"
},
{

"name": "Hitman",

"imdb": 6.3,

"category": "Action"
},
{

"name": "Dark Knight",

"imdb": 9.0,

"category": "Adventure"
},
{

"name": "The Help",

"imdb": 8.0,

"category": "Drama"
},
{

"name": "The Choice",

"imdb": 6.2,

"category": "Romance"
},
{

"name": "Colonia",

"imdb": 7.4,

"category": "Romance"
},
{

"name": "Love",

"imdb": 6.0,

"category": "Romance"
},
{

"name": "Bride Wars",

"imdb": 5.4,

"category": "Romance"
},
{

"name": "AlphaJet",

"imdb": 3.2,

"category": "War"
},
{

"name": "Ringing Crime",

"imdb": 4.0,

"category": "Crime"
},
{

"name": "Joking muck",

"imdb": 7.2,

"category": "Comedy"
},
{

"name": "What is the name",

"imdb": 9.2,

"category": "Suspense"
},
{

"name": "Detective",

"imdb": 7.0,

"category": "Suspense"
},
{

"name": "Exam",

"imdb": 4.2,

"category": "Thriller"
},
{

"name": "We Two",

"imdb": 7.2,

"category": "Romance"
}
]
# 1. Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def first(given):
    for i in movies:
        if i["name"] == given:
            if i["imdb"] > 5.5:
                return True
    return False
print(first("Exam"))
print()

# 2. Write a function that returns a sublist of movies with an IMDB score above 5.5.
def second():
    a = []
    for i in movies:
        if i["imdb"] > 5.5:
            a.append(i["name"])
    return a
print(second())
print()

# 3. Write a function that takes a category name and returns just those movies under that category.
def third(given):
    a = []
    for i in movies:
        if i["category"] == given:
            a.append(i["name"])
    return a
print(third("Romance"))
print()

# 4. Write a function that takes a list of movies and computes the average IMDB score.
def fourth(givens):
    sum = 0
    for i in givens:
        sum += i["imdb"]
    return float(sum/len(givens))

# 5. Write a function that takes a category and computes the average IMDB score.

def fifth(categories):
    sum = 0
    cnt = 0
    for i in movies:
        if i["category"] in categories:
            sum+=i["imdb"]
            cnt+=1
    return float(sum/cnt)

ex = ["Thriller", "Drama"]
print(fifth(ex))