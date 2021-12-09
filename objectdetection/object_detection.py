import os
import io
import json
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes
import requests
from PIL import Image, ImageDraw, ImageFont
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches

credintials = json.load(open('authentication.json'))
API_KEY = credintials["API_KEY"]
ENDPOINT = credintials["ENDPOINT"]

cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))
# Open image file
image_path = "apples.jpg"
image = open(image_path, "rb")

img = Image.open(image_path)

# Call API
detect_objects_results = cv_client.detect_objects_in_stream(image)

for obj in detect_objects_results.objects:
    print("object is: {} at location {}, {}, {}, {}".format(obj.object_property, obj.rectangle.x, obj.rectangle.x + obj.rectangle.w, obj.rectangle.y, obj.rectangle.y + obj.rectangle.h))
    print("with confidence: {}".format(obj.confidence))

# Create figure and axes
fig, ax = plt.subplots()

# Display the image
ax.imshow(img)

print("Objects in image:")
if len(detect_objects_results.objects) == 0:
    print("No objects detected.")
else:
    for object in detect_objects_results.objects:
        # Create a Rectangle patch
        rect = patches.Rectangle((object.rectangle.x, object.rectangle.y), object.rectangle.w, object.rectangle.h, linewidth=2, edgecolor='r', facecolor='none')

        # Add the patch to the Axes
        ax.add_patch(rect)

plt.show()