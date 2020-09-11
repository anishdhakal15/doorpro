import cv2
import threading
import face_recognition
import os
import time

KNOWN_FACES_DIR = 'known_faces'
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'cnn'

print('Loading known faces...')
known_faces = []
known_names = []
def dooropen():
    with open("dooropen","w") as aa:
        aa.write("")
def doorclose():
    with open("doorclose","w") as bb:
        bb.write("")

# We oranize known faces as subfolders of KNOWN_FACES_DIR
# Each subfolder's name becomes our label (name)
def loaddata():
    while(True):
        for name in os.listdir(KNOWN_FACES_DIR):

            # Next we load every file of faces of known person
            for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):

                # Load an image
                image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')

                # Get 128-dimension face encoding
                # Always returns a list of found faces, for this purpose we take first face only (assuming one face per image as you can't be twice on one image)
                encoding = face_recognition.face_encodings(image)[0]

                # Append encodings and name
                known_faces.append(encoding)
                known_names.append(name)
datastart= threading.Thread(target=loaddata)

video_capture = cv2.VideoCapture(0)

# Initialize variables
face_locations = []
datastart.start()
def compare():
        # Grab a single frame of video
    ret, frame = video_capture.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]
        

        # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    for face_encoding, face_location in zip(encodings, face_locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results: 
            return known_names[results.index(True)]
                
#com= threading.Thread(target=compare)
#com.start()

matchaa=None
while True:
    matchaa=compare()
    if matchaa !=None:

        print(matchaa,"dooropen")
        dooropen()
        time.sleep(6)
        print("doorclosed")
        doorclose()
        matchaa=None




video_capture.release()