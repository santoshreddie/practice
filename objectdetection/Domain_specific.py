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

#detect landmarks
domain = 'landmarks'
template_image = open('./eiffel-tower.jpg', 'rb')
analysis = cv_client.analyze_image_by_domain_in_stream(model=domain, image=template_image)
print(analysis)
for land in analysis.result.get('landmarks'):
    print(land['name'])


#detect famous people
def display_result(image, result, text_color = 'red', line_color = 'white', line_width = 5):

    img = Image.open(io.BytesIO(image.content))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 15)

    for object in  result:
        confidence = '{0:.0f}%'.format(object['confidence'] * 100)
        name = object['name']
        rect = object['faceRectangle']
        left = rect['left']
        top = rect['top']
        right = rect['width'] + left
        bottom = rect['height'] + top
        draw.rectangle(
            ((left, top), (right, bottom)),
            outline=line_color,
            width=line_width
        )

        draw.text((right + 4, top), 'name:' + name, fill=text_color, font=font)
        draw.text((right + 4, top + 35), 'confidence:' + confidence, fill=text_color, font=font)

    img.show()

time.sleep(5)

domain = "celebrities"
image_url = 'https://cdn.ceoworld.biz/wp-content/uploads/2020/11/Elon-Musk-2.jpg'
analysis = cv_client.analyze_image_by_domain(model=domain, url = image_url)
print(analysis.result)

if analysis.result:
    img_response = requests.get(image_url)
    display_result(img_response, analysis.result['celebrities'],text_color='#f58916')





