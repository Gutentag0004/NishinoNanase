import pypinyin
import requests
import bs4
import time
import csv



def getTargetNation(name, Nationslist):
    resultlist =[]
    url = "http://s.tcmap.com.cn/cse/search?q={}&click=1&s=8921814902502906757&nsid="

    target = url.format(name)
    result =  requests.get(target)
    print("resut"+str(result.status_code))
    if(result.status_code != 200):
        print(name)
        print("request fail")
        return resultlist
    co = result.content
    soup = bs4.BeautifulSoup(co)
    list = soup.find_all('a', target='_blank')
    if (len(list) > 0):
        hre = list[0]
        print(hre)
        destination = requests.get(hre['href'])
        print("status"+str(destination.status_code))
        if (destination.status_code != 200):
            print(name)
            print("request fail")
            return resultlist
        soup = bs4.BeautifulSoup(destination.content)
        contentStr = str(soup)
        print(contentStr)
        for nation in Nationslist:
            if nation in contentStr:
                resultlist.append(nation)

    return resultlist
nationsListStr = open("D:\PycharmProjects\gmyproj\\nationalityproperty\\nationslist",'r',encoding="utf-8")


nationsList = []
#获取民族列表
for line in nationsListStr.readlines():
    nationsList.append(line.strip());
print(nationsList)

community = "D:\PycharmProjects\gmyproj\\nationalityproperty\\11Wtask\\community.txt"
villageCommunity = "D:\PycharmProjects\gmyproj\\nationalityproperty\\11Wtask\\villageCommunity.txt"
areasWithNationality = "D:\PycharmProjects\gmyproj\\nationalityproperty\\11Wtask\\areasWithNationality.txt"
testFile = "D:\PycharmProjects\gmyproj\\nationalityproperty\\11Wtask\\test.txt"
def getNationlityFunc(inputName, outPutName):
    count = 0
    up = 0
    down = 0
    count = 1
    input = open(inputName, 'r', encoding="UTF-8")
    output = open(outPutName,'a+', encoding="UTF-8")
    for line in input.readlines():
            print(count)

            count+=1
            down+=1
            name = line.split(",")[7]
            propertylist = []
            for nation in nationsList:
                if nation in name:
                    propertylist.append(nation)
            propertylist.extend(getTargetNation(name, Nationslist=nationsList))
            time.sleep(0.1)
            property = ""
            for i in range(len(propertylist)):
                if str(propertylist[i]) in property:
                    continue
                if i == len(propertylist)-1:
                    property += str(propertylist[i])
                else:
                    property += str(propertylist[i])+"|"
            print("write"+str(count))
            strline = line.strip()+","+property+"\n"

            print(strline)
            output.write(strline)
            if len(propertylist) > 0:
                up +=1
    print(str(up)+"/"+str(down))

    input.close()
    output.close()



#getNationlityFunc(community,areasWithNationality)
# getNationlityFunc(villageCommunity,areasWithNationality)
getNationlityFunc(testFile,areasWithNationality)