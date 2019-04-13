import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import operator
from pprint import pprint
import time
# import pyttsx3


def text_recognize():
    # Replace <Subscription Key> with your valid subscription key.
    subscription_key = "2b04c53c5c59481e82fbf2b164ed5838"
    assert subscription_key

    vision_base_url = "https://eastus2.api.cognitive.microsoft.com/vision/v2.0/"

    analyze_url = vision_base_url + "recognizeText"

    # Set image_path to the local path of an image that you want to analyze.
    image_path = "images/TextTest.png"

    # Read the image into a byte array
    image_data = open(image_path, "rb").read()
    headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
                'Content-Type': 'application/octet-stream'}
    params     = {'mode': 'Printed'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    time.sleep(2)

    headers_second = {'Ocp-Apim-Subscription-Key': subscription_key}
    url_second = response.headers["Operation-Location"]
    response_second = requests.get(url_second, headers=headers_second)
    pprint(vars(response_second))


if __name__=='__main__':
    text_recognize()