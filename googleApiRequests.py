from google_images_search import GoogleImagesSearch

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch('AIzaSyA7cpHY5EhLn56eGAjEW0Qukgk9eL4r7CI', 'My Project 70423')
imageDatabase = {"planes": [[None],[None]], "cars":[[None],[None]], "stars":[[None],[None]], "scenery":[[None],[None]], "pottery":[[None],[None]], "portrait":[[None],[None]], "headphones":[[None],[None]], "objects":[[None],[None]], "coder":[[None],[None]], "fruits":[[None],[None]], "vegetables":[[None],[None]], "foods":[[None],[None]], "places":[[None],[None]], "attractions":[[None],[None]]}

# define search params
# option for commonly used search param are shown below for easy reference.
# For param marked with '##':
#   - Multiselect is currently not feasible. Choose ONE option only
#   - This param can also be omitted from _search_params if you do not wish to define any value
for key in imageDatabase:
    _search_params = {
    'q': key,
    #'num': 10,
    #'fileType': 'jpg',
    #'rights': 'cc_publicdomain',
    #'safe': 'active', ##
    #'imgType': 'clipart', ##
    #'imgSize': 'huge', ##
    #'imgDominantColor': 'black', ##
    #'imgColorType': 'color' ##
    }
    #gis.search(search_params= _search_params)
    gis.search({'q': 'puppies', 'num': 3})
    #for image in gis.results():
         #mageDatabase[key][0] = image.url  # image direct url
print(imageDatabase)
