import face_recognition
import cv2
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import os
from imutils.video import VideoStream
import imutils
import pickle
#  import AAR API  part
import sys
import time
import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import firestore

class aarApi:
    def __init__(self):
        self.version = 1
        self.DATA_NAME_COLLECTION = "messages"
        self.DATA_PATH_JSON_FILE = "./Admin_SDK.json"
        self.DATA_TEXT = ""
        self.DATA_OFSET = 2000000000
        self.JSON_CONFIG = {
            "type": "service_account",
            "project_id": "sj2-dashboard-web",
            "private_key_id": "aeb12090b7dc1a33195741b6cfb7a941cc8caa98",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC02jcPJUGO1tMp\nW5C2frgkXQIFIy1cywDQarETnLcjDrAfg/jV9iMRDWm3oSY+TDpk7YN5859Ywd3U\n4lqp63/KQLwHHHUUEysmU78SMwiy7j/dNFKJOHiFxyek1ipTnoM53OimwCoNp/DD\nYN4GNfZTnUThmYITLhlnfftVc6lA1edtKrvpnBJG1grbo9KFS+9nbehrgU7Y/pYZ\nIfsIhiMyVP8pvtJQMMINLxSxxvs5bpC8dz7aA4J5n1UGB+bU4bCKXHtC9Io7pAfk\nEr1e2rjXt86ZcFx59BxJQdkloeoHYzgaQALP5Mnscyav8w4/7Vq02wpkl16PJONi\nUBEDjbuDAgMBAAECggEAG3+2sYHbtwlpMDexCF66RyUxQnC33A0uAYLHjBDfM+Bu\n3Uvm0TnM2THt6jMBqqVSl7gZrrhheVB5F36XhJC/bJRtQrOMBdJoVDqVqgHCh9p8\nMXlcN2szwDupBoJeCzrl/y1c3sYHXu4zSLH48H7SBqK6L4d05M+0oyzfw32DtczP\nIxLu7Krr2jhNjiZ0epX97QEsoTbE0C6D6/uQu8ngacxU1fXaqHAuRNrxN56SP1ya\nnYgdSwqzpxGLVcHIqnh3V2GJfhbubmrys85t0O4NCSsnEyns2G1yqiVHGUcWfoWV\nfDghUnKvzJDeYV16Cwh7PbWz8mbfN10zw2guQERpAQKBgQDattSkoTLrF8X0Xtqt\nwtxa/Lah8lciokCgd3ry98jSpWlb3zS2K314rYjad+vhng7FBoPWzBZioCqDUaFp\nboCmdvkRSE+/dg6CTg09bo/7MY1rKR+QbaZgt4+MVY5wfyNi/1HphUV4SNU9Rced\ncbo8JpeF1mZaxL79YmAgB+hYAwKBgQDTrwNK2k7IJzkyjgyQPry9NmifRfrtomz7\nc0UIIiQ/u1/XvhMzfOx0Rl1yMJzofVIhGbzEvVZOiK6jBLQ3dyaz0BwM9yopJch2\nOtGkOrGAWOlCHFxonnjCzGZAan5MnE+oQXL6k8LkoV1auhg9YwiYcw8/ZT8Ttlli\nWVbw5Ph2gQKBgF9V6LTmS0Ksty4BFsM9OD41AArxjsfa/96ylhZIqfIgBh/02I47\nwNKUmh3Yvio3cmqxn1BG388Xz9A0Ce7iKxPkska1RYXImSR1j1Hi2sH85I78evTC\nxw5LlTfvp0okMTGa54KqBBEddk3iF9PqWeqUS+IcBbu1HSdn9UyhBccvAoGBAJCb\nRCKEU8FDmj1A8LAxS3nuizYS9kIT7WMw8X2G5UBsXiLhg/huZJFh6EAzmVzxD4Px\nMxUrSqRHlxViB0LEsLmxdxgcWL7XQsQRllkch1loY6B4A2CssU5Rl6B1n2XyejA0\n1bj76+2HlmB+NETrPFn4b/gc0CRFM3aOFWhm4p0BAoGANLWdjAGJDZGcoXHfgEpL\nboWOf5qbjexamhWByKRxvXrL22y5s0JaoKFLTkHnFI9IWN4rghcikLaYVH5IzlEc\nMeSBvFWpgHjIoYM2tJu/cVtz/rFYdBR/q4baY9S+hVDcmC8Y2uF+782zGHUgWr8a\nBGa/KmihfOBboKSyE9BgjgU=\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-adzvd@sj2-dashboard-web.iam.gserviceaccount.com",
            "client_id": "104648854302579403876",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-adzvd%40sj2-dashboard-web.iam.gserviceaccount.com"
        }

    def sendMessage(self, data_name, data_text):
        cred = credentials.Certificate(self.JSON_CONFIG)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%d - %b - %Y ( %H : %M : %S )")
        # secondsSinceEpoch = 1
        secondsSinceEpoch = time.time()
        secondsSinceEpoch = self.DATA_OFSET - secondsSinceEpoch
        doc_ref = db.collection(
            u'' + self.DATA_NAME_COLLECTION).document(str(secondsSinceEpoch))
        data = {
            u'name': u''+data_name,
            u'timestamp': u''+str(timestampStr),
            u'text': u''+data_text,
            u'createAt': secondsSinceEpoch
        }
        doc_ref.set(data)
# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.
# construct the argument parser and parse the arguments
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    protocol = aarApi()
    ap.add_argument("-v", "--video", help="path to the video file")
    args = vars(ap.parse_args())
    frameSize = (640, 360)
    areaFrame = frameSize[0] * frameSize[1]
    MinCountourArea = areaFrame * 0.0111  #Adjust ths value according to your usage
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()

    #camera.crop = (0.25, 0.25, 0.5, 0.5)
    camera.crop = (0.22, 0.10, 0.40, 0.40)
    camera.rotation = 180
    camera.hflip = False
    camera.resolution = (640, 360)
    camera.framerate = 30
    camera.brightness = 65
    #camera.roi = (0.5,0.5,0.25,0.25)
    #camera.brightness = 60
    rawCapture = PiRGBArray(camera, size=(640, 360))
    # Get a reference to webcam #0 (the default one)
    namefile = None
    if args["video"] is None :
        #camera = VideoStream(src=0, usePiCamera=True, resolution=frameSize, framerate=15).start()
        namefile = 'camera'
    else :
        camera = cv2.VideoCapture(args["video"])
        namefile = args["video"]
    known_face_encodings = []
    known_face_names = []
    pathKnownImg = "encodings.pickle"
    data = pickle.loads(open(pathKnownImg, "rb").read())
    known_face_encodings = data["encodings"]
    #known_face_names = data["name"]

    # Create arrays of known face encodings and their names
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    motion_flag = False
    idle_time = 0
    namePre = ""
    for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        if args["video"] is None :
            #frame = camera.read()
            #frame = imutils.rotate(frame, 180)
            frame = image.array
        else:
            _,frame = camera.read()
            if (frame is None):
                # not connect camera
                break
            x = 300
            y = 300
            frame = frame[y:y+450, x:x+800]
            frame = imutils.resize(frame, width=frameSize[0])

        # Grab a single frame of video
        # Only process every other frame of video to save time
        if process_this_frame :
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::1]
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding,0.4)
                name = "Unknown"
                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}
                    # for i in matchedIdxs:
                    print (matchedIdxs)
                    name = data["names"][matchedIdxs]
                    counts[name] = counts.get(name, 0) + 1
                    name = max(counts, key=counts.get)
                    face_names.append(name)
                    if ( matchedIdxs == 5):
                        msg_name = "Khajornsak Promwiset 60515007"
                        protocol.sendMessage(msg_name, matchedIdxs)
                    elif (matchedIdxs == 16):
                        msg_name = "kan"
                        protocol.sendMessage(msg_name, matchedIdxs)
                
        if idle_time%5==0:
            process_this_frame = True

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        # Display the resulting image
        cv2.imshow('Video', frame)
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        idle_time += 1
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
