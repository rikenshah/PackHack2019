from multiprocessing import Process
from face_detect_api_call import face_detect
from vision_analyze_api_call import image_analyze
from text_recognize_api_call import text_recognize
import sys
import pyttsx3
from gpiozero import Button

def main():
    p_face_detect = Process(target=face_detect)
    p_image_analyze = Process(target=image_analyze)
    p_text_recognize = Process(target=text_recognize)
    p_face_detect.start()
    p_image_analyze.start()
    p_text_recognize.start()
    p_face_detect.join()
    p_image_analyze.join()
    p_text_recognize.join()
    
    with open('end_result.json', 'r') as f:
        end_result = json.load(f)

    engine = pyttsx3.init()
    button_green = Button(17)
    button_red = Button(15)
    engine.say(end_result["description"])
    engine.runAndWait()

    # if end_result["emotion"]:
    #     engine.say("A face is detected, do you want to know the emotion?")
    #     engine.runAndWait()
    #     time.sleep(5)
    #     if button_green.is_pressed():
    #         engine.say("Emotion is " + end_result["emotion"])


if __name__=='__main__':
    main()