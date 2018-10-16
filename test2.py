import csv

with open('user_images.csv', 'r') as readFile:
	reader = csv.reader(readFile)
	lines = list(reader)
	print(list(reader))
	print(lines)

    # with open('user_images.csv', 'w') as writeFile:
    #     writer = csv.writer(writeFile)
    #     writer.writerows(lines)

readFile.close()
    # writeFile.close()