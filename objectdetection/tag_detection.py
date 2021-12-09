#Example code for detecting landmark and celebrities
import os
import io
import json
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes
import requests
from PIL import Image, ImageDraw, ImageFont
import time
from io import BytesIO

credintials = json.load(open('authentication.json'))
API_KEY = credintials["API_KEY"]
ENDPOINT = credintials["ENDPOINT"]

cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))


'''
Detect Objects - remote
This example detects different kinds of objects with bounding boxes in a remote image.
'''
image_url = "https://cdn.vox-cdn.com/thumbor/27fjOG2nixADoyjRzIz38k8r3cg=/0x0:4431x2954/1820x1024/filters:focal(1030x1360:1738x2068):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/66732472/GettyImages_1209347829.0.jpg"
max_descriptions = 10
response = cv_client.describe_image(image_url, max_descriptions)
print("Objects in the picture")
print("*"*70)
for tag in  response.tags:
    print(tag)




