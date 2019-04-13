from multiprocessing import Process, Manager
from face_detect_api_call import face_detect
from vision_analyze_api_call import image_analyze
from text_recognize_api_call import text_recognize
import sys
import pyttsx3
from gpiozero import Button
from picamera import PiCamera

class ButtonPressed(Exception): pass

def main():
    global end_result
    global engine
    global green_pressed
    global red_pressed
    global camera
    global button_green
    global button_red
    global button_yellow
    image_path = "images/buttonrpi-yellow.jpg"
    
    camera.start_preview(alpha=200)
    
    button_yellow.wait_for_press()
    camera.capture(image_path)
    camera.stop_preview()

    p_face_detect = Process(target=face_detect, args = [end_result, image_path])
    p_image_analyze = Process(target=image_analyze, args = [end_result, image_path])
    p_text_recognize = Process(target=text_recognize, args = [end_result, image_path])
    p_face_detect.start()
    p_image_analyze.start()
    p_text_recognize.start()
    p_face_detect.join()
    p_image_analyze.join()
    p_text_recognize.join()
    
    print(end_result)

    if end_result["description"]:
        engine.say(end_result["description"])
        engine.runAndWait()

    if end_result["emotion"]:
        engine.say("A face is detected, do you want to know the emotion?")
        engine.runAndWait()
        green_pressed, red_pressed = False, False
        while True:
            button_green.when_pressed = emotion_yes_pressed
            button_red.when_pressed = no_pressed
            #print("GREEN EMOTION" + str(green_pressed))
            if green_pressed or red_pressed:
                break

    elif end_result["text"]:
        engine.say("Image has some text, do you want to listen?")
        engine.runAndWait()
        green_pressed, red_pressed = False, False
        while True:
            button_green.when_pressed = text_yes_pressed
            button_red.when_pressed = no_pressed
            #print("GREEN TEXT" + str(green_pressed))
            if green_pressed or red_pressed:
                break
        

def emotion_yes_pressed():
    global engine
    global green_pressed
    engine.say(end_result["emotion"])
    engine.runAndWait()
    green_pressed = True


def text_yes_pressed():
    global engine
    global green_pressed
    engine.say(end_result["text"])
    engine.runAndWait()
    green_pressed = True


def no_pressed():
    global red_pressed
    red_pressed = True


def cb(name):
    print(name)
    
    
if __name__=='__main__':
    manager = Manager()
    engine = pyttsx3.init()
    camera = PiCamera()
    button_green = Button(17)
    button_red = Button(15)
    button_yellow = Button(18)
    engine.connect('started-utterance', cb)
    while True:
        green_pressed = False
        red_pressed = False  
        end_result = manager.dict()
        end_result['description'] = ''
        end_result['text'] = ''
        end_result['emotion'] = ''

        main()
