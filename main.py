from multiprocessing import Process, Lock
from face_detect_api_call import face_detect
from vision_analyze_api_call import image_analyze
from text_recognize_api_call import text_recognize
import sys

def main():
    lock = Lock()
    p_face_detect = Process(target=face_detect, args = [lock])
    p_image_analyze = Process(target=image_analyze, args = [lock])
    p_text_recognize = Process(target=text_recognize, args = [lock])
    p_face_detect.start()
    p_image_analyze.start()
    p_text_recognize.start()
    p_face_detect.join()
    p_image_analyze.join()
    p_text_recognize.join()

if __name__=='__main__':
    main()