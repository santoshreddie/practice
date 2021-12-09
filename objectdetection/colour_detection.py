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

credintials = json.load(open('authentication.json'))
API_KEY = credintials["API_KEY"]
ENDPOINT = credintials["ENDPOINT"]

cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

'''
Detect Color - remote
This example detects the different aspects of its color scheme in a remote image.
'''

image2 = 'https://preview.redd.it/lh2sgtctub281.jpg?width=1080&format=pjpg&auto=webp&s=8cb7d2a701f8fcca80155d972f1c2d66da80ba05'

print("===== Detect Color - remote =====")
# Select the feature(s) you want
remote_image_features = ["color"]
# Call API with URL and features
detect_color_results_remote = cv_client.analyze_image(image2, remote_image_features)

# Print results of color scheme
print("Getting color scheme of the remote image: ")
print("Is black and white: {}".format(detect_color_results_remote.color.is_bw_img))
print("Accent color: {}".format(detect_color_results_remote.color.accent_color))
print("Dominant background color: {}".format(detect_color_results_remote.color.dominant_color_background))
print("Dominant foreground color: {}".format(detect_color_results_remote.color.dominant_color_foreground))
print("Dominant colors: {}".format(detect_color_results_remote.color.dominant_colors))