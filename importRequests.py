import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': 'horse painting',
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
imageData =r.json()
print(imageData)