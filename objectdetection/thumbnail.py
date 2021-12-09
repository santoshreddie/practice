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

image2 = 'https://i.redd.it/mif0yeq2e2381.jpg'

response = cv_client.generate_thumbnail(200, 200, image2, smart_cropping=True, model_version="latest", custom_headers= None, raw=False, callback=None)

with open("thumb.png", 'wb') as fp:
    for chuck in response:
        fp.write(chuck)


