imageDatabase = {"planes": [[None],[None]], 
                "cars":[[None],[None]], 
                "stars":[[None],[None]], 
                "scenery":[[None],[None]], 
                "pottery":[[None],[None]], 
                "portrait":[[None],[None]], 
                "headphones":[[None],[None]], 
                "objects":[[None],[None]], 
                "coder":[[None],[None]], 
                "fruits":[[None],[None]], 
                "vegetables":[[None],[None]], 
                "foods":[[None],[None]], 
                "places":[[None],[None]], 
                "attractions":[[None],[None]]}


# from torch import autocast
# from diffusers import StableDiffusionPipeline
# pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token="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")
# pipe = pipe.to("cpu")

# prompt = "apple"
# with autocast("cpu"):
#     image = pipe(prompt).images[0]  

#import requests, lxml, re, urllib.request
from bs4 import BeautifulSoup
import random

for key in imageDatabase:
    params = {
        "q": key, # search query
        "tbm": "isch",                # image results
        "hl": "en",                   # language of the search
        "gl": "us",                   # country where search comes from
        "content-type": "image/png"   # parameter that indicate the original media type 
    }

    html = requests.get("https://images.google.com/search", params=params, timeout=30)
    soup = BeautifulSoup(html.text, "lxml")

    def get_images_with_request_headers():
        i = 0
        images=[]
        for img in soup.select("img"):
            images.append(img["src"])
        return images[random.randrange(len(images))]

    imageDatabase[key][0] = get_images_with_request_headers()

#print(imageDatabase)
