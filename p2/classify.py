import os
import sys
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Add your Computer Vision subscription key and endpoint to your environment variables.
if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

analyze_url = endpoint + "vision/v3.0/analyze"

with open('images_to_filter.txt') as images_to_filter:
    for img_name in images_to_filter.readlines():
        img_name = img_name.replace('\n', '')
        print(img_name)
        image_name = 'images/%s' % img_name
        im = Image.open(image_name)
        im = im.resize((50, 50))
        im.save(image_name)

        # Read the image into a byte array
        image_data = open(image_name, "rb").read()

        headers = {'Ocp-Apim-Subscription-Key': subscription_key,
                   'Content-Type': 'application/octet-stream'}
        params = {'visualFeatures': 'Categories,Description,Color'}
        response = requests.post(
            analyze_url, headers=headers, params=params, data=image_data)
        response.raise_for_status()

        # The 'analysis' object contains various fields that describe the image. The most
        # relevant caption for the image is obtained from the 'description' property.
        analysis = response.json()

        filtered_file = 'filtered_images/%s' % img_name
        if "dog" in analysis["description"]["tags"]:
            img = Image.new('RGB', (5, 5), color = 'black')
        else:
            img = Image.new('RGB', (5, 5), color = 'white')
        img.save(filtered_file)

