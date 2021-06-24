import bs4
import requests
import time

names = open("D:\PycharmProjects\gmyproj\processedname",'r',encoding="utf-8")
lnglatinfo = open("D:\PycharmProjects\gmyproj\lngandlatinfo",'w',encoding="utf-8")
ak = "hGvCxboxNw16CwBkgZdwDUif0cqQdiSK"
url = "http://api.map.baidu.com/geocoding/v3/?output=json&ak=hGvCxboxNw16CwBkgZdwDUif0cqQdiSK&callback=showLocation&address="
# url = url +"吐鲁番地区鄯善县鄯善城镇蒲昌村"
# res = requests.get(url)
# print(res.content)

for name in names.readlines():
    name = name.strip()
    print(name)
    time.sleep(0.06)
    if(len(name) < 5):
        lnglatinfo.write(name+"\n")
    else:
        targetUrl = url+name
        result = requests.get(targetUrl)
        if(result.status_code == 200):
            list = str(result.content, encoding="utf-8").split("lng\":")
            info = list[1].split("},")
            detail = info[0]
            temList = detail.split(",\"lat\":")
            lng = temList[0]
            lat = temList[1]
            lnglatinfo.write(name+","+lng+","+lat+"\n")
        else:
            lnglatinfo.write(name+","+"get fail\n")

#json 解析
