import requests
from PIL import Image
from io import BytesIO
import pyttsx3
import json


def image_analyze():
    print("Start Image Analyze")
    # Replace <Subscription Key> with your valid subscription key.
    subscription_key = "2b04c53c5c59481e82fbf2b164ed5838"
    assert subscription_key

    vision_base_url = "https://eastus2.api.cognitive.microsoft.com/vision/v2.0/"

    analyze_url = vision_base_url + "analyze"

    # Set image_path to the local path of an image that you want to analyze.
    image_path = "images/Notice.jpg"

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
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    print(image_caption)

    with open('end_result.json', 'r') as f:
        end_result = json.load(f)
        
    end_result["description"] = image_caption
    with open('end_result.json', 'w') as f:
        json.dump(end_result, f)


if __name__=='__main__':
    image_analyze()

