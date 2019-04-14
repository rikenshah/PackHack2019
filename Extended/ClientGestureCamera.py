from lib import Leap
import sys, thread, time
import socket, random
from lib.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

ip_address = '0.tcp.ngrok.io'
port = 11561

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip_address, port))

class SampleListener(Leap.Listener):
    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        finger_direction, f_dir_id = "", '0'
        # Get hands
        for hand in frame.hands:
            # Get fingers
            for finger in hand.fingers:
                if finger.is_extended:
                    # print(finger.direction)
                    if finger.direction[0] < 0:
                        if finger.direction[1] > 0:
                            finger_direction = "top left"
                            f_dir_id = '1'
                        else:
                            finger_direction = "bottom left"
                            f_dir_id = '4'
                    else:
                        if finger.direction[1] > 0:
                            finger_direction = "top right"
                            f_dir_id = '2'
                        else:
                            finger_direction = "bottom right"
                            f_dir_id = '3'
                    print(finger_direction)
        # Get gestures
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)
                # Determine clock direction using the angle between the pointable and the circle normal
                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                    clockwiseness = "clockwise"
                else:
                    clockwiseness = "counterclockwise"
                print("Circle in direction : {}".format(finger_direction))
                s.sendall(f_dir_id.encode())
        time.sleep(0.3)

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
