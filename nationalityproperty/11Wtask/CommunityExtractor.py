areasFile = open("C:\\Users\\gph\\workspace\\NishinoNanase\\nationalityproperty\\11Wtask\\areas.txt", 'r', encoding="UTF-8")
communityFile = open("C:\\Users\gph\workspace\\NishinoNanase\\nationalityproperty\\11Wtask\community.txt", 'a+', encoding="UTF-8")
villiageCommunityFile = open("C:\\Users\\gph\\workspace\\NishinoNanase\\nationalityproperty\\11Wtask\\villageCommunity.txt", 'a+', encoding="UTF-8")

count = 1
villiageCount = 1
for line in areasFile.readlines():
    line = line.strip()
    name = line.split(",")[5]
    if "社区" in name:
        communityFile.write(line+"\r")
        print(count)
        count+=1
    else:
        villiageCommunityFile.write(line+"\r")
        print(villiageCount)
        villiageCount+=1
