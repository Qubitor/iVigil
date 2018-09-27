# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from DB_funtions import select, insert, update
from django.http import StreamingHttpResponse
import time
select=select()
insert=insert()
update=update()
from datetime import datetime
import face_recognition
import os
import glob
import cv2
import sys
import numpy
known_faces = []
known_face_names = []
for img in glob.glob("img_data/accept_list/*.jpg"):
    # Load a sample picture and learn how to recognize it.
    image = face_recognition.load_image_file(img)
    data = face_recognition.face_encodings(image)[0]
    known_faces.append(data)
    name=img.split('/')
    user_name, ext = os.path.splitext(name[2])
    known_face_names.append(user_name)
face_locations = []
face_encodings = []
face_names = []
frame_number = 0
current_path = os.getcwd()
counter = 0
counter1 = 0
from django.shortcuts import render
from django.views.decorators.gzip import gzip_page

def base(request):
	# print "HALO"
	return render(request, 'base.html')

def demo(request):
	data=stream_video(request)
	return render(request,'stream.html')

def stream_video(request):
    return StreamingHttpResponse(stream_response_generator(),content_type="multipart/x-mixed-replace;boundary=frame")


def stream_response_generator():
	camera_port=0
	ramp_frames=100
	video_capture=cv2.VideoCapture(camera_port) #this makes a web cam object 
	i=1
	while True:
		ret, frame = video_capture.read()
		# cv2.imwrite("test.jpg", frame)
		# frame_number += 1
		face_locations = face_recognition.face_locations(frame)
		face_encodings = face_recognition.face_encodings(frame, face_locations)
		face_names = []
		for face_encoding in face_encodings:
			match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)
			name = None
			if True in match:
				first_match_index = match.index(True)
				name = known_face_names[first_match_index]
				data=select.select_user(name)
				print ("*"*60)
				print ("\t\t::USER DISCRIPTIONS::")
				print ("*"*60)
				print ("USER ID  :",data[1])
				time=str(data[2])
				print ("RECOGNIZED TIME :",time[11:],time[0:11])
				print ("*"*60,'\n\n')
				current_time=datetime.now()
				update.update_time_stamp(current_time,name)
			else:
				ret, frame = video_capture.read()
				current_time=datetime.now()
				id=insert.create_new_user(current_time)
				filename='img_data/reject_list/'+id+'.jpg'
				# gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
				# faces=face_cascade.detectMultiScale(gray,1.3,5)
				# for (top, right, bottom, left) in faces:
				# 	out = cv2.imwrite(filename, frame[right-50:right+left+50,top-50:top+bottom+100])
				out = cv2.imwrite(filename, frame)
				# Load a new image and learn how to recognize it.
				# image = face_recognition.load_image_file(filename)
				# data = face_recognition.face_encodings(image)[0]
				# known_faces.append(data)
				# name=filename.split('/')
				# user_name, ext = os.path.splitext(name[2])
				# known_face_names.append(user_name)
	            
				print ("new face recognized Time:",current_time)
	        #it will insert and update the time stamp of an particular user's into database

	            # os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem  WARNING !!!!" "safe_quit"'%())
				os.system(' telegram-cli -k server.pub -W -e "msg Alert WARNING: A NEW PERSON HAS ENTERED !!!!  " "safe_quit" ')
				os.system(' telegram-cli -k server.pub -W -e "send_photo Alert %s" "safe_quit"' %(filename) )
	            # os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem NEW USER_ID: %s " "safe_quit" '%(id))
				os.system(' telegram-cli -k server.pub -W -e "msg Alert Accept : http://192.168.10.4:8000/iSee/accept/%s "  "safe_quit" '%(id))
				os.system(' telegram-cli -k server.pub -W -e "msg Alert Reject : http://192.168.10.4:8000/iSee/reject/%s " "safe_quit" '%(id))
				print (id)
				data=select.select_user(id)
				# print ("*"*60)
				# print ("\t\t::USER DISCRIPTIONS::")
				# print ("*"*60)
				# print ("USER ID:\t\t\t",data[1])
				# time=str(data[2])
				# print ("RECOGNIZED TIME :",time[11:],time[0:11])
				# print ("*"*60,"\n\n\n")
				# os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem TIME STAMP: %s " "safe_quit" '%(time))
				name="unknown"
			face_names.append(name)
			for (top, right, bottom, left), name in zip(face_locations, face_names):
				if not name:
					continue
				cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
				crop_img = frame[top:bottom, left:right]
				cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
				font = cv2.FONT_HERSHEY_DUPLEX
				cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
		imgencode=cv2.imencode('.jpg',frame)[1]
		stringData=imgencode.tostring()
		yield (b'--frame\r\n'
			b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
		i+=1
	del(camera)


def accept(request,user_id):
	# print "HALO"
	res=user_id
	import shutil
	old_file='img_data/reject_list/'+str(user_id)+'.jpg'
	new_file='img_data/accept_list/'+str(user_id)+'.jpg'
	exists = os.path.isfile(old_file)
	insert.accept_user(user_id)
	if exists:
		shutil.copy2(old_file, new_file)
		os.remove('img_data/reject_list/'+str(user_id)+'.jpg')
		image = face_recognition.load_image_file(new_file)
		data = face_recognition.face_encodings(image)[0]
		known_faces.append(data)
		name=new_file.split('/')
		print(name)
		user_name, ext = os.path.splitext(name[2])
		print (user_name,ext)
		known_face_names.append(user_name)
		return HttpResponse("user "+res+" is Accepted Successfully") 
	else:
		return HttpResponse("user "+res+" is already accepted or not exits in reject list") 
def alert(request):
	waiting_list=[]
	data=select.select_waiting_list()
	for i in data:
		a={'id':i[1]}
		waiting_list.append(a)
	return render(request,'alert.html',{'data':waiting_list})   
	  

def reject(request,user_id):
	# print "HALO"
	res=user_id
	return HttpResponse(res+"Rejected")
















	
def popup_face_rec(request):
	face_cascade=cv2.CascadeClassifier('/home/suresh/project/iVigil/haarcascade_frontalface_default.xml')
	video_capture = cv2.VideoCapture(0)
	# Load some sample pictures and learn how to recognize them.
	#loads the dataset( sample images) in the given directory sucha as "img_data/"
	for img in glob.glob("img_data/accept_list/*.jpg"):
	    # Load a sample picture and learn how to recognize it.
	    image = face_recognition.load_image_file(img)
	    data = face_recognition.face_encodings(image)[0]

	    known_faces.append(data)
	    name=img.split('/')
	    user_name, ext = os.path.splitext(name[2])
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
	            print("sss::::;",name)
	            print(data)
	            print ("*"*60)
	            print ("\t\t::USER DISCRIPTIONS::")
	            print ("*"*60)
	            print ("USER ID  :",data[1])
	            time=str(data[2])
	            print ("RECOGNIZED TIME :",time[11:],time[0:11])
	            print ("*"*60,'\n\n')
	            current_time=datetime.now()
	            update.update_time_stamp(current_time,name)
	        else:
	            ret, frame = video_capture.read()
	        # store the new image with randon name in the directory "img_data/" 
	            # id=randint(0,10000000)
	            current_time=datetime.now()
	            id=insert.create_new_user(current_time)
	            filename='img_data/reject_list/'+str(id)+'.jpg'
	            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	            faces=face_cascade.detectMultiScale(gray,1.3,5)
	            for (top, right, bottom, left) in faces:
	            	out = cv2.imwrite(filename, frame[right-50:right+left+50,top-50:top+bottom+100])
	            
	            	# out = cv2.imwrite(filename, frame)  
	            # Load a new image and learn how to recognize it.
	            # image = face_recognition.load_image_file(filename)
	            # data = face_recognition.face_encodings(image)[0]
	            # known_faces.append(data)
	            name=filename.split('/')
	            print(name)
	            user_name, ext = os.path.splitext(name[1])
	            # known_face_names.append(user_name)
	            
	            print ("new face recognized Time:",current_time)
	        #it will insert and update the time stamp of an particular user's into database

	            # os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem WARNING: A NEW PERSON HAS ENTERED !!!!  " "safe_quit" ')
	            os.system(' telegram-cli -k server.pub -W -e "send_photo Alertsystem %s" "safe_quit"' %(filename) )
	            # os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem NEW USER_ID: %s " "safe_quit" '%(id))
	            os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem Accept : http://192.168.10.4:8000/iSee/accept/%s " "safe_quit" '%(id))
	            # os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem Reject : http://192.168.10.4:8000/iSee/reject/%s " "safe_quit" ' %(id))

	            # print (id)
	            data=select.select_user(id)
	            print ("*"*60)
	            print ("\t\t::USER DISCRIPTIONS::")
	            print ("*"*60)
	            print ("USER ID:\t\t\t",data[1])
	            time=str(data[2])
	            print ("RECOGNIZED TIME :",time[11:],time[0:11])
	            print ("*"*60,"\n\n\n")
	            # os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem TIME STAMP: %s " "safe_quit" '%(time))
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

	    cv2.imshow('iVigil - Smart Vigilance Systems', frame)
	    # Hit 'q' on the keyboard to quit!
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

	# All done!
	cv2.destroyAllWindows()



	return HttpResponse("sss")