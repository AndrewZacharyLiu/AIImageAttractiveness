import urllib3

http = urllib3.PoolManager()

topics = [planes, cars, stars, scenery, pottery, portrait, headphones, objects, coder, fruits, vegetables, foods, places, attractions]

# Find all of the objects with the word "cat" in the title and return only a few fields per record
r = http.request('GET', 'https://api.harvardartmuseums.org/object',
    fields = {
        'apikey': 'ed7453b3-98fa-4caf-a931-864669b36f4c',
        'title': 'cat',
        'fields': 'objectnumber,title,dated'
    })

print(r.status, r.data)
