import requests
import csv
import json

result=[] #创建一个list容器
fileName='*:\\***\\***.csv' #提前创建好CSV文件，filename指向CSV路径,单反斜杠替换成双反斜杠,示例:'C:\\File\\test.csv'
urls=['http://***.***.***',
'http://***.***.***',
'http://***.***.***',
'http://***.***.***']
#需要测试的各个接口地址

#下面对需要测试的接口地址进行循环请求
for url in urls:
    data1=url  #返回url，用来判断同一组数据内url对应关系
    response=requests.get(url)  #使用requests模块的get函数单次请求接口地址
    data2=(response.json()["code"])   #使用json模块解析code字段返回值
    data3=(response.json()["msg"])    #使用json模块解析msg字段返回值
    data4=(response.json()["data"])   #使用json模块解析data字段返回值
    data=(data1,data2,data3,data4) #拼接
    result.append(data)   #把每一组请求结果添加到list
    with open(fileName,'w',newline='') as csvfile:  #打开本地CSV文件并写入
        csv_writer=csv.writer(csvfile)
        csv_writer.writerows(result)

