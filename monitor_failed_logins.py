import win32evtlog
import win32evtlogutil
import win32security
import os
import cv2
from datetime import datetime

def get_failed_logins():
    server = 'localhost'
    logtype = 'Security' 
    hand = win32evtlog.OpenEventLog(server, logtype)

    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)

    failed_logins = []

    events = win32evtlog.ReadEventLog(hand, flags, 0)
    while events:
        for event in events:
            if event.EventID == 4625:  
                failed_logins.append(event)

        events = win32evtlog.ReadEventLog(hand, flags, 0)

    win32evtlog.CloseEventLog(hand)
    return failed_logins
def capture_photo():
    username = os.getenv('USERNAME')
    folder_name = fr"C:\Users\{username}\failed_logins_images"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Created folder: {folder_name}")


    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video device.")
        return

    ret, frame = cap.read()
    if ret:
        filename = os.path.join(folder_name, f"failed_login_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
        if cv2.imwrite(filename, frame):
            print(f"Photo saved as {filename}")
        else:
            print(f"Error: Could not save photo as {filename}")
    else:
        print("Error: Could not capture photo.")

    cap.release()
    cv2.destroyAllWindows()

def take_action():
    os.system('echo "Failed login attempt detected!"')
    capture_photo()

if __name__ == "__main__":
    failed_logins = get_failed_logins()
    if failed_logins:
        take_action()
