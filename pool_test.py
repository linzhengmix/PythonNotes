
from multiprocessing import Pool
import time, os, random

def worker(msg):
    t_start = time.time()
    print("%d start, PID is %d" %(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"finished, time consuming %0.3f" %(t_stop-t_start))


po = Pool(3)

for i in range(0,10):
    #worker(i)
    po.apply_async(worker,(i,))


print("---start---")
po.close()
po.join()
print("---end---")
