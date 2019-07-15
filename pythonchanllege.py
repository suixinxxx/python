import requests
import time

t1= time.time() 
for i in range(200,300):
    url ="http://www.pythonchallenge.com/pc/def/{0}.html".format(i)
    response = requests.get(url)
    if response.status_code == 200:
        print (response.text)


print("spend:",time.time()-t1)

import asyncio

async def request_html(n):
    print ("start")
    loop = asyncio.get_event_loop()

    url ="http://www.pythonchallenge.com/pc/def/{0}.html".format(n)
    await loop.run_in_executor(None,requests,url)
async def request_co(n,j):
    print("协程" + str(n) +"启动")
    await request_html(j)
if __name__ == "__main__":
    task = []
    t3 = time.time()
    for i,n in range(200,300):
        task.append(request_co(i,n))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task))
    loop.close()
    print("co spend:",time.time()-t3)
