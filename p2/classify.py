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
# f = open('unclassified_images.txt', 'w')
#
# with open('images_to_filter.txt') as images_to_filter:
#     for img_name in images_to_filter.readlines():
#         img_name = img_name.replace('\n', '')
#         print(img_name)
#         image_name = 'images/%s' % img_name
#         #image_name = 'images/57.png'
#         im = Image.open(image_name)
#         im = im.resize((200,200))
#         im.save(image_name)
#
#         # Read the image into a byte array
#         image_data = open(image_name, "rb").read()
#
#         headers = {'Ocp-Apim-Subscription-Key': subscription_key,
#                    'Content-Type': 'application/octet-stream'}
#         params = {'visualFeatures': 'Categories,Description,Color'}
#         response = requests.post(
#             analyze_url, headers=headers, params=params, data=image_data)
#         response.raise_for_status()
#
#         # The 'analysis' object contains various fields that describe the image. The most
#         # relevant caption for the image is obtained from the 'description' property.
#         analysis = response.json()
#         filtered_file = 'filtered_images/%s' % img_name
#         if "plane" in analysis["description"]["tags"] or 'airplane' in analysis["description"]["tags"] or 'jet' in analysis["description"]["tags"] or 'runway' in analysis["description"]["tags"] or 'train' in analysis["description"]["tags"] or 'bird' in analysis["description"]["tags"]:
#             img = Image.new('RGB', (5, 5), color = 'white')
#             img.save(filtered_file)
#         elif "dog" in analysis["description"]["tags"] or "cat" in analysis["description"]["tags"] or "animal" in analysis["description"]["tags"] or "head" in analysis["description"]["tags"] or "man" in analysis["description"]["tags"] or "sitting" in analysis["description"]["tags"] or "standing" in analysis["description"]["tags"]:
#             img = Image.new('RGB', (5, 5), color = 'black')
#             img.save(filtered_file)
#         else:
#             print(analysis)
#             im.save('unclassified/' + img_name)
#             f = open("unclassified_images.txt", "a")
#             f.write(img_name + '\n')

f = open("unclassified_images_2.txt", "w")
with open('unclassified_images.txt') as images_to_filter:
    for img_name in images_to_filter.readlines():
        img_name = img_name.replace('\n', '')
        print(img_name)
        image_name = 'images/%s' % img_name
        #image_name = 'images/57.png'
        im = Image.open(image_name)
        im = im.resize((50,50))
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
        if "plane" in analysis["description"]["tags"] or 'airplane' in analysis["description"]["tags"] or 'jet' in analysis["description"]["tags"] or 'runway' in analysis["description"]["tags"] or 'train' in analysis["description"]["tags"] or 'bird' in analysis["description"]["tags"]:
            img = Image.new('RGB', (5, 5), color = 'white')
            img.save(filtered_file)
        elif "dog" in analysis["description"]["tags"] or "cat" in analysis["description"]["tags"] or "animal" in analysis["description"]["tags"] or "head" in analysis["description"]["tags"] or "man" in analysis["description"]["tags"] or "sitting" in analysis["description"]["tags"] or "standing" in analysis["description"]["tags"]:
            img = Image.new('RGB', (5, 5), color = 'black')
            img.save(filtered_file)
        else:
            print(analysis)
            im.save('unclassified/' + img_name)
            f = open("unclassified_images_2.txt", "a")
            f.write(img_name + '\n')


        # # Display the image and overlay it with the caption.
        # image = Image.open(BytesIO(image_data))
        # plt.imshow(image)
        # plt.axis("off")
        # _ = plt.title(image_caption, size="x-large", y=-0.1)
        # plt.show()

