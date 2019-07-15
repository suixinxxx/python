#import time
#import threading
#import asyncio
#import requests
#from concurrent import futures
#
#async def request_sina():
#    sinat1 = time.time()
#    res = requests.get("http://www.sina.com")
#    print (res.status_code ,threading.currentThread())
#    print('cost:',time.time()-sinat1)
#async def request_163():
#    t2 = time.time()
#    res = requests.get("http://www.163.com")
#    print (res.status_code ,threading.currentThread())
#    print('cost:',time.time()-t2)
#async def request_baidu():
#    t3 = time.time()
#    res = requests.get("http://www.baidu.com")
#    print (res.status_code ,threading.currentThread())
#    print('cost:',time.time()-t3)
#async def hello():
#    t1= time.time()
#    print('Hello world! (%s)' % threading.currentThread())
#    await asyncio.sleep(3)
#    print('Hello again! (%s)' % threading.currentThread())
#    print('cost:',time.time()-t1)
#t4= time.time()
#loop = asyncio.get_event_loop()
#tasks = [request_163(), request_sina(),request_baidu()]
#loop.run_until_complete(asyncio.wait(tasks))
#loop.close()
#print('all_time',time.time()-t4)

#import asyncio
#import requests
#import time 
#async def main():
#    t1= time.time()
#    loop = asyncio.get_event_loop()
#    future1 = loop.run_in_executor(None, requests.get, 'http://www.163.com')
#    future2 = loop.run_in_executor(None, requests.get, 'http://www.baidu.com')
#    future2 = loop.run_in_executor(None, requests.get, 'http://www.sina.com')
#    response1 = await future1
#    response2 = await future2
#    #print(response1.text)
#    #print(response2.text)
#    print('cost',time.time()-t1)
#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())
import time
import asyncio
import concurrent.futures
import requests

async def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor, 
                requests.get, 
                'http://example.org/'
            )
            for i in range(20)
        ]
        for response in await asyncio.gather(*futures):
            pass

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print('cost',time.time()-t1)
