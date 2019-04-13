from multiprocessing import Process
from face_detect_api_call import face_detect
from vision_analyze_api_call import image_analyze
import sys

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

if __name__=='__main__':
    main()