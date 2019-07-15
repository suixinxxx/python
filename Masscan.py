import masscan
import traceback
import os
#mas = masscan.PortScanner()
#for i in range(0,20):
#    try:
#        ip = '10.60.119.'+str(i)
#        print(ip)
#        mas.scan(str(ip),ports='0/1000')
#        print (mas.scan_result)
#    except:
#        print ("error!!!!!!!!!!!!!!!")
for i in range(0,100):
    ip = '10.60.119.'+str(i)
    masscan1=os.system('masscan {0} -p 80-8000'.format(str(ip)))
    print (masscan1)
