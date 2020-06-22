#!/usr/bin/env python3
#该脚本实现从指定hub.docker.com中的命名空间可以获取所有的镜像名包括其版本号

import json
import requests
from queue import Queue
import threading
import time

def getDockerImg(namespace,page=1):
    while True:
        getNameUrl = 'https://hub.docker.com/v2/repositories/kolla/?page_size=25&page='+str(page)+'&ordering=last_updated'
        try:
            nameRes = requests.get(getNameUrl, timeout = 10)
        except:
            print('url:'+getNameUrl+'request failed')
            f.write(getNameUrl)
        nameText = nameRes.text
        if "Not found" in nameText:
            break
        nameJson = json.loads(nameText)
        for i in range(len(nameJson['results'])):
            dockerImgName = nameJson['results'][i]['name']
            id_queue.put(dockerImgName)
        page += 1
        time.sleep(0.1)
    f.close()

def getTag():
    w = open(r'results.txt', "w+")
    while True:
        page = 1
        try:
            dockerImgName = id_queue.get(timeout=10)
        except:
            break
        while True:
            getTagUrl = 'https://hub.docker.com/v2/repositories/kolla/'+dockerImgName+'/tags/?page_size=25&page='+str(page)
            try:
                tagRes = requests.get(getTagUrl, timeout = 10)
            except:
                print('url:'+getTagUrl+'request failed')
                f.write(getTagUrl)
            tagText = tagRes.text
            tagJson = json.loads(tagText)
            if tagJson['count'] == 0:
                break
            for i in range(len(tagJson['results'])):
                dockerTagName = tagJson['results'][i]['name']
                fullName = dockerImgName + ':' + dockerTagName
                print(fullName)
                w.write(fullName+"\n")
            page += 1
            time.sleep(0.1)
    w.close()

if __name__ == '__main__':
    id_queue = Queue(100)
    f = open(r'failed.txt', "w+")
    namespace = 'kolla' #定义命名空间
    T_img = threading.Thread(target=getDockerImg, args=(namespace,))
    T_tag = threading.Thread(target=getTag)
    T_img.start()
    T_tag.start()
