import csv
# with open('images.csv', 'r') as readFile:
# 	reader = csv.reader(readFile)
# 	lines = list(reader)
# for i in range(1,len(lines)):
# 	data=lines[i]
# 	face_name_list.append(data[0])
# 	en=data[1:]
# 	data=[]
# 	for k in en:
# 		data.append(float(k))
# 	face_data.append(data)

in1=open('images.csv','rb')
reader=csv.reader(in1)
w=open('images.csv','wb')
writee=csv.writer(w)
for i in reader:
	i[2]="suresh"
	w.writer(i)
in1.close()
w.close()
