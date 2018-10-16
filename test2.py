    with open('user_images.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        for x in lines:
            if(x[0]==s):
                x[0] = user_name

    with open('user_images.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    readFile.close()
    writeFile.close()