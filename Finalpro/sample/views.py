# -*- coding: utf-8 -*-

from collections import Counter
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.template.loader import render_to_string, get_template
from ip_config import local_ip,port
from datetime import datetime
import time
import face_recognition
import os
import glob
import cv2
import csv
import sys
import numpy
face_cascade=cv2.CascadeClassifier('sample/static/opencv/haarcascade_frontalface_default.xml')

accepted_face_data = []
accepted_name_list = []
waiting_face_data = []
waiting_name_list = []
rejected_face_data = []
rejected_name_list = []
# print(waiting_name_list)
# print("^^^^^^^^^^^^^^^^^^^^^^^")
with open('sample/static/trained_data/accepted_list.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
for i in range(1,len(lines)):
    data=lines[i]
    accepted_name_list.append(data[0])
    en=data[1:]
    data=[]
    for k in en:
        data.append(float(k))
    accepted_face_data.append(data)
# with open('sample/static/trained_data/waiting_list.csv', 'r') as readFile:
#     reader = csv.reader(readFile)
#     lines = list(reader)
# for i in range(1,len(lines)):
#     data=lines[i]
#     waiting_name_list.append(data[0])
#     en=data[1:]
#     data=[]
#     for k in en:
#         data.append(float(k))
#     waiting_face_data.append(data)
for img in glob.glob("sample/static/img_data/wait_list/*.jpg"):
    # Load a sample picture and learn how to recognize it.
    image = face_recognition.load_image_file(img)
    data = face_recognition.face_encodings(image)[0]
    waiting_face_data.append(data)
    name=img.split('/')
    user_name, ext = os.path.splitext(name[4])
    r=user_name
    waiting_name_list.append(user_name)
    red=waiting_name_list
    # print(waiting_name_list)


    # print("***********************")
with open('sample/static/trained_data/rejected_list.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
for i in range(1,len(lines)):
    data=lines[i]
    rejected_name_list.append(data[0])
    en=data[1:]
    data=[]
    for k in en:
        data.append(float(k))
    rejected_face_data.append(data)

face_locations = []
face_encodings = []
face_names = []
frame_number = 0
current_path = os.getcwd()
counter = 0
counter1 = 0

from django.shortcuts import render
# from django.views.decorators.gzip import gzip_page

def base(request):
    return render(request, 'base.html')

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# def demo(request):

# 	subject, from_email, to = 'ALERT FROM iVigil system', 'suresh@zoogle.com.sg', 'sureshiknow@gmail.com'

# 	html_content = render_to_string('mail.html', {'data':'suresh'}) # render with dynamic value
# 	text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

# 	# create the email, and attach the HTML version as well.
# 	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
# 	msg.attach_alternative(html_content, "text/html")
# 	msg.send()
# 	return HttpResponse('Successfully')

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
        strs=[]
        face_names = []
        for face_encoding in face_encodings:
            match = face_recognition.compare_faces(accepted_face_data, face_encoding, tolerance=0.60)
            name = None
            if True in match:
                first_match_index = match.index(True)
                name = accepted_name_list[first_match_index]
              
                
            else:
               
                for face_encoding in face_encodings:
                    match = face_recognition.compare_faces(rejected_face_data, face_encoding, tolerance=0.60)
                    name = None
                    if True in match:
                        first_match_index = match.index(True)
                        name = rejected_name_list[first_match_index]
                    else:
                        for face_encoding in face_encodings:
                            match = face_recognition.compare_faces(waiting_face_data, face_encoding, tolerance=0.60)
                            name = None
                            if True in match:
                                first_match_index = match.index(True)
                                name = waiting_name_list[first_match_index]
                            else:
                                gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                                faces=face_cascade.detectMultiScale(gray,1.3,5)
                                for (top, right, bottom, left) in faces:
                                    fram=frame[right-50:right+left+50,top-50:top+bottom+100]
                                    filename="sample/static/temp.jpg"
                                    out = cv2.imwrite(filename, fram)
                                    face_locations = face_recognition.face_locations(fram)
                                    face_encodings = face_recognition.face_encodings(fram, face_locations)
                                    for face_encoding in face_encodings:
                                        match = face_recognition.compare_faces(waiting_face_data, face_encoding, tolerance=0.40)
                                        name = None
                                        if True in match:
                                            first_match_index = match.index(True)
                                            name = waiting_name_list[first_match_index]

                                        else:
                                            current_time=datetime.now()
                                            ts = int(time.time())
                                            id ="wid_"+str(ts)
                                            filename='sample/static/img_data/wait_list/'+id+'.jpg'
                                            out = cv2.imwrite(filename, fram)
                                            # out = cv2.imwrite(filename, frame)
                                            image = face_recognition.load_image_file(filename)
                                            data = face_recognition.face_encodings(image)[0]
                                            waiting_face_data.append(data)
                                            waiting_name_list.append(id)
                                            row = [id]

                                            for i in data:
                                                row.append(float(i))
                                            with open('sample/static/trained_data/waiting_list.csv', 'a') as csvFile:
                                                writer = csv.writer(csvFile)
                                                writer.writerow(row)
                                            csvFile.close()
                                            # print ("new face recognized Time:",current_time)
                                            # data=select.select_user(id)
                                            
            

            strs.append(name)  
            # print(strs) 
              
            d=[]    
            for x in strs:
                if not x:
                    x='bc'
                    print(x)
                # filter(partial(is_not, None),q)
                q=x[0]
                
                # print(q)
                d.append(q)
                # print(d)
                daaa=Counter(d)
                # print(daaa)       
                col = ['a','r','w'] 
                # aas=[]
                for color in col: 
                    # print(daaa[color])
                    s=color,daaa[color]
                    # print(s)
                    
                    if 'a' in s:
                        row = []
                        sa=s
                        row.append(sa)
                        # print(row)
                        
                        with open('sample/static/trained_data/sample.csv', 'r') as readFile:
                            reader = csv.reader(readFile)
                            lines = list(reader)
                            lines = row
                            # print(lines)
                        with open('sample/static/trained_data/sample.csv', 'w') as writeFile:
                            writer = csv.writer(writeFile)
                            writer.writerows(lines)

                        readFile.close()
                        writeFile.close()
                    elif 'w' in s:
                        row = []
                        sa=s 
                        row .append(sa)
                        # row = []
                        # print(row)            
                        with open('sample/static/trained_data/test.csv', 'r') as readFile:
                            reader = csv.reader(readFile)
                            lines = list(reader)
                            lines = row
                            # print(lines)

                        with open('sample/static/trained_data/test.csv', 'w') as writeFile:
                            writer = csv.writer(writeFile)
                            writer.writerows(lines)

                        readFile.close()
                        writeFile.close()
                    elif 'r' in s:     
                        row = []
                        sa=s
                        row.append(sa)
                        # row = []
                        # print(row)            
                        with open('sample/static/trained_data/review.csv', 'r') as readFile:
                            reader = csv.reader(readFile)
                            lines = list(reader)
                            lines = row
                            # print(lines)

                        with open('sample/static/trained_data/review.csv', 'w') as writeFile:
                            writer = csv.writer(writeFile)
                            writer.writerows(lines)

                        readFile.close()
                        writeFile.close()                                
            face_names.append(name)
            print("***********************************")
            print()
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
        # print(red)

        if not face_encodings:
            sample =("a",0)
            row=[sample]
            with open('sample/static/trained_data/sample.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                lines = list(reader)
                lines = row
                # print(lines)
            with open('sample/static/trained_data/sample.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)

            readFile.close()
            writeFile.close()
            print("******************")
            q=('w',0)
            test=[q]
            with open('sample/static/trained_data/test.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                lines = list(reader)
                lines = test
                print(lines)

            with open('sample/static/trained_data/test.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)

            readFile.close()
            writeFile.close()
            print("##########################")

            w=('r',0)
            ded=[w]
            with open('sample/static/trained_data/review.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                lines = list(reader)
                lines = ded
                # print(lines)

            with open('sample/static/trained_data/review.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)

            readFile.close()
            writeFile.close()
            print("^^^^^^^^^^^^")

                # waiting_name_list.remove("wid_")
        else:
            pass
        # # i+=1
    del(camera)


def accept(request,user_id):
    s=user_id
    user_id=user_id[4:]
# wait list csv file has been moved
    import pandas as pd
    df = pd.read_csv("sample/static/trained_data/waiting_list.csv")
    df.loc[df["user_id"]==s, "user_id"] = 'file-moved'
    df.to_csv("sample/static/trained_data/waiting_list.csv", index=False)
    
    import shutil
    old_file='sample/static/img_data/wait_list/'+"wid_"+str(user_id)+'.jpg'
    ts = int(time.time())
    id ="aid_"+str(ts)
    new_file='sample/static/img_data/accept_list/'+id+'.jpg'
    shutil.copy2(old_file, new_file)
    os.remove(old_file)
    name=new_file.split('/')
    user_name, ext = os.path.splitext(name[4])
    for i in range(0,len(waiting_name_list)):
        if(waiting_name_list[i]==s):
            waiting_name_list[i]=user_name
            data=waiting_face_data[i]
    accepted_face_data.append(data)
    accepted_name_list.append(user_name)
    row = [user_name]
    for i in data:
        row.append(float(i))
    with open('sample/static/trained_data/accepted_list.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    print('*'*60)
    print("a New User is Accepted with id "+ str(user_name) +" by *admin* ")
    print('*'*60)
    data=[{'message':user_id+" is Accepted Successfully"}]
    return HttpResponse(json.dumps(data), content_type="application/json")

def waiting_list(request):
    # get_data(request, 's','ssss');
    waiting_list=[]
    # data=(((41, 'wid_1544160905')), (42, 'wid_1544160906'))
    
    with open('sample/static/trained_data/waiting_list.csv') as f: 
        data=[line.split(",")[0] for line in f]
         
    if(data):
        data=reversed(data)
        for i in data:
            a={'id':i}
            waiting_list.append(a)
        return render(request,'alert.html',{'data':waiting_list,'ip':local_ip,'port':port})
    else:
        return 0
import json
def reject(request,user_id):
    s=user_id
    user_id=user_id[4:]
    import pandas as pd
    df = pd.read_csv("sample/static/trained_data/waiting_list.csv")
    df.loc[df["user_id"]==s, "user_id"] = 'file-moved'
    df.to_csv("sample/static/trained_data/waiting_list.csv", index=False)
    import shutil
    old_file='sample/static/img_data/wait_list/'+"wid_"+str(user_id)+'.jpg'
    ts = int(time.time())
    id ="rjd_"+str(ts)
    new_file='sample/static/img_data/reject_list/'+id+'.jpg'
    shutil.copy2(old_file, new_file)
    name=new_file.split('/')
    user_name, ext = os.path.splitext(name[4])
    os.remove(old_file)
    
    for i in range(0,len(waiting_name_list)):
        if(waiting_name_list[i]==s):
            waiting_name_list[i]=user_name
            data=waiting_face_data[i]
    rejected_face_data.append(data)
    rejected_name_list.append(user_name)
    row = [user_name]
    for i in data:
        row.append(float(i))
    with open('sample/static/trained_data/rejected_list.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    data=[{'message':user_id+" is Rejected Successfully"}]
    return HttpResponse(json.dumps(data), content_type="application/json")



def notifi_data(request):
    waiting_list=[]
    with open('sample/static/trained_data/waiting_list.csv') as f:
        data=[line.split(",")[0] for line in f]
    data=reversed(data)
    for i in data:
        if (i !="sample" and i !="file-moved" and i !="user_id" ):
            a={'id':i,'image':'http://192.168.10.26:8000/static/img_data/wait_list/'+str(i)+'.jpg'}
            waiting_list.append(a)
    return HttpResponse(json.dumps(waiting_list), content_type="application/json")

def accept_list(request):
        # get_data(request, 's','ssss');
    accept_list=[]
        # data=(((41, 'wid_1544160905')), (42, 'wid_1544160906'))
        
    with open('sample/static/trained_data/accepted_list.csv') as f: 
        data=[line.split(",")[0] for line in f]
             
        if(data):
            data=reversed(data)
            for i in data:
                a={'id':i}
                accept_list.append(a)
            return render(request,'accept.html',{'data':accept_list,'ip':local_ip,'port':port})
        else:
            return 0
def reject_list(request):
        # get_data(request, 's','ssss');
    reject_list=[]
        # data=(((41, 'wid_1544160905')), (42, 'wid_1544160906'))
        
    with open('sample/static/trained_data/rejected_list.csv') as f: 
        data=[line.split(",")[0] for line in f]
             
        if(data):
            data=reversed(data)
            for i in data:
                a={'id':i}
                reject_list.append(a)
            return render(request,'reject.html',{'data':reject_list,'ip':local_ip,'port':port})
        else:
            return 0    



def accept_api(request):
    accept_list=[]
    with open('sample/static/trained_data/accepted_list.csv') as f:
        data=[line.split(",")[0] for line in f]
        data=reversed(data)
        for i in data:
            if (i !="user_id" ):
                a={'id':i,'image':'http://192.168.10.26:8000/static/img_data/accept_list/'+str(i)+'.jpg'}
                accept_list.append(a)
        return HttpResponse(json.dumps(accept_list), content_type="application/json")

def rej_api(request):
    reject_list=[]
    with open('sample/static/trained_data/rejected_list.csv') as f:
        data=[line.split(",")[0] for line in f]
        data=reversed(data)
        for i in data:
            if (i !="user_id" ):
                a={'id':i,'image':'http://192.168.10.26:8000/static/img_data/reject_list/'+str(i)+'.jpg'}
                reject_list.append(a)
        return HttpResponse(json.dumps(reject_list), content_type="application/json")


def sam(request):
    # sharp=[]
    with open('sample/static/trained_data/sample.csv') as f:
        data=[line for line in f]
        return HttpResponse(json.dumps(data), content_type="application/json")

def test(request):
    # ape=[]
    with open('sample/static/trained_data/test.csv') as f:
        data=[line for line in f]
        return HttpResponse(json.dumps(data), content_type="application/json")

def rev(request):
    # pe=[]
    with open('sample/static/trained_data/review.csv') as f:
        data=[line for line in f]
        return HttpResponse(json.dumps(data), content_type="application/json")

def delete(request):
    d=[]
    import os
    os.remove('sample/static/trained_data/waiting_list.csv')

    import glob
    directory='sample/static/img_data/wait_list/'
    for i in glob.glob(os.path.join(directory,"*.jpg")):
        os.remove(i)
        # d=[{'message':" is Delete_data Successfully"}]
    return HttpResponse(json.dumps(d), content_type="application/json")
def create(request):
    da=[]
    import csv
    s=[['user_id', ' 1',' 2',' 3',' 4',' 5',' 6',' 7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31',' 32',  '33',  '34',  '35',  '36',  '37',  '38', '39','40',  '41',  '42', ' 43', ' 44' ,' 45' , '46',  '47',  '48',  '49',  '50',  '51',  '52',  '53',  '54',  '55',  '56', ' 57',  '58' , '59',  '60',  '61',  '62',  '63',  '64',  '65',  '66' , '67' , '68' , '69',  '70' , '71',  '72',  '73' , '74',  '75' , '76',  '77',  '78',  '79',  '80',  '81',  '82',  '83',  '84', ' 85',  '86',  '87',  '88',  '89',  '90', ' 91',  '92',  '93',  '94'  ,'95',  '96' , '97',  '98',  '99' , '100', '101', '102', '103', '104', '105', '106' ,'107' ,'108 ','109' ,'110', '111', '112', '113' ,'114', '115', '116', '117', '118','119', '120', '121', '122', '123', '124', '125', '126', '127', '128']]
    with open('sample/static/trained_data/waiting_list.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(s)
        da=[{'message':" is create_waiting_list_csv Successfully"}]
    return HttpResponse(json.dumps(da), content_type="application/json")

#reject data clear
def clear(request):
    ata=[]
    import os
    os.remove('sample/static/trained_data/rejected_list.csv')

    import glob
    directory='sample/static/img_data/reject_list/'
    for i in glob.glob(os.path.join(directory,"*.jpg")):
        os.remove(i)
        # ata=[{'message':" is Delete_data Successfully"}]
    return HttpResponse(json.dumps(ata), content_type="application/json")
def add(request):
    ta=[]
    import csv
    s=[['user_id', ' 1',' 2',' 3',' 4',' 5',' 6',' 7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31',' 32',  '33',  '34',  '35',  '36',  '37',  '38', '39','40',  '41',  '42', ' 43', ' 44' ,' 45' , '46',  '47',  '48',  '49',  '50',  '51',  '52',  '53',  '54',  '55',  '56', ' 57',  '58' , '59',  '60',  '61',  '62',  '63',  '64',  '65',  '66' , '67' , '68' , '69',  '70' , '71',  '72',  '73' , '74',  '75' , '76',  '77',  '78',  '79',  '80',  '81',  '82',  '83',  '84', ' 85',  '86',  '87',  '88',  '89',  '90', ' 91',  '92',  '93',  '94'  ,'95',  '96' , '97',  '98',  '99' , '100', '101', '102', '103', '104', '105', '106' ,'107' ,'108 ','109' ,'110', '111', '112', '113' ,'114', '115', '116', '117', '118','119', '120', '121', '122', '123', '124', '125', '126', '127', '128']]
    with open('sample/static/trained_data/rejected_list.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(s)
        ta=[{'message':" is create_rejected_list_csv Successfully"}]
    return HttpResponse(json.dumps(ta), content_type="application/json")

#accept data clear

def cut(request):
    dt=[]
    import os
    os.remove('sample/static/trained_data/accepted_list.csv')

    import glob
    directory='sample/static/img_data/accept_list/'
    for i in glob.glob(os.path.join(directory,"*.jpg")):
        os.remove(i)
        # dt=[{'message':" is Delete_data Successfully"}]
    return HttpResponse(json.dumps(dt), content_type="application/json")
def generate(request):
    qw=[]
    import csv
    s=[['user_id', ' 1',' 2',' 3',' 4',' 5',' 6',' 7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31',' 32',  '33',  '34',  '35',  '36',  '37',  '38', '39','40',  '41',  '42', ' 43', ' 44' ,' 45' , '46',  '47',  '48',  '49',  '50',  '51',  '52',  '53',  '54',  '55',  '56', ' 57',  '58' , '59',  '60',  '61',  '62',  '63',  '64',  '65',  '66' , '67' , '68' , '69',  '70' , '71',  '72',  '73' , '74',  '75' , '76',  '77',  '78',  '79',  '80',  '81',  '82',  '83',  '84', ' 85',  '86',  '87',  '88',  '89',  '90', ' 91',  '92',  '93',  '94'  ,'95',  '96' , '97',  '98',  '99' , '100', '101', '102', '103', '104', '105', '106' ,'107' ,'108 ','109' ,'110', '111', '112', '113' ,'114', '115', '116', '117', '118','119', '120', '121', '122', '123', '124', '125', '126', '127', '128']]
    with open('sample/static/trained_data/accepted_list.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(s)
        qw=[{'message':" is create_accepted_list_csv Successfully"}]
    return HttpResponse(json.dumps(qw), content_type="application/json")                
