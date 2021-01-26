# Requires "requests" to be installed (see python-requests.org)
#import requests module
import requests

image = "./images.jfif"  # filepath for image

# POST request to send our image to remove.bg
response = requests.post(
    'https://api.remove.bg/v1.0/removebg', #link to connect
    files={'image_file': open(image, 'rb')}, #file to send
    data={'size': 'auto'}, 
    headers={'X-Api-Key': 'you api key'},  # fill with your key
)

if response.status_code == requests.codes.ok:
    with open('file_name.png', 'wb') as out: #you can change file name
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)
