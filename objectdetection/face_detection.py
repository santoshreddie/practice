
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
import matplotlib.pyplot as plt
import matplotlib.patches as patches

credintials = json.load(open('authentication.json'))
API_KEY = credintials["API_KEY"]
ENDPOINT = credintials["ENDPOINT"]

cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

print("===== Detect Faces - remote =====")
# Get an image with faces
#remote_image_url_faces = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/faces.jpg"
# Select the visual feature(s) you want.
# Open image file
image_path = "small-family.jpg"
image = open(image_path, "rb")

img = Image.open(image_path)

# Select visual features you want
img_features = ["faces"]

# Call the API
faces_result = cv_client.analyze_image_in_stream(image, img_features)

# Print the results with gender, age, and bounding box
print("Faces in the remote image: ")
if (len(faces_result.faces) == 0):
    print("No faces detected.")
else:
    for face in faces_result.faces:
        print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
        face.face_rectangle.left, face.face_rectangle.top, \
        face.face_rectangle.left + face.face_rectangle.width, \
        face.face_rectangle.top + face.face_rectangle.height))

# Create figure and axes
fig, ax = plt.subplots()

# Display the image
ax.imshow(img)

print("Faces:")
if (len(faces_result.faces) == 0):
    print("No faces detected.")
else:
    for face in faces_result.faces:
        # Create a Rectangle patch
        rect = patches.Rectangle((face.face_rectangle.left, face.face_rectangle.top), face.face_rectangle.width, face.face_rectangle.height, linewidth=2, edgecolor='r', facecolor='none')

        # Add the patch to the Axes
        ax.add_patch(rect)

plt.show()