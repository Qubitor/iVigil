from DB_funtions import select,insert,update
select=select()
insert=insert()
update=update()
from datetime import datetime
import face_recognition
import cv2
import os
# from utils import create_csv
import glob
from random import randint

video_capture = cv2.VideoCapture(0)
# Load some sample pictures and learn how to recognize them.
# list contains face encoded data from given sample images
known_faces = []
#this list contains  names/id of an encoded data respectively
known_face_names = []
#loads the dataset( sample images) in the given directory sucha as "img_data/"
for img in glob.glob("img_data/*.jpg"):
    # Load a sample picture and learn how to recognize it.
    image = face_recognition.load_image_file(img)
    data = face_recognition.face_encodings(image)[0]

    known_faces.append(data)
    name=img.split('/')
    user_name, ext = os.path.splitext(name[1])
    known_face_names.append(user_name)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0
current_path = os.getcwd()
counter = 0
counter1 = 0

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    frame_number += 1
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

        # If you had more than 2 faces, you could make this logic a lot prettier
        # but I kept it simple for the demo
        name = None
        if True in match:
            first_match_index = match.index(True)
            name = known_face_names[first_match_index]
            print (name)
            data=select.select_user(name)
            print ("*"*60)
            print ("\t\t::USER DISCRIPTIONS::")
            print ("*"*60)
            print ("USER ID  :",data[1])
            time=str(data[2])
            print ("LAST RECOGNIZED TIME :",time[11:],time[0:11])
            print ("*"*60,'\n\n')
            current_time=datetime.now()
            update.update_time_stamp(current_time,name)
        else:
            ret, frame = video_capture.read()
        # store the new image with randon name in the directory "img_data/" 
            # id=randint(0,10000000)
            current_time=datetime.now()
            id=insert.create_new_user(current_time)
            filename='img_data/'+str(id)+'.jpg'
            out = cv2.imwrite(filename, frame)
            # Load a new image and learn how to recognize it.
            image = face_recognition.load_image_file(filename)
            data = face_recognition.face_encodings(image)[0]
            known_faces.append(data)
            name=filename.split('/')
            user_name, ext = os.path.splitext(name[1])
            known_face_names.append(user_name)
            known_face_names.append(filename)
            
            print ("new face recognized Time:",current_time)
        #it will insert and update the time stamp of an user's into database

            # os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem  WARNING !!!!" "safe_quit"'%())
            os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem WARNING: A NEW PERSON HAS ENTERED !!!!  " "safe_quit" ')
            os.system(' telegram-cli -k server.pub -W -e "send_photo Alertsystem %s" "safe_quit"' %(filename) )
            os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem NEW USER_ID: %s " "safe_quit" '%(id))

            print (id)
            data=select.select_user(id)
            print ("*"*60)
            print ("\t\t::USER DISCRIPTIONS::")
            print ("*"*60)
            print ("USER ID  :",data[1])
            time=str(data[2])
            print ("LAST RECOGNIZED TIME :",time[11:],time[0:11])
            print ("*"*60,"\n\n\n")
            os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem TIME STAMP: %s " "safe_quit" '%(time))
            name=user_name
        face_names.append(name)
    # Label the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        crop_img = frame[top:bottom, left:right]
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('face_recog_crop', frame)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# All done!
cv2.destroyAllWindows()


