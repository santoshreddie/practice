import os
import io
import time
import json
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes

credintials = json.load(open('authentication.json'))
key = credintials["API_KEY"]
endpoint = credintials["ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

# Open local image file
image_path = "notes1.jpg"
image = open(image_path, "rb")
# Call the API
read_response = computervision_client.read_in_stream(image, raw=True)
# Get the operation location (URL with an ID at the end)
read_operation_location = read_response.headers["Operation-Location"]
# Grab the ID from the URL
operation_id = read_operation_location.split("/")[-1]
# Retrieve the results 
while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)
# Print the detected text and bounding boxes
if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
                print(line.text)
                print(line.bounding_box)