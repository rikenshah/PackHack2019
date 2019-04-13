from multiprocessing import Process
from face_detect_api_call import face_detect
from vision_analyze_api_call import image_analyze
import sys

def main():
    p_face_detect = Process(target=face_detect)
    p_face_detect.start()
    p_image_analyze = Process(target=image_analyze)
    p_image_analyze.start()
    p_face_detect.join()
    p_image_analyze.join()

if __name__=='__main__':
    main()