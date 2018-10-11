# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.http import StreamingHttpResponse

from django.template import Context
from django.template.loader import render_to_string, get_template
from DB_funtions import select, insert, update,delete
from ip_config import local_ip
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
current_path = os.getcwd()
counter = 0
counter1 = 0

from django.shortcuts import render
from django.views.decorators.gzip import gzip_page

def base(request):
	return render(request, 'base.html')

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def demo(request):

	subject, from_email, to = 'ALERT FROM iVigil system', 'suresh@zoogle.com.sg', 'sureshiknow@gmail.com'

	html_content = render_to_string('mail.html', {'data':'suresh'}) # render with dynamic value
	text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

	# create the email, and attach the HTML version as well.
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	return HttpResponse('Successfully')

def stream_video(request):
	# data=StreamingHttpResponse(stream_response_generator(),content_type="multipart/x-mixed-replace;boundary=frame")
	return StreamingHttpResponse(stream_response_generator(),content_type="multipart/x-mixed-replace;boundary=frame")

def stream_response_generator():
#this makes a web cam object 
    i=1
    video_capture=cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        # cv2.imwrite("test.jpg", frame)
        # frame_number += 1
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            match = face_recognition.compare_faces(face_data, face_encoding, tolerance=0.50)
            name = None
            if True in match:
                first_match_index = match.index(True)
                name = face_name_list[first_match_index]
                if('aid_' in name):
                    try:
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
                    except:
                        pass
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
                            id=insert.create_new_user(current_time)
                            filename='iSee/static/img_data/wait_list/'+id+'.jpg'
                            out = cv2.imwrite(filename, fram)               
                            # out = cv2.imwrite(filename, frame)
                            image = face_recognition.load_image_file(filename)
                            data = face_recognition.face_encodings(image)[0]
                            face_data.append(data)
                            face_name_list.append(id)   
                            print ("new face recognized Time:",current_time)
                            data=select.select_user(id)
                            os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem WARNING: A NEW PERSON HAS ENTERED !!!!  " "safe_quit" ')
                            os.system(' telegram-cli -k server.pub -W -e "send_photo Alertsystem %s" "safe_quit"' %(filename) )
                            os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem NEW USER_ID: %s " "safe_quit" '%(id))
                            os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem Accept : http://%s:8000/iSee/accept/%s " "safe_quit" '%(local_ip,id))
                            os.system(' telegram-cli -k server.pub -W -e "msg Alertsystem Reject : http://%s:8000/iSee/reject/%s " "safe_quit" '%(local_ip,id))
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
        imgencode=cv2.imencode('.jpg',frame)[1]
        stringData=imgencode.tostring()
        yield (b'--frame\r\n'
			b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
        i+=1
    del(camera)


def accept(request,user_id):
    s=user_id
    user_id=user_id[4:]
    import shutil
    old_file='iSee/static/img_data/wait_list/'+"wid_"+str(user_id)+'.jpg'
    id=insert.accept_user(user_id)
    new_file='iSee/static/img_data/accept_list/'+str(id)+'.jpg'
    shutil.copy2(old_file, new_file)
    os.remove(old_file)
    name=new_file.split('/')
    user_name, ext = os.path.splitext(name[4])
    for i in range(0,len(face_name_list)):
        if(face_name_list[i]==s):
            face_name_list[i]=user_name
    print('*'*60)
    print("a New User is Accepted with id "+ str(user_name) +" by *admin* ")
    print('*'*60)
    return HttpResponse("user "+user_id+" is Accepted Successfully") 
	# else:
		# return HttpResponse("user "+res+" is already accepted or not exits in reject list") 
def waiting_list(request):
	waiting_list=[]
	data=select.select_waiting_list()
	data=reversed(data)
	for i in data:
		a={'id':i[1]}
		waiting_list.append(a)
	return render(request,'alert.html',{'data':waiting_list,'ip':local_ip})   
	  

def reject(request,user_id):
	user_id=user_id[4:]
	import shutil
	old_file='iSee/static/img_data/wait_list/'+"wid_"+str(user_id)+'.jpg'
	id=insert.reject_user(user_id)
	new_file='iSee/static/img_data/reject_list/'+str(id)+'.jpg'
	shutil.copy2(old_file, new_file)
	name=new_file.split('/')
	user_name, ext = os.path.splitext(name[4])
	os.remove(old_file)
	s='wid_'+user_id
	for i in range(0,len(face_name_list)):
		if(face_name_list[i]==s):
			face_name_list[i]=user_name
	return HttpResponse(user_id+"Rejected")



def send_mail(request):
    subject = "I am an HTML email"
    to = ['sureshiknow@gmail.com']
    from_email = 'qubitor.python@gmail.com'

    ctx = {
        'user': 'buddy',
        'purchase': 'Books'
    }

    message = get_template('mail.html').render(Context(ctx))
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

    return 0











