

names = open("D:\PycharmProjects\gmyproj\\name",'r',encoding="utf-8")
processedNames = open("D:\PycharmProjects\gmyproj\processedname",'w',encoding="utf-8")

for line in names.readlines():
    list = line.strip().split(" ")
    if(len(list) > 1):
        if(len(list) == 2):
            processedNames.write(list[-1]+"\n")
        else:
            tem = ""
            for string in list[1::]:
                tem += string
            processedNames.write(tem+"\n")
    else :
        if(len(line.strip()) == 0):
            continue
        if str.isdigit(line.strip()):
            continue
        else:
            processedNames.write(line.strip()+"\n")

