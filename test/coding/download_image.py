# filename:  download_image.py

import os
import requests
import shutil

# URL of an image from Unsplash, which provides free images
url = "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759"

response = requests.get(url, stream=True)

# Check if the request was successful
if response.status_code == 200:
    response.raw.decode_content = True

    # Get the path to the current user's desktop
    file_name = os.path.join(os.path.expanduser('~'), 'Desktop', 'image.jpg')  

    # Write the data to a file
    with open(file_name, 'wb') as f:
        shutil.copyfileobj(response.raw, f)
        
    print('Image successfully Downloaded: ', file_name)
else:
    print('Image Couldn\'t be retrieved')