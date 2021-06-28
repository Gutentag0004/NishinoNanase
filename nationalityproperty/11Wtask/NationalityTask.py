import pypinyin
import requests
import bs4
import time



# 民族列表路径
nationsListPath = "C:\\Users\\gph\\workspace\\NishinoNanase\\nationalityproperty\\nationslist"
# 社区列表路径
community = "C:\\Users\\gph\\workspace\\NishinoNanase\\nationalityproperty\\11Wtask\\community.txt"
# 村委会路径
villageCommunity = "C:\\Users\\gph\\workspace\\NishinoNanase\\nationalityproperty\\11Wtask\\villageCommunity.txt"
# 获取民族成分之后的结果路径
areasWithNationality = "C:\\Users\\gph\\workspace\\NishinoNanase\\nationalityproperty\\11Wtask\\areasWithNationality.txt"
contentFile = "C:\\Users\\gph\\workspace\\NishinoNanase\\nationalityproperty\\11Wtask\\content.txt"
nationsListStr = open(nationsListPath,'r',encoding="utf-8")
nationsList = []

#获取民族列表
for line in nationsListStr.readlines():
    nationsList.append(line.strip());
print(nationsList)

# function  request请求 获取民族列表
def getTargetNation(name, Nationslist):
    print("request")
    resultlist =[]
    url = "http://s.tcmap.com.cn/cse/search?q={}&click=1&s=8921814902502906757&nsid="

    target = url.format(name)
    result = ""
    try:
        result = requests.get(target, timeout=5)
    except BaseException:
        print('timeout exception')
        return resultlist
    else:
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
            for nation in Nationslist:
                if nation[:-1] in contentStr:
                    resultlist.append(nation)


    return resultlist

def getContent(name):
    print("request")
    resultlist = []
    url = "http://s.tcmap.com.cn/cse/search?q={}&click=1&s=8921814902502906757&nsid="
    target = url.format(name)
    result = ""
    try:
        result = requests.get(target, timeout=5)
    except BaseException:
        print('timeout exception')
        return resultlist
    else:
        print("resut" + str(result.status_code))
        if (result.status_code != 200):
            print(name)
            print("request fail")
            return resultlist
        co = result.content
        print(co)
        strCo = co.decode().strip()
        strCo = strCo.replace("\n","").replace("\r","").replace("\t","")
        return strCo


# main function 根据input文件  获取对应文件中对应地址的民族成分输出到outPut中
# def getNationlityFunc(inputName, outPutName):
#     count = 0
#     up = 0
#     down = 0
#     count = 1
#     input = open(inputName, 'r', encoding="UTF-8")
#     output = open(outPutName,'a+', encoding="UTF-8")
#     for line in input.readlines():
#             print(count)
#
#             count+=1
#             down+=1
#             name = line.split(",")[7]
#             propertylist = []
#             for nation in nationsList:
#                 if nation in name:
#                     propertylist.append(nation)
#             propertylist.extend(getTargetNation(name, Nationslist=nationsList))
#             time.sleep(0.1)
#             property = ""
#             for i in range(len(propertylist)):
#                 if str(propertylist[i]) in property:
#                     continue
#                 if i == len(propertylist)-1:
#                     property += str(propertylist[i])
#                 else:
#                     property += str(propertylist[i])+"|"
#             print("write"+str(count))
#             strline = line.strip()+","+property+"\n"
#
#             print(strline)
#             output.write(strline)
#             if len(propertylist) > 0:
#                 up +=1
#     print(str(up)+"/"+str(down))
#     output.flush()
#     input.close()
#     output.close()



# getNationlityFunc(community,areasWithNationality)
# getNationlityFunc(villageCommunity,areasWithNationality)

def contentCrawler(inputName, outputName):

    input = open(inputName, 'r', encoding="UTF-8")
    output = open(outputName, 'a+', encoding="UTF-8")
    for line in input.readlines():
        print(line.split(",")[0])
        name = line.split(",")[7]
        webContent = getContent(name)
        time.sleep(0.1)
        print(type(webContent))
        print(type(line.split(",")[0]))
        output.write(str(line.split(",")[0])+":::"+webContent+"\n")
        output.flush()

    input.close()
    output.close()


contentCrawler(community, contentFile)
contentCrawler(villageCommunity,contentFile)