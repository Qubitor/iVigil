
from datetime import datetime
import face_recognition
import cv2
import os
# from utils import create_csv
import glob
import numpy
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_data = []
face_name_list = []
for img in glob.glob("iSee/static/img_data/accept_list/*.jpg"):
    # Load a sample picture and learn how to recognize it.
    image = face_recognition.load_image_file(img)
    data = face_recognition.face_encodings(image)[0]
    face_data.append(data)
    name=img.split('/')
    user_name, ext = os.path.splitext(name[4])
    face_name_list.append(user_name)
for img in glob.glob("iSee/static/img_data/reject_list/*.jpg"):
    # Load a sample picture and learn how to recognize it.
    image = face_recognition.load_image_file(img)
    data = face_recognition.face_encodings(image)[0]
    face_data.append(data)
    name=img.split('/')
    user_name, ext = os.path.splitext(name[4])
    face_name_list.append(user_name)
for img in glob.glob("iSee/static/img_data/wait_list/*.jpg"):
    # Load a sample picture and learn how to recognize it.
    image = face_recognition.load_image_file(img)
    data = face_recognition.face_encodings(image)[0]
    face_data.append(data)
    name=img.split('/')
    user_name, ext = os.path.splitext(name[4])
    face_name_list.append(user_name)
face_locations = []
face_encodings = []
face_names = []
frame_number = 0
from random import randint
current_path = os.getcwd()
counter = 0
counter1 = 0
video_capture=cv2.VideoCapture(0)
def demo():
    i=1
    while True:
        ret, frame = video_capture.read()
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            match = face_recognition.compare_faces(face_data, face_encoding, tolerance=0.50)
            name = None
            if True in match:
                first_match_index = match.index(True)
                name = face_name_list[first_match_index]
                print ("*"*60)
                print ("\t\t::USER DISCRIPTIONS::")
                print ("*"*60)
                print ("USER ID  :",name)
                time=str(datetime.now())
                print ("RECOGNIZED TIME :",time[11:],time[0:11])
                print ("*"*60,'\n\n')
                current_time=datetime.now()
            else:
                # name="unknow"
                gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                faces=face_cascade.detectMultiScale(gray,1.3,5)
                for (top, right, bottom, left) in faces:
                    fram=frame[right-50:right+left+50,top-50:top+bottom+100]
                    filename="temp.jpg"
                    out = cv2.imwrite(filename, fram)
                    face_locations = face_recognition.face_locations(fram)
                    face_encodings = face_recognition.face_encodings(fram, face_locations)
                    for face_encoding in face_encodings:
                        match = face_recognition.compare_faces(face_data, face_encoding, tolerance=0.50)
                        name = None
                        if True in match:
                            first_match_index = match.index(True)
                            name = face_name_list[first_match_index]
                        else:
                            current_time=datetime.now()
                            id=randint(0, 100000)
                            filename='iSee/static/img_data/wait_list/'+id+'.jpg'
                            out = cv2.imwrite(filename, fram)               
                            image = face_recognition.load_image_file(filename)
                            data = face_recognition.face_encodings(image)[0]
                            face_data.append(data)
                            face_name_list.append(id)   
                            print ("New face recognized Time:",current_time)
                            data=select.select_user(id)
            face_names.append(name)
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                if not name:
                    continue
                if('wid_'in name):
                    c=(0,165,255)
                elif('aid_'in name):
                    c=(34,139,34)
                else:
                    c= (0, 0, 255)
                cv2.rectangle(frame, (left, top), (right, bottom),c, 2)
                crop_img = frame[top:bottom, left:right]
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), c, cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                cv2.imshow("iVigil",frame)
                cv2.waitKey(10)

demo();