import time
import threading
import asyncio
import requests

def request_sina():
    sinat1 = time.time()
    res = requests.get("http://www.sina.com")
    #print (res.status_code ,threading.currentThread())
    print('cost:',time.time()-sinat1)
def request_163():
    t2 = time.time()
    res = requests.get("http://www.163.com")
    #print (res.status_code ,threading.currentThread())
    print('cost:',time.time()-t2)
def request_baidu():
    t3 = time.time()
    res = requests.get("http://www.baidu.com")
    #print (res.status_code ,threading.currentThread())
    print('cost:',time.time()-t3)
def hello():
    t1= time.time()
    print('Hello world! (%s)' % threading.currentThread())
    print('Hello again! (%s)' % threading.currentThread())
    print('cost:',time.time()-t1)
t4= time.time()
request_sina()
request_163()
request_baidu()
print('all_time',time.time()-t4)
