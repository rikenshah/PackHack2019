import requests
from PIL import Image
from io import BytesIO
import pyttsx3
import json


def image_analyze(ans_dict, image_path):
    print("Start Image Analyze")
    # Replace <Subscription Key> with your valid subscription key.
    subscription_key = "2b04c53c5c59481e82fbf2b164ed5838"
    assert subscription_key

    vision_base_url = "https://eastus2.api.cognitive.microsoft.com/vision/v2.0/"

    analyze_url = vision_base_url + "analyze"

    # Set image_path to the local path of an image that you want to analyze.

    # Read the image into a byte array
    image_data = open(image_path, "rb").read()
    headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
                'Content-Type': 'application/octet-stream'}
    params     = {'visualFeatures': 'Categories,Description,Color'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    # The 'analysis' object contains various fields that describe the image. The most
    # relevant caption for the image is obtained from the 'description' property.
    analysis = response.json()
    # print(analysis)
    if analysis["description"]["captions"]:
        image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    else:
        image_caption = ''
    print(image_caption)
    ans_dict['description'] = image_caption
    with open("output.txt", "a") as f:
        f.write("Description: " + image_caption + "\n---------------------------\n")

if __name__=='__main__':
    image_analyze()

