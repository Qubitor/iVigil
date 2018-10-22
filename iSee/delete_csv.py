import csv

with open("/home/suresh/project/iVigil/iSee/static/trained_data/user_face_info (copy).csv") as fr:
    cr = csv.reader(fr)
    title = next(cr)
    with open("/home/suresh/project/iVigil/iSee/static/trained_data/waiting_list (copy).csv","w") as fw:  # add ,newline='' for python 3
        cw = csv.writer(fw)
        cw.writerow(title)
        for row in cr:
            row[0]=""
            cw.writerow(row)


# with open('/home/suresh/project/iVigil/iSee/static/trained_data/user_face_info (copy).csv', 'r') as readFile:
# 	reader = csv.reader(readFile)
# 	lines = list(reader)
# 	for x in lines:
# 		if(x[0]=="ssss"):
# 			x[0] = " "

# with open('/home/suresh/project/iVigil/iSee/static/trained_data/user_face_info (copy).csv', 'w') as rmdata:
# 	writer = csv.writer(rmdata)
# 	writer.writerows(lines)
# 	readFile.close()
# 	rmdata.close()