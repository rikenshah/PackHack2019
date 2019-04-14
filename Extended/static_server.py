import socket
from vision_analyze_api_call import image_analyze
import sys
import pyttsx3
from picamera import PiCamera
from crop import crop_image

engine = pyttsx3.init()
engine.setProperty('rate', 145)
engine.setProperty('volume', 1)
engine.setProperty('voice', 'english+f1')
#camera = PiCamera()
#camera.rotation = 270
#camera.start_preview(alpha=200)

bind_ip = '0.0.0.0'
bind_port = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

print('Listening on {}:{}'.format(bind_ip, bind_port))

client_sock, address = server.accept()
while True:
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    data = client_sock.recv(1024)
    if int(data) == 1:
        print("GOt 1")
    elif int(data) == 2:
        print("GOt 2")
    elif int(data) == 3:
        print("GOt 3")
    elif int(data) == 4:
        print("GOt 4")
    else:
        continue
    print(data)

    image_path = sys.argv[1]
    if !os.path.exists(image_path):
        sys.exit()

    end_result = {'description':''}

    # camera.start_preview(alpha=200)
    #camera.capture(image_path)
    # camera.stop_preview()

    crop_image(image_path, int(data))
    image_analyze(end_result, image_path)
    print(end_result)
    if end_result["description"]:
        engine.say(end_result["description"])
        engine.runAndWait()
    else:
        engine.say('Nothing to describe in the image.')

socket.close()
