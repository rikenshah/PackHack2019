import requests
from PIL import Image
from io import BytesIO
import operator
import json


def face_detect(ans_dict, image_path):
    print("Start Face Detect")
    # Replace <Subscription Key> with your valid subscription key.
    subscription_key = "4bf52f897b004b5ca614af2a39b82351"
    assert subscription_key

    vision_base_url = "https://eastus2.api.cognitive.microsoft.com/face/v1.0/"

    analyze_url = vision_base_url + "detect"

    # Set image_path to the local path of an image that you want to analyze.

    # Read the image into a byte array
    image_data = open(image_path, "rb").read()
    headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
                'Content-Type': 'application/octet-stream'}
    params     = {'returnFaceAttributes': 'emotion'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    # The 'analysis' object contains various fields that describe the image.
    analysis = response.json()
    # emotion = []
    # print(analysis)
    if analysis:
        for face in analysis:
            # emotion.append(max(dict(face["faceAttributes"]["emotion"]).items(), key=operator.itemgetter(1))[0])
            emotion = max(dict(face["faceAttributes"]["emotion"]).items(), key=operator.itemgetter(1))[0]
    else:
        emotion = ""
    print(emotion)
    ans_dict['emotion'] = emotion

if __name__=='__main__':
    face_detect()